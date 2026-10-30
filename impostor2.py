import random
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Jogo do Impostor", page_icon="🔪🩸", layout="centered"
)

st.title("🔪🩸 Jogo do Impostor")
st.markdown("---")

# Dicionário de Categorias com Palavras e Dicas Diferenciadas
CATEGORIAS = {
    "Comidas & Bebidas": {
        "Pizza": [
            "É algo muito popular no fim de semana.",
            "Normalmente é dividida em fatias ou pedaços.",
            "Costuma levar queijo derretido por cima.",
            "Muitas pessoas comem usando as mãos.",
        ],
        "Hambúrguer": [
            "É muito associado a lanchonetes e fast-food.",
            "Geralmente vem montado dentro de um pão.",
            "Costuma ser acompanhado por batata frita.",
            "Pode levar vários molhos e acompanhamentos.",
        ],
        "Sushi": [
            "É um prato tradicional de origem oriental.",
            "Muitos dos seus tipos levam peixe e arroz.",
            "Frequentemente consumido com molho shoyu.",
            "Geralmente é servido em pedaços pequenos ou rolinhos.",
        ],
        "Chocolate": [
            "É um doce muito popular feito a partir do cacau.",
            "Existe nas versões ao leite, meio amargo e branco.",
            "Pode derreter facilmente no calor.",
            "É um presente muito comum em datas comemorativas.",
        ],
        "Sorvete": [
            "É uma sobremesa fria e refrescante.",
            "Muito consumido em dias quentes e no verão.",
            "Pode ser servido em casquinha ou no copo.",
            "Existe em uma grande variedade de sabores e caldas.",
        ],
    },
    "Objetos do Cotidiano": {
        "Celular": [
            "É um aparelho eletrônico de uso diário e pessoal.",
            "Precisa ter a bateria recarregada com frequência.",
            "Usado para comunicação, jogos e redes sociais.",
            "Cabe no bolso ou na palma da mão.",
        ],
        "Relógio": [
            "Serve para medir ou acompanhar o tempo.",
            "Pode ser de pulso, de parede ou digital.",
            "Costuma marcar horas, minutos e segundos.",
            "É um acessório funcional e também estético.",
        ],
        "Garrafa": [
            "É um recipiente usado para armazenar líquidos.",
            "Muitas pessoas levam para a academia ou trabalho.",
            "Pode ser de plástico, vidro ou metal térmico.",
            "Possui uma tampa para evitar vazamentos.",
        ],
        "Mochila": [
            "É usada para transportar objetos com facilidade.",
            "Muito comum no dia a dia escolar ou de trabalho.",
            "Possui alças para ser carregada nas costas.",
            "Geralmente tem vários compartimentos e zíperes.",
        ],
    },
    "Animais": {
        "Cachorro": [
            "É considerado um dos animais mais fiéis ao ser humano.",
            "Muito comum como animal de estimação em casas.",
            "Gosta de passear e brincar com bolinhas.",
            "Comunica-se emitindo latidos ou ganidos.",
        ],
        "Gato": [
            "É um animal de estimação bastante independente.",
            "Tem grande habilidade de salto e agilidade.",
            "É conhecido por miar e se lamber para se limpar.",
            "Costuma gostar de se espreguiçar e dormir bastante.",
        ],
        "Tubarão": [
            "É um grande predador dos oceanos.",
            "Possui dentes afiados e barbatanas visíveis.",
            "É muito retratado em filmes de suspense no mar.",
            "Respira por guelras debaixo d'água.",
        ],
        "Elefante": [
            "É um dos maiores mamíferos terrestres do mundo.",
            "Possui uma tromba longa e orelhas bem grandes.",
            "É conhecido por ter uma excelente memória.",
            "É um animal herbívoro de grande porte.",
        ],
        "Leão": [
        "É conhecido como o rei da selva e vive em grupos chamados bandos.",
        "Os machos possuem uma juba imponente ao redor do pescoço.",
        "São carnívoros e excelentes caçadores, especialmente as fêmeas.",
        "Habitam principalmente as savanas africanas."
    ],
    "Tigre": [
        "É o maior felino do mundo e se destaca por sua pelagem alaranjada com listras pretas.",
        "Ao contrário da maioria dos felinos, os tigres adoram água e nadam muito bem.",
        "São animais solitários e de hábitos predominantemente noturnos.",
        "Encontrados principalmente nas florestas e selvas da Ásia."
    ],
    "Urso": [
        "É um mamífero de grande porte, conhecido por sua força e robustez.",
        "Algumas espécies passam o inverno dormindo em um processo chamado hibernação.",
        "Possuem uma dieta variada, alimentando-se de plantas, peixes e mel.",
        "Existem várias espécies, como o urso-pardo, o urso-polar e o panda."
    ],
    "Coelho": [
        "É um pequeno mamífero herbívoro conhecido por suas orelhas longas e saltos rápidos.",
        "Possui dentes incisivos que crescem continuamente durante toda a sua vida.",
        "Vive geralmente em tocas subterrâneas construídas em grupos chamados colônias.",
        "É um animal muito ágil e de reprodução rápida."
    ],
    "Cavalo": [
        "É um mamífero de grande porte domesticado pelo ser humano há milhares de anos.",
        "Possui excelente capacidade de corrida e sentidos muito apurados, como a audição.",
        "Alimenta-se principalmente de grama e capim, sendo um animal herbívoro.",
        "É utilizado historicamente para transporte, trabalho no campo e esportes."
    ],
    "Golfinho": [
        "É um mamífero aquático extremamente inteligente e sociável.",
        "Vive em grupos chamados bandos ou colônias e se comunica por meio de cliques e assobios.",
        "Utiliza a ecolocalização para navegar e encontrar alimentos na água.",
        "Precisa vir à superfície regularmente para respirar oxigênio pelo espiráculo."
    ],
    "Águia": [
        "É uma ave de rapina de grande porte com uma visão extremamente aguçada.",
        "Possui garras fortes e um bico curvo adaptado para caçar presas.",
        "Constrói seus ninhos, chamados ninhos de águia ou penhascos, em locais altos e de difícil acesso.",
        "É considerada um símbolo de força e liberdade em várias culturas."
    ],

    
    },
    "Profissões": {
        "Médico": [
            "Profissional focado na saúde e no diagnóstico.",
            "Trabalha em consultórios, postos ou hospitais.",
            "Usa instrumentos como estetoscópio.",
            "Examina pacientes e receita tratamentos.",
        ],
        "Professor": [
            "Trabalha focado no ensino e no aprendizado.",
            "Costuma atuar em escolas, cursos ou universidades.",
            "Prepara aulas, explica conteúdos e aplica avaliações.",
            "Utiliza lousas, livros e apresentações.",
        ],
        "Bombeiro": [
            "Atua em situações de emergência e resgate.",
            "É muito lembrado no combate a incêndios.",
            "Usa uniformes de proteção e equipamentos especiais.",
            "Atende chamados urgentes para salvar pessoas e locais.",
        ],
    },
    "Pessoas Famosas": {
        "Neymar": [
            "É um jogador de futebol brasileiro muito conhecido mundialmente.",
            "É famoso por seus dribles e habilidade em campo.",
            "Já jogou na Europa e na seleção brasileira.",
            "Sua imagem atrai grande atenção da mídia e das redes.",
        ],
        "Taylor Swift": [
            "É uma famosa cantora e compositora internacional.",
            "É conhecida por lotar estádios em suas turnês mundiais.",
            "Transitou do estilo country para o pop.",
            "Tem uma legião de fãs muito dedicados pelo mundo.",
        ],
    },
    "Marcas & Logotipos": {
        "Nike": [
            "É uma marca de produtos esportivos famosa no mundo todo.",
            "Seu símbolo lembra um cheque ou verificação visual.",
            "Produz tênis, roupas e acessórios esportivos.",
            "Patrocina grandes atletas e clubes de futebol.",
        ],
        "Apple": [
            "É uma gigante de tecnologia e inovação.",
            "Seu logotipo é uma maçã com uma mordida.",
            "Conhecida por celulares, computadores e tablets de alto padrão.",
            "Possui um sistema operacional próprio e exclusivo.",
        ],
    },
    "Super-Heróis": {
        "Homem-Aranha": [
            "Herói que ganhou habilidades após a picada de um aracnídeo.",
            "Conhecido por lançar teias e escalar edifícios altos.",
            "Usa um traje nas cores vermelha e azul.",
            "Possui a famosa frase sobre grandes poderes e responsabilidades.",
        ],
        "Batman": [
            "Defensor de Gotham City que não possui superpoderes sobre-humanos.",
            "Utiliza tecnologia avançada, inteligência e artes marciais.",
            "Sua identidade secreta é um empresário milionário.",
            "Seu símbolo e traje são inspirados em um morcego.",
        ],
    },
    "Videojogos": {
        "Minecraft": [
            "Jogo focado na exploração e na construção com blocos.",
            "Possui modos como sobrevivência e criativo.",
            "Um dos seus personagens mais conhecidos é o Steve.",
            "Famoso pelo seu estilo visual pixelado e quadrado.",
        ],
        "Mario": [
            "Famoso personagem de jogos de plataforma da Nintendo.",
            "É um encanador que usa chapéu e macacão.",
            "Frequenta o Reino dos Cogumelos para salvar a Princesa Peach.",
            "Ganha poderes ao pegar cogumelos e flores de fogo.",
        ],
    },
    "Clima & Natureza": {
        "Chuva": [
            "Fenômeno meteorológico de precipitação de água do céu.",
            "Essencial para abastecer rios e a agricultura.",
            "As pessoas costumam usar guarda-chuva para se proteger.",
            "Geralmente associada a nuvens carregadas e trovões.",
        ],
        "Vulcão": [
            "Estrutura geológica que conecta o interior da Terra à superfície.",
            "Pode entrar em erupção e expelir magma e cinzas.",
            "Geralmente possui formato de montanha com uma cratera no topo.",
            "A rocha derretida expelida por ele é chamada de lava.",
        ],
    },
}

