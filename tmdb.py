"""
Integração com a API do TMDB (The Movie Database).

Módulo independente: não depende do Streamlit nem do cinemood.py, então
pode ser reaproveitado depois em uma API (FastAPI) ou em um app de celular.

Só usa a biblioteca padrão do Python (nenhuma instalação extra).
"""

import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API = "https://api.themoviedb.org/3"
IMAGENS = "https://image.tmdb.org/t/p/w500"


class TMDBErro(Exception):
    """Falha de comunicação com o TMDB (rede, chave inválida, limite)."""


def _get(caminho: str, chave: str, **params) -> dict:
    """GET na API. Aceita a chave v3 (api_key) ou o token v4 (começa com 'eyJ')."""
    headers = {"accept": "application/json"}
    if chave.startswith("eyJ"):
        headers["Authorization"] = f"Bearer {chave}"
    else:
        params["api_key"] = chave

    url = f"{API}{caminho}?{urlencode(params)}"
    try:
        with urlopen(Request(url, headers=headers), timeout=8) as resposta:
            return json.load(resposta)
    except HTTPError as e:
        if e.code == 401:
            raise TMDBErro("Chave do TMDB inválida.") from e
        raise TMDBErro(f"O TMDB respondeu com erro {e.code}.") from e
    except (URLError, TimeoutError, ValueError) as e:
        raise TMDBErro("Não foi possível falar com o TMDB.") from e


def _separar_ano(titulo: str):
    """'Frankenstein (2025)' -> ('Frankenstein', '2025'). Sem ano -> (titulo, None)."""
    m = re.search(r"\s*\((\d{4})\)\s*$", titulo)
    if m:
        return titulo[: m.start()].strip(), m.group(1)
    return titulo.strip(), None


def buscar_filme(titulo: str, chave: str, pais: str = "BR"):
    """
    Procura o filme pelo título e devolve um dicionário com:
      id, titulo, ano, sinopse, nota, poster, link_tmdb,
      link_assistir (página com onde ver no país), streaming, aluguel, compra

    Devolve None se o filme não for encontrado.
    Levanta TMDBErro se houver problema de rede ou de chave.
    """
    nome, ano = _separar_ano(titulo)

    params = {"query": nome, "language": "pt-BR", "include_adult": "false"}
    if ano:
        params["year"] = ano

    resultados = _get("/search/movie", chave, **params).get("results", [])
    if not resultados:
        return None

    # O TMDB já ordena por relevância; prefere o primeiro que tenha pôster.
    filme = next((r for r in resultados if r.get("poster_path")), resultados[0])

    provedores = (
        _get(f"/movie/{filme['id']}/watch/providers", chave)
        .get("results", {})
        .get(pais, {})
    )

    def nomes(tipo):
        return [p["provider_name"] for p in provedores.get(tipo, [])]

    caminho_poster = filme.get("poster_path")
    return {
        "id": filme["id"],
        "titulo": filme.get("title") or nome,
        "ano": (filme.get("release_date") or "")[:4],
        "sinopse": filme.get("overview") or "",
        "nota": filme.get("vote_average") or 0,
        "poster": f"{IMAGENS}{caminho_poster}" if caminho_poster else None,
        "link_tmdb": f"https://www.themoviedb.org/movie/{filme['id']}",
        "link_assistir": provedores.get("link"),
        "streaming": nomes("flatrate"),
        "aluguel": nomes("rent"),
        "compra": nomes("buy"),
    }