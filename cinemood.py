import random

# ============================================
# BANNER
# ============================================

BANNER = r"""
  ___  ____  _  _  ____  __  __  _____  _____  ____  
 / __)(_  _)( \( )( ___)(  \/  )(  _  )(  _  )(  _ \ 
( (__  _)(_  )  (  )__)  )    (  )(_)(  )(_)(  )(_) )
 \___)(____)(_)\_)(____)(_/\/\_)(_____)(_____)(____/
 """

# ============================================
# BANCO DE FILMES POR HUMOR/EXPERIÊNCIA
# ============================================

FILMES = {
    "1": {
        "emoji": "😂",
        "titulo": "Quero morrer de rir",
        "lista": [
            "As Branquelas", "Shrek", "A Nova Onda do Imperador", "Miss Simpatia",
            "Se Beber, Não Case", "O Auto da Compadecida", "Uma Noite no Museu",
            "Tá Dando Onda", "Madagascar", "Legalmente Loira", "Meninas Malvadas",
            "Minha Mãe é uma Peça", "Diário de um Banana", "Click",
            "Curtindo a Vida Adoidado", "Debi & Lóide", "Este É o Fim", "Zoolander",
            "A Máscara", "Ace Ventura: Um Detetive Diferente", "Ted",
            "As Patricinhas de Beverly Hills", "Superbad: É Hoje",
        ],
    },
    "2": {
        "emoji": "😭",
        "titulo": "Quero chorar até desidratar",
        "lista": [
            "Um Olhar do Paraíso", "À Espera de um Milagre", "Diário de uma Paixão",
            "Viva, a Vida é uma Festa", "Uma Prova de Amor", "Te Amarei para Sempre",
            "Questão de Tempo", "A Culpa é das Estrelas", "As Vantagens de Ser Invisível",
            "A Beleza Oculta", "Ponte para Terabítia", "Robô Selvagem",
            "O Menino do Pijama Listrado", "Sempre ao Seu Lado", "Marley e Eu",
            "O Lado Bom da Vida", "A Corrente do Bem", "Meu Amigo Enzo",
            "Ainda Alice", "P.S. Eu Te Amo", "Como Estrelas na Terra", "Extraordinário",
            "O Menino que Descobriu o Vento",
        ],
    },
    "3": {
        "emoji": "❤️",
        "titulo": "Quero me apaixonar",
        "lista": [
            "Como Eu Era Antes de Você", "Orgulho e Preconceito",
            "Ele Não Está Tão a Fim de Você", "10 Coisas que Eu Odeio em Você",
            "Um Lugar Chamado Notting Hill", "Elementos", "Casa Comigo?",
            "Enquanto Você Dormia", "O Diário de Bridget Jones", "A Proposta",
            "O Amor Não Tira Férias", "Simplesmente Acontece",
            "O Casamento do Meu Melhor Amigo", "Antes do Amanhecer", "E se Fosse Verdade",
            "Simplesmente Amor", "500 Dias com Ela", "Diário de Bridget Jones: No Limite da Razão",
            "Como Perder um Homem em 10 Dias", "Cartas para Julieta",
            "Um Amor para Recordar", "La La Land",
        ],
    },
    "4": {
        "emoji": "🤔",
        "titulo": "Quero refletir",
        "lista": [
            "A Chegada", "O Jogo da Imitação", "O Show de Truman", "Interstellar",
            "A Origem", "A Lista de Schindler", "Divertida Mente", "Soul",
            "Sonhos de Trem", "Coringa", "Brilho Eterno de uma Mente sem Lembranças",
            "Vidas Passadas", "A Ghost Story", "O Quarto de Jack", "Garota, Interrompida",
            "Clube da Luta", "O Labirinto do Fauno", "A Vida é Bela",
            "Blade Runner 2049", "Ex Machina", "Her", "O Curioso Caso de Benjamin Button",
            "Réquiem para um Sonho",
        ],
    },
    "5": {
        "emoji": "😱",
        "titulo": "Quero sentir medo",
        "lista": [
            "Obsessão", "O Iluminado", "Corra!", "O Exorcista",
            "O Massacre da Serra Elétrica", "Hereditário", "A Hora do Pesadelo",
            "A Hora do Mal", "Midsommar", "Eu Sei o que Vocês Fizeram no Verão Passado",
            "Pânico", "Faça Ela Voltar", "A Hora da Sua Morte", "Jogos Mortais", "Nós",
            "Sexta-Feira 13", "Annabelle", "Invocação do Mal", "Atividade Paranormal",
            "It: A Coisa", "Longlegs", "Talk to Me: Fale com os Mortos",
        ],
    },
    "6": {
        "emoji": "🔥",
        "titulo": "Quero adrenalina",
        "lista": [
            "Mad Max: Estrada da Fúria", "John Wick", "Missão Impossível",
            "Duro de Matar", "Em Ritmo de Fuga", "O Exterminador do Futuro", "Matrix",
            "A Odisseia", "Guardiões da Galáxia", "Gladiador", "Top Gun: Maverick",
            "X-Men: O Filme", "Jogos Vorazes", "Piratas do Caribe: A Maldição do Pérola Negra",
            "Capitão América: Guerra Civil", "Velozes e Furiosos 7", "007: Sem Tempo Para Morrer",
            "Duro de Matar 2", "Missão: Impossível - Efeito Fallout", "Kill Bill: Volume 1",
            "Homem de Ferro", "Vingadores: Ultimato", "Black Panther: Wakanda Para Sempre",
        ],
    },
    "7": {
        "emoji": "💭",
        "titulo": "Quero fugir da realidade",
        "lista": [
            "Alice no País das Maravilhas", "Avatar", "O Lar das Crianças Peculiares",
            "Como Treinar o Seu Dragão", "As Crônicas de Nárnia", "A Viagem de Chihiro",
            "Coração de Tinta", "Viagem ao Centro da Terra", "Malévola",
            "Animais Fantásticos e Onde Habitam", "Duna", "O Castelo Animado",
            "Mestres do Universo", "Super Mario Bros: O Filme", "Wicked",
            "Harry Potter e a Pedra Filosofal", "O Hobbit: Uma Jornada Inesperada",
            "Percy Jackson e o Ladrão de Raios", "Stardust: O Mistério da Estrela",
            "Onde Vivem os Monstros", "Pan: Viagem à Terra do Nunca",
            "A Fantástica Fábrica de Chocolate",
        ],
    },
    "8": {
        "emoji": "👀",
        "titulo": "Quero me surpreender",
        "lista": [
            "Não Olhe para Cima", "Backrooms", "Fragmentado", "Mãe!", "Águas Rasas",
            "Um Lugar Silencioso", "Sinais", "Bugonia", "Garota Exemplar",
            "Telefone Preto", "Ilha do Medo", "Anatomia de uma Queda",
            "Five Nights at Freddy's: O Pesadelo sem Fim", "O Ilusionista", "Corpo Fechado",
            "Se7en: Os Sete Crimes Capitais", "O Silêncio dos Inocentes", "Zodíaco",
            "Prisioneiros", "A Garota no Trem",
        ],
    },
    "9": {
        "emoji": "🎵",
        "titulo": "Quero cantar até perder a voz",
        "lista": [
            "Frozen 2", "O Rei Leão 2", "Encantada", "A Bela e a Fera", "Mamma Mia",
            "O Rei do Show", "Irmão Urso", "Moana", "Mulan", "O Príncipe do Egito",
            "O Mágico de Oz", "Enrolados", "Tarzan", "Nem que a Vaca Tussa",
            "A Pequena Sereia", "A Bela Adormecida", "Cinderela", "Pocahontas",
            "Hércules", "Aladdin", "Grease: Nos Tempos da Brilhantina",
            "Sing: Quem Canta Seus Males Espanta", "Rocketman",
        ],
    },
    "10": {
        "emoji": "👤",
        "titulo": "Quero me redescobrir como ser humano",
        "lista": [
            "Brokeback Mountain", "Love, Simon", "Me Chame pelo Seu Nome",
            "Imagine Eu e Você", "Nunca Fui Santa", "Vermelho, Branco e Sangue Azul",
            "Um Amor Secreto", "Luar", "O País de Deus", "Honey, Não!",
            "Twinless: Um Gêmeo a Menos", "Paloma", "Retrato de uma Jovem em Chamas",
            "Matthias e Maxime", "Rafiki", "Carol", "A Vida de Adèle", "Elisa e Marcela",
            "Milk: A Voz da Igualdade", "Pride", "A Garota Dinamarquesa",
            "Feliz Dia Meu Amor", "Bohemian Rhapsody",
        ],
    },
    "11": {
        "emoji": "👩‍🦰",
        "titulo": "Quero me redescobrir como mulher",
        "lista": [
            "De Repente 30", "O Diabo Veste Prada", "Uma Linda Mulher", "Miss Simpatia",
            "Adoráveis Mulheres", "Red: Crescer é uma Fera", "Eu, Tonya",
            "O Diário da Princesa", "Barbie", "Legalmente Loira", "Meninas Malvadas",
            "Lady Bird", "Estrelas Além do Tempo", "Cruella", "Mulan",
            "Mulher-Maravilha", "As Sufragistas", "Erin Brockovich - Uma Mulher de Talento",
            "Histórias Cruzadas", "Pequenas Mulheres", "RBG: Rede de Justiça",
        ],
    },
    "12": {
        "emoji": "🌍",
        "titulo": "Quero descobrir o mundo",
        "lista": [
            "Encontros e Desencontros", "Na Natureza Selvagem", "Diários de Motocicleta",
            "Up: Altas Aventuras", "A Vida Secreta de Walter Mitty", "Para Roma, com Amor",
            "Sob o Sol da Toscana", "A Praia", "Última Viagem a Vegas",
            "Paris Pode Esperar", "Thelma & Louise", "O Turista", "Meia-Noite em Paris",
            "Antes de Partir", "Entre Montanhas", "Comer, Rezar, Amar", "Selvagem",
            "127 Horas", "Náufrago", "A Volta ao Mundo em 80 Dias",
        ],
    },
}