# Inicialização dos estados na sessão do Streamlit
if "estado" not in st.session_state:
    st.session_state.estado = "CONFIGURACAO"
if "num_jogadores" not in st.session_state:
    st.session_state.num_jogadores = 5
if "num_impostores" not in st.session_state:
    st.session_state.num_impostores = 1
if "categoria_selecionada" not in st.session_state:
    st.session_state.categoria_selecionada = "Comidas"
if "palavra_secreta" not in st.session_state:
    st.session_state.palavra_secreta = ""
if "impostores_ids" not in st.session_state:
    st.session_state.impostores_ids = []
if "dicas_impostores" not in st.session_state:
    st.session_state.dicas_impostores = {}
if "jogador_atual" not in st.session_state:
    st.session_state.jogador_atual = 1
if "revelado" not in st.session_state:
    st.session_state.revelado = False

# ---------------------------------------------------------
# TELA 1: CONFIGURAÇÃO DO JOGO
# ---------------------------------------------------------
if st.session_state.estado == "CONFIGURACAO":
    st.header(" Configurações da Partida")

    num_jogadores = st.number_input(
        "Quantidade de Jogadores:",
        min_value=3,
        max_value=20,
        value=st.session_state.num_jogadores,
        step=1,
    )

    max_imp = max(1, int(num_jogadores // 2))
    num_impostores = st.number_input(
        "Quantidade de Impostores:",
        min_value=1,
        max_value=max_imp,
        value=min(st.session_state.num_impostores, max_imp),
        step=1,
    )

    lista_categorias = list(CATEGORIAS.keys())

    col1, col2 = st.columns([3, 1])
    with col1:
        idx_atual = (
            lista_categorias.index(st.session_state.categoria_selecionada)
            if st.session_state.categoria_selecionada in lista_categorias
            else 0
        )
        categoria_escolhida = st.selectbox(
            "Escolha a Categoria:", lista_categorias, index=idx_atual
        )
        st.session_state.categoria_selecionada = categoria_escolhida

    with col2:
        st.write("")
        st.write("")
        if st.button("🎲 Sortear", use_container_width=True):
            st.session_state.categoria_selecionada = random.choice(
                lista_categorias
            )
            st.rerun()

    st.markdown("---")

    if st.button("🚀 Iniciar Jogo", use_container_width=True):
        st.session_state.num_jogadores = int(num_jogadores)
        st.session_state.num_impostores = int(num_impostores)

        cat = st.session_state.categoria_selecionada
        palavra = random.choice(list(CATEGORIAS[cat].keys()))
        st.session_state.palavra_secreta = palavra

        # Sorteia os impostores
        todos_jogadores = list(range(1, st.session_state.num_jogadores + 1))
        impostores = random.sample(
            todos_jogadores, st.session_state.num_impostores
        )
        st.session_state.impostores_ids = impostores

        # Sorteia dicas DIFERENTES para cada impostor
        dicas_disponiveis = CATEGORIAS[cat][palavra].copy()
        random.shuffle(dicas_disponiveis)

        st.session_state.dicas_impostores = {}
        for idx, imp_id in enumerate(impostores):
            # Se houver mais impostores do que dicas, reutiliza com ciclo
            dica_atribuida = dicas_disponiveis[idx % len(dicas_disponiveis)]
            st.session_state.dicas_impostores[imp_id] = dica_atribuida

        st.session_state.jogador_atual = 1
        st.session_state.revelado = False
        st.session_state.estado = "DISTRIBUICAO"
        st.rerun()

# ---------------------------------------------------------
# TELA 2: REVELAÇÃO DOS PAPÉIS (PASSE O DISPOSITIVO)
# ---------------------------------------------------------
elif st.session_state.estado == "DISTRIBUICAO":
    atual = st.session_state.jogador_atual
    total = st.session_state.num_jogadores

    st.header(f"👤 Jogador {atual} de {total}")

    if not st.session_state.revelado:
        st.info("Passe o dispositivo para o jogador correspondente.")
        if st.button(
            f"👁️ Ver Meu Papel (Jogador {atual})", use_container_width=True
        ):
            st.session_state.revelado = True
            st.rerun()
    else:
        # Se for um dos impostores
        if atual in st.session_state.impostores_ids:
            st.error("🚨 **VOCÊ É UM IMPOSTOR!** 🚨")

            # Exibe a dica exclusiva do impostor
            dica = st.session_state.dicas_impostores.get(
                atual, "Pense em algo relacionado à categoria."
            )
            st.warning(f"💡 **Sua dica secreta:** *{dica}*")

            st.write(
                "Use essa dica com cuidado para dar uma pista sutil sem revelar que não sabe a palavra exata!"
            )

            if st.session_state.num_impostores > 1:
                outros = [
                    f"Jogador {i}"
                    for i in st.session_state.impostores_ids
                    if i != atual
                ]
                st.write(
                    f"🤝 **Seu(s) parceiro(s) impostor(es):** {', '.join(outros)}"
                )

        # Se for inocente
        else:
            st.success(
                f"🔑 A palavra secreta é: **{st.session_state.palavra_secreta}**"
            )
            st.write("Sua missão: Dê uma pista sutil sobre a palavra!")

        st.markdown("---")

        if atual < total:
            if st.button("✅ Ok, Próximo Jogador", use_container_width=True):
                st.session_state.jogador_atual += 1
                st.session_state.revelado = False
                st.rerun()
        else:
            if st.button("🔥 Começar a Partida!", use_container_width=True):
                st.session_state.estado = "EM_JOGO"
                st.rerun()

# ---------------------------------------------------------
# TELA 3: REGRAS E DEBATE
# ---------------------------------------------------------
elif st.session_state.estado == "EM_JOGO":
    st.header("🎮 Partida em Andamento!")

    st.subheader("📌 Regras da Rodada")
    st.markdown(f"""
    * **Categoria da partida:** {st.session_state.categoria_selecionada}
    * **Quantidade de Impostores:** {st.session_state.num_impostores}
    1. **Rodada de Pistas:** Cada jogador diz **uma única palavra/frase** relacionada à palavra secreta.
    2. **Discussão:** Debatam quem deu as pistas mais suspeitas.
    3. **Votação:** Ao sinal de todos, apontem para quem acham ser impostor!
    """)

    st.markdown("---")

    if st.button("🔍 Revelar Impostores e Palavra", use_container_width=True):
        st.session_state.estado = "FIM"
        st.rerun()

# ---------------------------------------------------------
# TELA 4: RESULTADO FINAL
# ---------------------------------------------------------
elif st.session_state.estado == "FIM":
    st.header("🏆 Fim da Partida!")

    impostores_str = ", ".join(
        [f"Jogador {i}" for i in sorted(st.session_state.impostores_ids)]
    )
    st.error(f"🤫 O(s) Impostor(es) era(m): **{impostores_str}**")
    st.success(
        f"🔑 A palavra secreta era: **{st.session_state.palavra_secreta}**"
    )

    st.markdown("---")

    if st.button("🔄 Jogar Novamente", use_container_width=True):
        st.session_state.estado = "CONFIGURACAO"
        st.rerun()