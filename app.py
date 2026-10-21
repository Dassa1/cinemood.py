"""
Interface web do Cinemood.

Este arquivo apenas IMPORTA o cinemood.py (que fica intacto, na mesma pasta)
e reaproveita FILMES e montar_baralhos(). Nada do código original é alterado.

Pôsteres, sinopse e "onde assistir" vêm do tmdb.py (API do TMDB).

Como rodar:
    pip install streamlit
    streamlit run app.py
"""

import os
from urllib.parse import quote_plus

import streamlit as st

import cinemood as cm  # código original, sem modificações
import tmdb

st.set_page_config(page_title="Cinemood", page_icon="🎬", layout="centered")

st.markdown(
    """
    <style>
      .cartao-humor { opacity: .75; margin: 0 0 .2rem 0; }
      .cartao-filme { font-size: 2rem; font-weight: 700; line-height: 1.2; margin: 0 0 .2rem 0; }
      .cartao-meta  { opacity: .75; margin: 0 0 .8rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


def chave_tmdb():
    """Lê a chave de .streamlit/secrets.toml ou da variável de ambiente."""
    try:
        return st.secrets["TMDB_API_KEY"]
    except Exception:
        return os.environ.get("TMDB_API_KEY")


@st.cache_data(ttl=60 * 60 * 24, show_spinner=False)
def detalhes_do_filme(titulo: str, chave: str):
    """Consulta o TMDB uma vez por filme por dia (erros não ficam em cache)."""
    return tmdb.buscar_filme(titulo, chave)


# ------------------------------------------------------------
# Estado da sessão: os baralhos ficam guardados para que o filme
# não se repita até a lista do humor esgotar (lógica do original).
# ------------------------------------------------------------
if "baralhos" not in st.session_state:
    st.session_state.baralhos = cm.montar_baralhos()
    st.session_state.chave = None
    st.session_state.filme = None


def sortear(chave: str) -> None:
    """Saca o próximo filme do baralho do humor escolhido."""
    st.session_state.chave = chave
    st.session_state.filme = st.session_state.baralhos[chave].sacar()


# ------------------------------------------------------------
# Tela
# ------------------------------------------------------------
st.title("🎬 Cinemood")
st.write("Encontre um filme para o seu momento atual.")

resultado = st.container()

st.subheader("Como você quer se sentir hoje?")

colunas = st.columns(2)
for i, (chave, dados) in enumerate(cm.FILMES.items()):
    with colunas[i % 2]:
        st.button(
            f"{dados['emoji']} {dados['titulo']}",
            key=f"humor_{chave}",
            on_click=sortear,
            args=(chave,),
            use_container_width=True,
        )

with resultado:
    chave = st.session_state.chave
    filme = st.session_state.filme

    if chave is None or filme is None:
        st.info("Escolha um humor abaixo para receber uma recomendação.")
    else:
        dados = cm.FILMES[chave]

        # Busca os detalhes no TMDB (se houver chave configurada)
        info, aviso = None, None
        api_key = chave_tmdb()
        if not api_key:
            aviso = (
                "Configure a chave do TMDB para ver pôster, sinopse e onde assistir "
                "(veja as instruções do projeto)."
            )
        else:
            try:
                info = detalhes_do_filme(filme, api_key)
            except tmdb.TMDBErro as erro:
                aviso = f"{erro} Mostrando só o título."

        # Links (usam o TMDB quando possível; senão, buscas genéricas)
        trailer = f"https://www.youtube.com/results?search_query={quote_plus(filme + ' trailer')}"
        assistir = (info or {}).get("link_assistir") or (
            f"https://www.justwatch.com/br/busca?q={quote_plus(filme)}"
        )

        col_poster, col_texto = st.columns([1, 2], gap="large")

        with col_poster:
            if info and info["poster"]:
                st.image(info["poster"], use_container_width=True)
            else:
                st.markdown("## 🎞️")

        with col_texto:
            st.markdown(
                f'<p class="cartao-humor">{dados["emoji"]} {dados["titulo"]}</p>'
                f'<p class="cartao-filme">{filme}</p>',
                unsafe_allow_html=True,
            )

            if info:
                meta = []
                if info["ano"]:
                    meta.append(info["ano"])
                if info["nota"]:
                    meta.append(f"⭐ {info['nota']:.1f}")
                if meta:
                    st.markdown(
                        f'<p class="cartao-meta">{"  ·  ".join(meta)}</p>',
                        unsafe_allow_html=True,
                    )
                if info["sinopse"]:
                    st.write(info["sinopse"])

                if info["streaming"]:
                    st.write("📺 **No streaming:** " + ", ".join(info["streaming"]))
                elif info["aluguel"] or info["compra"]:
                    st.write(
                        "💳 **Para alugar ou comprar:** "
                        + ", ".join(dict.fromkeys(info["aluguel"] + info["compra"]))
                    )
                else:
                    st.write("📺 Sem informação de streaming no Brasil por enquanto.")
            elif api_key and not aviso:
                st.caption("Não encontrei detalhes deste título no TMDB.")

            if aviso:
                st.caption(aviso)

            b1, b2, b3 = st.columns(3)
            with b1:
                st.button(
                    "🔄 Outra",
                    key="outra",
                    on_click=sortear,
                    args=(chave,),
                    use_container_width=True,
                )
            with b2:
                st.link_button("▶️ Trailer", trailer, use_container_width=True)
            with b3:
                st.link_button("📺 Assistir", assistir, use_container_width=True)

st.divider()
st.caption(
    "Este produto usa a API do TMDB, mas não é endossado nem certificado pelo TMDB. "
    "Informações de onde assistir fornecidas pelo JustWatch."
)