SAIR = "0"


# ============================================
# BARALHO DE FILMES (evita repetir até esgotar)
# ============================================

class BaralhoDeFilmes:
    """Embaralha os filmes de um humor e vai distribuindo um por um.
    Quando acaba, embaralha de novo — evitando repetir a última carta
    logo na primeira do novo embaralhamento, se der."""

    def __init__(self, filmes):
        self._filmes_originais = list(filmes)
        self._pilha = []
        self._ultimo = None
        self._reabastecer()

    def _reabastecer(self):
        nova_pilha = list(self._filmes_originais)
        random.shuffle(nova_pilha)
        if self._ultimo is not None and len(nova_pilha) > 1 and nova_pilha[-1] == self._ultimo:
            nova_pilha[0], nova_pilha[-1] = nova_pilha[-1], nova_pilha[0]
        self._pilha = nova_pilha

    def sacar(self):
        if not self._pilha:
            self._reabastecer()
        filme = self._pilha.pop()
        self._ultimo = filme
        return filme


def montar_baralhos():
    return {chave: BaralhoDeFilmes(dados["lista"]) for chave, dados in FILMES.items()}


# ============================================
# INTERFACE
# ============================================

def mostrar_titulo():
    print(BANNER)
    print("Encontre um filme para o seu momento atual!\n")


def mostrar_menu():
    print("Como você quer se sentir hoje?\n")
    for chave, dados in FILMES.items():
        print(f"{chave} - {dados['emoji']} {dados['titulo']}")
    print(f"{SAIR} - 🚪 Sair\n")


def pedir_escolha():
    """Pede a escolha do usuário; só aceita opções válidas.
    Ctrl+C ou Ctrl+D encerram o programa direto, sem travar."""
    opcoes_validas = set(FILMES.keys()) | {SAIR}
    while True:
        try:
            escolha = input("Digite o número da sua escolha: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n🍿 Até a próxima sessão de cinema!")
            raise SystemExit(0)
        if escolha in opcoes_validas:
            return escolha
        print(f"❌ Opção inválida. Escolha um número de {SAIR} a {len(FILMES)}.\n")


def recomendar_filme(escolha, baralhos):
    dados = FILMES[escolha]
    filme = baralhos[escolha].sacar()
    print(f"\n{dados['emoji']} Recomendação para \"{dados['titulo']}\": {filme}\n")


def perguntar_continuar():
    try:
        resposta = input("Quer outra recomendação? (s/n): ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return False
    return resposta in ("s", "sim", "")


def main():
    mostrar_titulo()
    baralhos = montar_baralhos()

    while True:
        mostrar_menu()
        escolha = pedir_escolha()

        if escolha == SAIR:
            print("\n🍿 Até a próxima sessão de cinema!")
            break

        recomendar_filme(escolha, baralhos)

        if not perguntar_continuar():
            print("\n🍿 Até a próxima sessão de cinema!")
            break
        print()


if __name__ == "__main__":
    main()