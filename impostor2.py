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
            "Hambúrguer": [
            "Lanche composto por disco de carne moída servido dentro do pão.",
            "Normalmente acompanhado por queijo, alface, tomate e molhos.",
            "Um dos pratos mais populares em redes de fast-food.",
            "Pode ser preparado na chapa, grelha ou churrasqueira.",
        ],
        "Pizza": [
            "Massa redonda assada no forno com molho de tomate e coberturas variadas.",
            "Servida tradicionalmente em fatias triangulares.",
            "Sabores famosos incluem muçarela, calabreza e frango com catupiry.",
            "Prato de origem italiana amado mundialmente.",
        ],
        "Cachorro-quente": [
            "Lanche feito com salsicha servida no pão de formato alongado.",
            "Pode levar molho de tomate, milho, batata palha e maionese.",
            "Muito popular em bancas de rua e festas infantis.",
            "Em algumas regiões do Brasil, leva purê de batata.",
        ],
        "Batata frita": [
            "Porção de batatas cortadas em palitos e fritas em óleo quente.",
            "Crocante por fora e macia por dentro, servida com sal.",
            "Acompanhamento clássico para hambúrgueres e pratos rápidos.",
            "Costuma ser consumida com ketchup e maionese.",
        ],
        "X-Bacon": [
            "Sanduíche que combina hambúrguer, queijo derretido e tiras de bacon crocante.",
            "Conhecido pelo sabor defumado marcante do bacon.",
            "Um dos sanduíches mais pedidos em lanchonetes.",
            "Servido em pão de hambúrguer macio.",
        ],
        "Nuggets": [
            "Pequenos empanados de carne de frango fritos ou assados.",
            "Possuem casca crocante e formato prático para petiscar.",
            "Muito comuns em menus infantis de redes de fast-food.",
            "Acompanham bem molhos como barbecue e mostarda e mel.",
        ],
        "Pastel": [
            "Massa fina frita em óleo bem quente que cria bolhas crocantes.",
            "Recheado com opções salgadas como carne, queijo ou pizza.",
            "Tradição nas feiras livres brasileiras acompanhado de caldo de cana.",
            "Pode ser encontrado em formatos retangulares ou meia-lua.",
        ],
        "Coxinha": [
            "Salgado frito feito com massa de batata ou farinha de trigo.",
            "Formatada no formato tradicional de uma coxa de galinha.",
            "Recheada com frango desfiado temperado e catupiry.",
            "Presença obrigatória em festas de aniversário brasileiras.",
        ],
        "Esfiha": [
            "Salgado de origem árabe assado no forno.",
            "Pode ser aberta ou fechada com recheio de carne, queijo ou zátar.",
            "Acompanhada frequentemente por gotas de limão fresco.",
            "Muito popular em lanchonetes e restaurantes de comida árabe.",
        ],
        "Sanduíche": [
            "Alimento preparado com recheios entre duas fatias de pão.",
            "Opção prática para refeições rápidas e lanches da tarde.",
            "Pode ser recheado com presunto, queijo, saladas e vegetais.",
            "Servido frio ou quente na chapa.",
        ],
        "Hot dog": [
            "Denominação em inglês para o tradicional cachorro-quente.",
            "Composto por pão macio e salsicha quente.",
            "Geralmente temperado com mostarda, ketchup e molho relish.",
            "Lanche icônico dos estádios de basquete e beisebol nos EUA.",
        ],
        "Tacos": [
            "Prato tradicional da culinária mexicana dobrado ao meio.",
            "Feito com tortilha de milho ou trigo recheada com carne e pimenta.",
            "Acompanhado por guacamoles, sour cream e salsa picante.",
            "Come-se diretamente com as mãos de forma prática.",
        ],
        "Burrito": [
            "Especialidade mexicana composta por uma grande tortilha de trigo enrolada.",
            "Recheado com carne moída, feijão, arroz, queijo e pimentas.",
            "Fechado em formato de cilindro para segurar o recheio sem vazar.",
            "Prato substancioso e muito popular na comida Tex-Mex.",
        ],
        "Panqueca": [
            "Massa fina discoidal preparada na frigideira a partir de ovos, leite e farinha.",
            "Pode ser recheada com carne moída salgada e coberta com molho de tomate.",
            "Na versão americana, é servida no café da manhã com mel ou melado.",
            "Versátil para receitas salgadas ou doces.",
        ],
        "Lasanha": [
            "Massa em camadas intercaladas com molhos, queijo e carnes.",
            "Assada no forno até derreter o queijo e gratinar no topo.",
            "Sabores clássicos incluem bolonhesa e quatro queijos.",
            "Prato de domingo tradicional em muitas famílias.",
        ],
        "Feijoada": [
            "Prato típico brasileiro feito com feijão preto e carnes de porco.",
            "Cozinhado lentamente em panela funda com temperos marcantes.",
            "Servido com acompanhamentos como farofa, couve refogada e laranja.",
            "Considerado um dos pratos nacionais mais icônicos do Brasil.",
        ],
        "Churrasco": [
            "Preparo de cortes de carne grelhados sobre o brasa de carvão ou lenha.",
            "Servido com sal grosso, farofa, vinagrete e pão de alho.",
            "Tradição forte no sul do Brasil e encontros de fim de semana.",
            "Assado em espetos ou grelhas apropriadas.",
        ],
        "Pão de queijo": [
            "Iguaria mineira assada no forno feita com polvilho e queijo.",
            "Crocante por fora e macio e elástico por dentro.",
            "Acompanhamento perfeito para o café passado quentinho.",
            "Não contém glúten por ser feito com base de polvilho.",
        ],
        "Brigadeiro": [
            "Docinho tradicional brasileiro feito com leite condensado, cacau e manteiga.",
            "Cozinhado na panela, enrolado em bolinhas e coberto com granulado.",
            "Item indispensável em festas de aniversário no Brasil.",
            "Também consumido quente direto da panela com colher.",
        ],
        "Moqueca": [
            "Cozido de peixe e frutos do mar com pimentões, tomate e coentro.",
            "Preparado e servido tradicionalmente em panela de barro quente.",
            "Possui variações famosas como a baiana (com azeite de dendê) e a capixaba.",
            "Acompanhado de pirão e arroz branco.",
        ],
        "Acarajé": [
            "Bolinho frito no azeite de dendê feito de massa de feijão-fradinho.",
            "Comida tradicional da culinária baiana vendida por baianas de fita.",
            "Recheado com vatapá, caruru, camarão seco e pimenta.",
            "Patrimônio cultural imaterial do Brasil.",
        ],
        "Baião de dois": [
            "Prato típico do nordeste que mistura arroz e feijão cozinhados juntos.",
            "Enriquecido com queijo coalho, carne de sol e coentro.",
            "Muito saboroso e tradicional no sertão nordestino.",
            "Prato forte e substancioso da culinária regional.",
        ],
        "Escondidinho": [
            "Prato assado no forno composto por camada de purê cobrindo um recheio salgado.",
            "Feito tradicionalmente com purê de mandioca e carne de sol desfiada.",
            "Gratinado no topo com queijo derretido.",
            "O recheio fica 'escondido' sob a camada de purê superior.",
        ],
        "Farofa": [
            "Acompanhamento crocante feito de farinha de mandioca ou milho tostada.",
            "Misturada na manteiga com bacon, ovos, cebola e temperos.",
            "Complemento perfeito para feijoada, churrasco e pratos do dia a dia.",
            "Prato essencial na mesa dos brasileiros.",
        ],
        "Vatapá": [
            "Creme denso da culinária baiana feito com pão, camarão, amendoim e dendê.",
            "Temperado com leite de coco, azeite de dendê e pimenta.",
            "Servido como recheio principal do acarajé ou acompanhamento.",
            "Possui textura cremosa e sabor rico e marcante.",
        ],
        "Pamonha": [
            "Comida tradicional feita de massa de milho verde cozida.",
            "Embrulhada e cozida dentro da própria palha do milho.",
            "Pode ser servida na versão doce ou salgada com queijo.",
            "Muito consumida nas festas juninas do Brasil.",
        ],
        "Tapioca": [
            "Iguaria de origem indígena feita com fécula de mandioca aquecida na frigideira.",
            "A massa junta-se com o calor formando uma casquinha flexível.",
            "Recheada com opções doces ou salgadas como queijo e coco.",
            "Opção saudável sem glúten para o café da manhã.",
        ],
        "Galinhada": [
            "Prato caipira saboroso de arroz cozinhado junto com pedaços de frango.",
            "Temperado com açafrão, dando uma cor amarelada característica.",
            "Muito popular nos estados de Goiás e Minas Gerais.",
            "Cozinhado em uma única panela grande com temperos frescos.",
        ],
        "Arroz carreteiro": [
            "Prato tradicional gaúcho feito de arroz misturado com carne de sol ou charque.",
            "Criado historicamente por transportadores de carga que viajavam pelo sul.",
            "Cozinhado com cebola, alho, cheiro-verde e carnes picadas.",
            "Refeição completa e cheia de sustância.",
        ],
        "Macarrão": [
            "Massa alimentícia seca ou fresca cozida em água fervente.",
            "Servida com molhos variados como bolonhesa, branco ou pesto.",
            "Encontrada em formatos como parafuso, pena e gravatinha.",
            "Base da culinária italiana presente nas refeições diárias.",
        ],
        "Espaguete": [
            "Tipo de macarrão em formato de fios longos e finos.",
            "Consumido enrolando os fios no garfo durante a refeição.",
            "Combina perfeitamente com molho de tomate e almôndegas.",
            "Uma das massas mais famosas do planeta.",
        ],
        "Nhoque": [
            "Massa macia em formato de pequenas esferas feitas de batata e farinha.",
            "Cozinhado em água quente até boiar na superfície.",
            "Servido com molho de tomate gratinado no forno.",
            "Tradicionalmente consumido no dia 29 para atrair sorte.",
        ],
        "Ravioli": [
            "Massa recheada dobrada em pequenos quadrados com bordas denteadas.",
            "Pode conter recheios de carne, queijo ricota ou espinafre.",
            "Cozido em água e servido com molho quente por cima.",
            "Especialidade da massaria clássica italiana.",
        ],
        "Risoto": [
            "Prato italiano cremoso à base de arroz arbóreo cozido lentamente.",
            "Preparado adicionando caldo quente aos poucos e manteiga no final.",
            "Pode levar ingredientes como cogumelos, queijo parmesão e frutos do mar.",
            "Servido bem quente e com textura aveludada.",
        ],
        "Strogonoff": [
            "Prato de tiras de carne ou frango em molho cremoso de creme de leite e ketchup.",
            "Geralmente leva cogumelos fatiados no preparo.",
            "Servido acompanhado de arroz branco e batata palha crocante.",
            "Receita de origem russa muito popular no Brasil.",
        ],
        "Purê de batata": [
            "Acompanhamento cremoso feito de batatas cozidas e espremidas.",
            "Misturado com leite, manteiga e sal até ficar homogêneo.",
            "Combina muito bem com carnes, assados e molhos.",
            "Textura macia que agrada crianças e adultos.",
        ],
        "Sopa": [
            "Prato líquido e quente preparado pelo cozimento de legumes e carnes.",
            "Muito consumida em dias frios para aquecer o corpo.",
            "Pode ser batida como creme ou ter pedaços inteiros.",
            "Acompanhada frequentemente por torradas e pão.",
        ],
        "Yakisoba": [
            "Prato de origem asiática composto por macarrão frito com legumes e carnes.",
            "Temperado com molho Shoyu denso e óleo de gergelim.",
            "Contém vegetais crocantes como acelga, brócolis e cenoura.",
            "Muito pedido em restaurantes de comida chinesa e japonesa.",
        ],
        "Maçã": [
            "Fruta arredondada de casca vermelha ou verde e polpa crocante.",
            "Contém sementes no centro e sabor suavemente doce ou azedinho.",
            "Muito conhecida pelo ditado popular sobre manter a saúde em dia.",
            "Consumida in natura, em tortas ou sucos.",
        ],
        "Banana": [
            "Fruta de formato curvo e casca amarela fácil de descascar.",
            "Rica em potássio e ótima fonte de energia para praticantes de esportes.",
            "Polpa macia e doce, consumida in natura ou com aveia.",
            "Uma das frutas mais consumidas do mundo.",
        ],
        "Morango": [
            "Fruta pequena e vermelha em formato de coração com pontinhos pretos.",
            "Sabor suavemente ácido e aroma característico marcante.",
            "Muito utilizada em sobremesas, bolos e coberturas de chocolate.",
            "Possui pequenas folhas verdes no topo.",
        ],
        "Uva": [
            "Pequena fruta arredondada que cresce em cachos nas videiras.",
            "Encontrada nas cores verde, roxa ou preta, com ou sem sementes.",
            "Matéria-prima principal para a fabricação de sucos e vinhos.",
            "Pode ser consumida fresca ou como uva-passa.",
        ],
        "Melancia": [
            "Fruta grande e pesada de casca verde e interior vermelho suculento.",
            "Contém alta quantidade de água, sendo muito refrescante no verão.",
            "Possui sementes pretas espalhadas pela polpa doce.",
            "Servida comumente em fatias grandes triangulares.",
        ],
        "Abacaxi": [
            "Fruta tropical de casca áspera com espinhos e coroa de folhas no topo.",
            "Polpa amarela sumarenta com sabor ácido e doce.",
            "Muito utilizado em sucos, sobremesas e pratos assados.",
            "Contém enzimas que ajudam na digestão de carnes.",
        ],
        "Manga": [
            "Fruta tropical de polpa suculenta amarela e caroço grande no centro.",
            "Possui casca com tons de verde, amarelo e vermelho.",
            "Muito doce e aromática, consumida fresca ou em sucos.",
            "Variedades famosas incluem a manga Rosa, Palmer e Tommy.",
        ],
        "Laranja": [
            "Fruta cítrica arredondada de casca laranja rica em Vitamina C.",
            "Dividida internamente em gomos suculentos.",
            "Muito utilizada para fazer suco natural espremido na hora.",
            "Ajuda no fortalecimento do sistema imunológico.",
        ],
        "Mamão": [
            "Fruta macia de formato oval com casca alaranjada e sementes pretas no centro.",
            "Muito consumida no café da manhã para auxiliar a digestão.",
            "Possui sabor doce e suave, consumida com colher.",
            "Variedades populares incluem mamão Papaia e Formosa.",
        ],
        "Kiwi": [
            "Fruta pequena de casca marrom peluda e interior verde brilhante.",
            "Polpa cheia de pequenas sementes pretas comestíveis no centro.",
            "Sabor cítrico, refrescante e levemente azedo.",
            "Rico em vitamina C e antioxidantes.",
        ],
        "Pera": [
            "Fruta de formato afunilado no topo e base mais larga.",
            "Polpa suculenta, doce e de textura suave ao morder.",
            "Casca fina que varia entre tons de verde, amarelo e vermelho.",
            "Ótima para consumo in natura ou cozida em caldas.",
        ],
        "Limão": [
            "Fruta cítrica de casca verde ou amarela e sabor bastante azedo.",
            "Utilizado como tempero para saladas, carnes e peixes.",
            "Base para a preparação de limonadas e caipirinhas.",
            "Rico em ácido cítrico e vitamina C.",
        ],
        "Goiaba": [
            "Fruta tropical de casca verde e polpa interna vermelha ou branca.",
            "Cheia de pequenas sementes duras no centro.",
            "Matéria-prima para o famoso doce goiabada.",
            "Muito aromática e rica em fibras e nutrientes.",
        ],
        "Maracujá": [
            "Fruta de casca amarela e polpa ácida cheia de sementes pretas.",
            "Famosa por suas propriedades calmantes e relaxantes.",
            "Muito utilizada na preparação de sucos, mousses e caldas.",
            "Possui aroma intenso e marcante.",
        ],
        "Cereja": [
            "Fruta pequena, redonda e de cor vermelha intensa presa a um cabinho.",
            "Sabor doce e delicado, muito usada para decorar bolos e tortas.",
            "Frequente em sobremesas finas e caldas doces.",
            "Possui um pequeno caroço duro no centro.",
        ],
        "Beijinho": [
            "Docinho tradicional de festa feito com leite condensado e coco ralado.",
            "Enrolado em bolinhas e passado no coco ralado fino.",
            "Geralmente decorado com um cravo-da-índia no topo.",
            "O par perfeito do brigadeiro nas mesas de aniversário.",
        ],
        "Bolo de chocolate": [
            "Massa assada macia de cacau com cobertura de brigadeiro ou calda.",
            "Sobremesa clássica para lanches e festas.",
            "Servido frequentemente acompanhado de um copo de leite ou café.",
            "Pode ser recheado ou ter cobertura vulcão.",
        ],
        "Pudim": [
            "Sobremesa cremosa assada em banho-maria com calda de caramelo por cima.",
            "Feito à base de leite condensado, leite e ovos.",
            "Desenformado em prato fundo revelando a calda dourada líquido.",
            "Possui textura lisa e derrete na boca.",
        ],
        "Sorvete": [
            "Sobremesa congelada cremosa servida em casquinhas ou potes.",
            "Encontrado em dezenas de sabores como chocolate, baunilha e morango.",
            "Ideal para se refrescar em dias quentes de verão.",
            "Pode levar coberturas de caldas doces e confeitos.",
        ],
        "Açaí": [
            "Creme roxo gelado feito da fruta típica da Amazônia.",
            "Servido na tigela ou copo com acompanhamentos como banana, granola e leite em pó.",
            "Fonte de energia muito popular entre jovens e praticantes de esportes.",
            "Sabor único e marcante.",
        ],
        "Brownie": [
            "Bolo denso e compacto de chocolate de origem americana.",
            "Possui casquinha crocante por fora e interior macio e úmido.",
            "Geralmente servido quente acompanhado de uma bola de sorvete de baunilha.",
            "Pode conter pedaços de nozes ou castanhas.",
        ],
        "Cheesecake": [
            "Torta doce americana com base de biscoito e recheio cremoso de cream cheese.",
            "Assada no forno e coberta com calda de frutas vermelhas ou morango.",
            "Mistura o sabor suavemente salgado do queijo com a calda doce.",
            "Sobremesa sofisticada servida gelada.",
        ],
        "Mousse": [
            "Sobremesa gelada de textura leve, aerada e cheia de bolinhas.",
            "Sabores mais tradicionais incluem maracujá, limão e chocolate.",
            "Preparada com claras em neve ou creme de leite batido.",
            "Servida em taças individuais bem gelada.",
        ],
        "Donuts": [
            "Rosquinha frita tradicional americana com furo no meio.",
            "Coberta com glacê colorido, chocolate e confeitos divertidos.",
            "Massa macia e adocicada perfeita para lanches.",
            "Muito associada à cultura pop e desenhos animados.",
        ],
        "Churros": [
            "Massa frita em formato cilíndrico e estriado polvilhada com açúcar e canela.",
            "Recheado por dentro com bastante doce de leite ou chocolate.",
            "Crocante por fora e macio por dentro.",
            "Vendido em carrinhos de rua e lanchonetes.",
        ],
        "Paçoca": [
            "Doce tradicional brasileiro feito de amendoim moído, farinha de mandioca e açúcar.",
            "Possui textura esfarelenta que esmaga na boca.",
            "Muito consumida durante as festividades juninas.",
            "Embalada tradicionalmente em formato de rolha ou quadrado.",
        ],
        "Cocada": [
            "Doce feito de coco ralado cozinhado com açúcar ou leite condensado.",
            "Pode ser encontrada nas versões branca, queimada ou com maracujá.",
            "Textura que varia entre o cremosa e o firme e crocante.",
            "Doce tradicional das praias e feiras do Brasil.",
        ],
        "Gelatina": [
            "Sobremesa leve, colorida e consistente preparada com água quente e fria.",
            "Servida bem gelada com textura firme que balança.",
            "Encontrada em sabores de frutas como morango, uva e limão.",
            "Opção de sobremesa leve e fácil de digerir.",
        ],
        "Torta de limão": [
            "Torta com base crocante de biscoito e recheio cremoso de limão.",
            "Coberta com merengue tostado ou raspas de limão por cima.",
            "Equilibra perfeitamente o sabor doce com a acidez do limão.",
            "Servida bem gelada em fatias.",
        ],
        "Água": [
            "Líquido incolor e inodoro fundamental para a sobrevivência humana.",
            "Essencial para manter o corpo hidratado ao longo do dia.",
            "Consumida natural, gelada ou com gás.",
            "Substância mais abundante do planeta Terra.",
        ],
        "Água de coco": [
            "Bebida natural isotônica extraída diretamente do interior do coco verde.",
            "Muito refrescante e rica em sais minerais e potássio.",
            "Consumida na praia diretamente no coco com canudo.",
            "Excelente para reidratação em dias quentes.",
        ],
        "Refrigerante": [
            "Bebida industrializada gaseificada e adocicada.",
            "Encontrado em sabores como cola, guaraná, laranja e limão.",
            "Servido bem gelado, frequentemente acompanhando fast-food.",
            "Possui versões normais, zero e sem açúcar.",
        ],
        "Suco de laranja": [
            "Bebida natural preparada pela espremidura de laranjas frescas.",
            "Rico em vitamina C e muito consumido no café da manhã.",
            "Pode ser servido coado ou com gomos da fruta.",
            "Bebida clássica para acompanhar refeições diárias.",
        ],
        "Suco de uva": [
            "Bebida roxa e doce preparada a partir do prensado de uvas.",
            "Rico em antioxidantes benéficos para a saúde do coração.",
            "Encontrado nas versões integral, concentrado ou néctar.",
            "Sabor encorpado e frutado.",
        ],
        "Limonada": [
            "Bebida refrescante feita com suco de limão, água e açúcar.",
            "Perfeita para combater o calor em dias ensolarados.",
            "Pode ser preparada na versão Suíça (batida com casca e leite condensado).",
            "Servida com bastante gelo e rodelas de limão.",
        ],
        "Café": [
            "Bebida quente e estimulante preparada com grãos de café torrados e moídos.",
            "Contém cafeína que ajuda a manter a atenção e energia.",
            "Consumido puro (pretinho) ou com leite no café da manhã.",
            "Uma das bebidas mais consumidas no cotidiano brasileiro.",
        ],
        "Chá": [
            "Bebida preparada pela infusão de ervas, folhas ou flores em água quente.",
            "Opções populares incluem camomila, hortelã e chá verde.",
            "Consumido para relaxar, aquecer ou para fins medicinais.",
            "Tradição milenar em diversas culturas do mundo.",
        ],
        "Leite": [
            "Líquido nutritivo branco produzido por mamíferos.",
            "Fonte rica de cálcio importante para o fortalecimento dos ossos.",
            "Consumido puro, com achocolatado ou no preparo de receitas.",
            "Base para produtos como queijos, iogurtes e manteiga.",
        ],
        "Achocolatado": [
            "Mistura de leite quente ou gelado com pó de chocolate ou cacau.",
            "Bebida doce muito popular entre crianças no café da manhã.",
            "Pode ser preparado em casa ou comprado pronto em caixinha.",
            "Marcas famosas incluem Nescau e Toddy.",
        ],
        "Vitamina de banana": [
            "Bebida cremosa batida no liquidificador com leite, banana e aveia.",
            "Muito nutritiva e consumida como lanche rápido ou pré-treino.",
            "Fornece energia e saciedade de forma saudável.",
            "Pode ser adoçada com mel ou açúcar.",
        ],
        "Milk-shake": [
            "Bebida gelada e densa batida com sorvete e leite.",
            "Servido em copo grande com chantilly e calda por cima.",
            "Sabores clássicos incluem chocolate, baunilha e morango.",
            "Acompanhamento famoso em lanchonetes e hamburguerias.",
        ],
        "Energético": [
            "Bebida gaseificada formulada para aumentar o alerta e energia física.",
            "Contém cafeína, taurina e vitaminas em sua composição.",
            "Muito consumida por estudantes, motoristas e em festas.",
            "Vendida em latas de alumínio características.",
        ],
        "Isotônico": [
            "Bebida desenvolvida para repor água e sais minerais perdidos no suor.",
            "Muito utilizada por atletas durante ou após treinos intensos.",
            "Previne desidratação e cãibras musculares.",
            "Vendida em cores chamativas e sabores de frutas.",
        ],
        "Chá gelado": [
            "Bebida refrescante à base de chá preto ou verde servida com gelo.",
            "Geralmente aromatizada com sabores de pêssego ou limão.",
            "Opção refrescante e saborosa para dias quentes.",
            "Consumida engarrafada ou preparada na hora.",
        ],
        "Cerveja": [
            "Bebida alcoólica fermentada produzida a partir de cevada, lúpulo e água.",
            "Servida estúpida de gelada em copos, garrafas ou latas.",
            "Acompanhamento tradicional para churrascos e encontros de amigos.",
            "Uma das bebidas alcoólicas mais antigas e consumidas do planeta.",
        ],
        "Vinho": [
            "Bebida alcoólica obtida pela fermentação do suco de uva.",
            "Encontrado nas variedades tinto, branco e rosê.",
            "Servido tradicionalmente em taças para harmonizar com jantares.",
            "Guardado e envelhecido em barris de carvalho.",
        ],
        "Champanhe": [
            "Vinho espumante e efervescente com bolhas finas de gás natural.",
            "Originário da região de Champagne, na França.",
            "Bebida associada a comemorações, festas de ano novo e brindes.",
            "Servido em taças altas e finas tipo flauta.",
        ],
        "Vodka": [
            "Bebida alcoólica destilada clara e transparente de alto teor de álcool.",
            "Originária da Rússia e Europa Oriental.",
            "Base principal para o preparo do drinque brasileiro caipiroska.",
            "Muito utilizada no preparo de coquetéis variados.",
        ],
        "Whisky": [
            "Bebida destilada envelhecida em barris de madeira de cor dourada.",
            "Possui aroma marcante, sabor amadeirado e alto teor alcoólico.",
            "Consumido puro, com gelo de água de coco ou energético.",
            "Tradicional de países como Escócia e Irlanda.",
        ],
        "Gin": [
            "Bebida destilada aromatizada com bagas de zimbro e botânicos.",
            "Base para o famoso e refrescante coquetel 'Gin Tônica'.",
            "Servido em taças grandes com bastante gelo e rodelas de frutas.",
            "Muito popular em bares e festas noturnas.",
        ],
        "Tequila": [
            "Bebida destilada tradicional do México extraída do agave-azul.",
            "Consumida tradicionalmente em shots rápidos com sal e limão.",
            "Possui sabor forte e marcante.",
            "Base para o famoso coquetel Margarita.",
        ],
        "Rum": [
            "Bebida alcoólica destilada obtida a partir da fermentação do melaço da cana.",
            "Famosa por sua associação histórica com marinheiros e piratas.",
            "Base essencial para coquetéis clássicos como Mojito e Piña Colada.",
            "Possui versões transparentes e envelhecidas de cor dourada.",
        ],
        "Licor": [
            "Bebida alcoólica doce e viscosa aromatizada com frutas, ervas ou creme.",
            "Consumida frequentemente em pequenos cálices após as refeições.",
            "Sabores famosos incluem chocolate, café, amêndoas e laranjas.",
            "Possui teor de açúcar elevado e textura aveludada.",
        ],
        "Cachaça": [
            "Aguardente brasileira obtida da fermentação e destilação do caldo de cana.",
            "Ingrediente alcoólico indispensável para a preparação da caipirinha.",
            "Pode ser consumida pura ou envelhecida em barris de madeira nobre.",
            "Símbolo cultural da produção de destilados no Brasil.",
        ],
    },
    "Objetos do Cotidiano": {
        "Sofá": [
            "Móvel estofado projetado para acomodar várias pessoas sentadas.",
            "Localizado geralmente na sala de estar para descanso e lazer.",
            "Pode ser encontrado em modelos de dois ou três lugares, ou retrátil.",
            "Geralmente posicionado em frente à televisão.",
        ],
        "Mesa": [
            "Móvel com tampo plano sustentado por pernas ou base.",
            "Utilizado para refeições, estudos ou reuniões em família.",
            "Geralmente acompanhado por cadeiras ao seu redor.",
            "Pode ser encontrado em materiais como madeira, vidro ou metal.",
        ],
        "Cadeira": [
            "Assento individual com encosto e quatro pernas ou base de apoio.",
            "Usado para sentar-se à mesa, na escrivaninha ou em escritórios.",
            "Encontrado em diversos estilos, desde madeira até plástico ou metal.",
            "Móvel essencial em qualquer ambiente residencial ou comercial.",
        ],
        "Cama": [
            "Móvel destinado ao repouso e ao sono durante a noite.",
            "Composto por estrutura de suporte, colchão, lençóis e travesseiros.",
            "Disponível em tamanhos como solteiro, casal, queen e king size.",
            "Essencial para garantir o descanso diário das pessoas.",
        ],
        "Guarda-roupa": [
            "Móvel de grande porte usado para organizar vestimentas e calçados.",
            "Possui portas que podem ser de abrir ou de correr.",
            "Contém prateleiras, gavetas e cabideiros em seu interior.",
            "Ajuda a manter o quarto limpo e organizado.",
        ],
        "Espelho": [
            "Superfície de vidro altamente polida que reflete imagens com clareza.",
            "Utilizado para checar a aparência e a vestimenta antes de sair.",
            "Pode ser encontrado pendurado na parede ou em móveis.",
            "Também serve para dar sensação de amplitude a ambientes pequenos.",
        ],
        "Abajur": [
            "Luminária de mesa ou de cabeceira com cúpula direcional.",
            "Emite uma luz suave e aconchegante para leitura noturna.",
            "Fica geralmente posicionado sobre criados-mudos na quarto.",
            "Funciona com interruptor próprio e lâmpada interna.",
        ],
        "Relógio": [
            "Instrumento utilizado para medir, registrar e indicar as horas.",
            "Pode ser encontrado em modelos de parede, de pulso ou digitais.",
            "Possui ponteiros (nos modelos analógicos) ou painel digital.",
            "Ajuda as pessoas a cumprirem horários e compromissos.",
        ],
        "Cortina": [
            "Peça de tecido pendurada em janelas para controlar a entrada de luz.",
            "Ajuda a dar privacidade ao interior da casa.",
            "Complementa a decoração visual e o design dos cômodos.",
            "Pode ser aberta ou fechada através de trilhos ou varões.",
        ],
        "Tapete": [
            "Peça têxtil colocada diretamente sobre o piso de ambientes internos.",
            "Proporciona conforto térmico e maciez ao caminhar descalço.",
            "Contribui bastante para a estética e decoração dos cômodos.",
            "Frequente na sala de estar, quartos ou embaixo de mesas.",
        ],
        "Geladeira": [
            "Eletrodoméstico essencial para conservar alimentos em baixa temperatura.",
            "Possui compartimento refrigerado e congelador (freezer).",
            "Evita que carnes, laticínios e vegetais estraguem rapidamente.",
            "Mantém bebidas e comidas frescas por mais tempo.",
        ],
        "Fogão": [
            "Eletrodoméstico ou aparelho a gás usado para cozinhar alimentos.",
            "Possui queimadores (bocas) na parte superior e forno embaixo.",
            "Indispensável na preparação de pratos quentes e assados.",
            "Acende chamas controladas por botões giratórios.",
        ],
        "Micro-ondas": [
            "Aparelho eletrônico que aquece e descongelar alimentos rapidamente.",
            "Utiliza ondas eletromagnéticas de alta frequência para cozinhar.",
            "Possui painel digital com timer e prato giratório interno.",
            "Muito utilizado pela praticidade no dia a dia corrido.",
        ],
        "Liquidificador": [
            "Eletrodoméstico com motor elétrico e lâminas giratórias no fundo.",
            "Utilizado para triturar, bater e misturar ingredientes líquidos ou pastosos.",
            "Ideal para o preparo de vitaminas, sucos e sopas cremosas.",
            "Possui copo de vidro ou acrílico com tampa.",
        ],
        "Panela": [
            "Utensílio de cozinha usado para cozinhar alimentos no fogo.",
            "Pode ser feita de alumínio, inox, ferro ou cerâmica.",
            "Possui cabo ou alças laterais e tampa correspondente.",
            "Utilizada para fazer arroz, feijão, sopas e refogados.",
        ],
        "Prato": [
            "Utensílio plano ou fundo onde se serve a comida nas refeições.",
            "Geralmente fabricado em cerâmica, vidro, porcelana ou plástico.",
            "Posicionado sobre a mesa durante café, almoço e jantar.",
            "Acomoda a porção individual de alimentos de cada pessoa.",
        ],
        "Copo": [
            "Recipiente cilíndrico aberto em cima para beber líquidos.",
            "Pode ser feito de vidro, plástico, metal ou acrílico.",
            "Utilizado para consumir água, sucos, refrigerantes e outras bebidas.",
            "Item indispensável em qualquer mesa ou cozinha.",
        ],
        "Garfo": [
            "Talher composto por um cabo e pequenos dentes na ponta.",
            "Utilizado para espetar e levar alimentos sólidos à boca.",
            "Geralmente usado em conjunto com a faca durante as refeições.",
            "Feito comumente de aço inoxidável ou plástico.",
        ],
        "Faca": [
            "Utensílio cortante formado por lâmina de metal e cabo.",
            "Utilizado para cortar carnes, legumes e alimentos no prato.",
            "Requer cuidado no manuseio devido ao fio cortante.",
            "Item fundamental no conjunto de talheres de mesa.",
        ],
        "Colher": [
            "Talher com uma pequena concha oval na ponta presa a um cabo.",
            "Utilizado para consumir alimentos líquidos, cremosos ou sopas.",
            "Também serve para misturar açúcar no café ou leite.",
            "Presente em todas as gavetas de talheres das cozinhas.",
        ],
        "Xícara": [
            "Pequeno recipiente com alça lateral projetado para bebidas quentes.",
            "Utilizado para servir café, chá ou chocolate quente.",
            "Geralmente vem acompanhado por um pequeno prato de apoio.",
            "Fabricado comumente em porcelana ou cerâmica.",
        ],
        "Chaleira": [
            "Utensílio com bico e tampa usado para ferver água.",
            "Pode ser aquecida diretamente no fogão ou ser elétrica.",
            "Emite um som de apito tradicional quando a água atinge fervura.",
            "Muito usada no preparo de chás e café passado.",
        ],
        "Torradeira": [
            "Eletrodoméstico de cozinha projetado para dourar fatias de pão.",
            "Possui aberturas onde os pães são inseridos na vertical.",
            "Conta com timer para controlar o nível de tostagem.",
            "Ideal para preparar o café da manhã rapidamente.",
        ],
        "Air fryer": [
            "Fritadeira elétrica que cozinha alimentos usando circulação de ar quente.",
            "Permite preparar frituras crocantes utilizando pouco ou nenhum óleo.",
            "Possui gaveta antiaderente removível com cesto.",
            "Um dos eletrodomésticos mais populares na culinária moderna.",
        ],
        "Peneira": [
            "Utensílio em formato de rede fina com aro e cabo.",
            "Usado para coar líquidos ou peneirar farinha e açúcar.",
            "Separa grumos e impurezas dos ingredientes secos.",
            "Encontrado em diferentes tamanhos na cozinha.",
        ],
    },
    "Tecnologia & Eletrônicos": {
        "Celular": [
            "Dispositivo móvel inteligente com tela sensível ao toque.",
            "Permite ligações, mensagens, acesso à internet e redes sociais.",
            "Carrega câmeras embutidas de alta resolução e aplicativos variados.",
            "Objeto indispensável que acompanha as pessoas o dia todo.",
        ],
        "Computador": [
            "Máquina eletrônica programável para processamento de dados.",
            "Composto por gabinete, monitor, teclado e mouse.",
            "Utilizado para trabalhos pesados, estudos, jogos e edições.",
            "Capaz de armazenar grandes volumes de arquivos.",
        ],
        "Notebook": [
            "Computador portátil compacto que integra tela, teclado e bateria.",
            "Fácil de transportar em mochilas para o trabalho ou faculdade.",
            "Funciona sem estar conectado permanentemente à tomada.",
            "Possui touchpad integrado no lugar do mouse.",
        ],
        "Tablet": [
            "Dispositivo portátil em formato de prancheta digital com tela sensível ao toque.",
            "Posicionado em tamanho entre o celular e o notebook.",
            "Usado para leitura, desenho digital, vídeos e navegação.",
            "Pode ser operado com os dedos ou caneta stylus.",
        ],
        "Televisão": [
            "Aparelho eletrônico para transmissão de imagens e sons à distância.",
            "Atualmente conectado à internet, transformando-se em Smart TV.",
            "Centraliza o entretenimento da sala com filmes e séries.",
            "Possui telas grandes de tecnologia LED, OLED ou QLED.",
        ],
        "Fone de ouvido": [
            "Dispositivo de áudio encaixado nos ouvidos ou sobre a cabeça.",
            "Permite escutar músicas, podcasts e chamadas de forma individual.",
            "Pode ser encontrado em modelos com fio ou sem fio (Bluetooth).",
            "Ajuda a isolar barulhos externos do ambiente.",
        ],
        "Carregador": [
            "Acessório eletrônico usado para repor a bateria de dispositivos.",
            "Conecta a tomada da parede ao aparelho via cabo USB.",
            "Indispensável para manter celulares e notebooks funcionando.",
            "Possui adaptadores específicos para cada tipo de entrada.",
        ],
        "Teclado": [
            "Periférico de computador composto por dezenas de teclas com letras e números.",
            "Utilizado para digitar textos, comandos e jogar.",
            "Pode se conectar via cabo USB ou sem fio por receptor/Bluetooth.",
            "Possui padrão de disposição de letras conhecido como QWERTY.",
        ],
        "Mouse": [
            "Dispositivo apontador que controla o cursor na tela do computador.",
            "Possui botões de clique esquerdo/direito e roda de rolagem.",
            "Movimentado com a mão sobre uma superfície plana ou mousepad.",
            "Essencial para navegação rápida em sistemas operacionais.",
        ],
        "Controle remoto": [
            "Aparelho portátil sem fio para comandar eletrônicos à distância.",
            "Utilizado principalmente para mudar canais ou volume da televisão.",
            "Funciona através de sinais infravermelhos ou conexão Bluetooth.",
            "Alimentado por pequenas pilhas em seu compartimento traseiro.",
        ],
        "Câmera": [
            "Dispositivo óptico usado para capturar fotografias e gravar vídeos.",
            "Pode ser encontrada em modelos profissionais DSLR ou compactos.",
            "Possui lentes ajustáveis para foco e entrada de luz.",
            "Registra momentos e memórias visuais com alta definição.",
        ],
        "Impressora": [
            "Periférico que transfere documentos digitais para o papel impresso.",
            "Utiliza cartuchos de tinta ou toner a laser.",
            "Pode ter funções adicionais como scanner e copiadora.",
            "Muito útil em escritórios, escolas e residências.",
        ],
        "Smartwatch": [
            "Relógio de pulso inteligente conectado via Bluetooth ao celular.",
            "Monitora atividades físicas, frequência cardíaca e notificações.",
            "Possui tela sensível ao toque e mostradores personalizáveis.",
            "Funciona como extensão digital do smartphone no pulso.",
        ],
        "Roteador": [
            "Aparelho de rede que distribui o sinal de internet Wi-Fi na casa.",
            "Possui antenas transmissoras e portas de conexão para cabos.",
            "Garante que celulares e computadores acessem a rede sem fio.",
            "Ligado diretamente ao modem da operadora de telecomunicações.",
        ],
        "Caixa de som": [
            "Dispositivo de áudio amplificado para reproduzir músicas em volume alto.",
            "Pode se conectar a celulares e computadores via Bluetooth.",
            "Muitas versões são portáteis e à prova d'água para festas.",
            "Oferece graves potentes e som estéreo para ambientes.",
        ],
    },
    "Escola & Papelaria": {
        "Mochila": [
            "Bolsa de grandes dimensões usada nas costas com duas alças.",
            "Utilizada por estudantes para carregar livros, cadernos e materiais.",
            "Possui bolsos com zíper e compartimentos organizadores.",
            "Encontrada em vários estilos, cores e tamanhos.",
        ],
        "Caderno": [
            "Conjunto de folhas de papel encadernadas com capa protetora.",
            "Utilizado por estudantes para anotações de aulas e tarefas.",
            "Pode ter folhas pautadas, quadriculadas ou em branco.",
            "Essencial para a organização do ano letivo.",
        ],
        "Caneta": [
            "Instrumento de escrita preenchido com tinta líquida ou pastosa.",
            "A ponta possui uma esfera metálica que libera tinta ao deslizar.",
            "Encontrada comumente nas cores azul, preta e vermelha.",
            "Ferramenta padrão para assinaturas e provas escolares.",
        ],
        "Lápis": [
            "Instrumento de escrita composto por um bastão de grafite envolvido em madeira.",
            "Permite apagar traços facilmente com o auxílio de borracha.",
            "Muito utilizado em desenhos, esboços e rascunhos iniciais.",
            "Possui graduações variadas de maciez na ponta.",
        ],
        "Borracha": [
            "Objeto de borracha sintética usado para apagar marcas de lápis.",
            "Remove traços de grafite do papel através do atrito.",
            "Geralmente encontrada nas cores branca ou colorida.",
            "Item obrigatório no estojo de qualquer estudante.",
        ],
        "Régua": [
            "Instrumento de medida plano e graduado em centímetros e milímetros.",
            "Utilizado para traçar linhas retas perfeitas no papel.",
            "Pode ser fabricado em plástico transparente, metal ou madeira.",
            "Muito usado em aulas de matemática e geometria.",
        ],
        "Apontador": [
            "Pequeno utensílio equipado com lâmina interna para afiar lápis.",
            "Desgasta a madeira e o grafite para criar uma ponta fina.",
            "Pode possuir um pequeno depósito integrado para guardar resíduos.",
            "Fundamental para manter o lápis pronto para uso.",
        ],
        "Tesoura": [
            "Utensílio de corte composto por duas lâminas cruzadas com cabos.",
            "Utilizado em trabalhos manuais escolares para recortar papéis.",
            "Existem modelos com ponta arredondada voltados para crianças.",
            "Ferramenta útil em atividades de artesanato e colagem.",
        ],
        "Cola": [
            "Substância adesiva usada para unir folhas e materiais de papelaria.",
            "Pode ser encontrada em formato líquido, bastão ou supercola.",
            "Seca após alguns minutos, fixando firmemente os elementos.",
            "Item essencial em maquetes e trabalhos escolares.",
        ],
        "Estojo": [
            "Pequeno recipiente com zíper usado para guardar materiais escolares.",
            "Armazena canetas, lápis, borrachas e apontadores organizados.",
            "Protege os itens e facilita o transporte dentro da mochila.",
            "Disponível em diversos tecidos, formatos e estampas.",
        ],
        "Grampeador": [
            "Aparelho mecânico usado para fixar folhas de papel juntas.",
            "Utiliza pequenos grampos metálicos curvados pela pressão.",
            "Organiza documentos e trabalhos escolares volumosos.",
            "Comum em escritórios, secretarias e escolas.",
        ],
        "Calculadora": [
            "Dispositivo eletrônico portátil usado para resolver operações matemáticas.",
            "Possui visor digital e teclado numérico com funções científicas.",
            "Facilita cálculos complexos de matemática, física e finanças.",
            "Pode ser alimentada por pilhas ou luz solar.",
        ],
        "Marca-texto": [
            "Caneta hidrográfica com tinta fluorescente de cores vivas.",
            "Utilizada para destacar trechos importantes de textos em livros.",
            "Possui ponta chanfrada grossa para cobrir linhas de texto.",
            "Cores comuns incluem amarelo, verde e rosa neon.",
        ],
        "Agenda": [
            "Caderno organizado por dias do ano para anotação de compromissos.",
            "Auxilia no planejamento de tarefas, provas e reuniões.",
            "Possui divisões mensais e espaço para horários.",
            "Ajuda a manter a rotina diária organizada.",
        ],
        "Pasta": [
            "Invólucro de plástico ou papelão usado para guardar documentos.",
            "Protege papéis importantes contra amassados e rasgos.",
            "Pode conter divisórias internas, elástico ou abas.",
            "Mantém trabalhos e folhas soltas organizados na mochila.",
        ],
    },
    "Higiene & Cuidados Pessoais": {
        "Escova de dentes": [
            "Utensílio de higiene bucal com cabo e cerdas macias nas pontas.",
            "Utilizado junto com o creme dental para escovar os dentes.",
            "Remove restos de comida e placa bacteriana da boca.",
            "Recomenda-se trocar de escova a cada três meses.",
        ],
        "Pasta de dentes": [
            "Creme higienizante aplicado na escova para limpeza dos dentes.",
            "Contém flúor para proteger o esmalte contra cáries.",
            "Deixa o hálito fresco e limpo após a escovação.",
            "Disponível em diversas marcas e sabores refrescantes.",
        ],
        "Sabonete": [
            "Produto de limpeza pessoal usado para lavar o corpo e as mãos.",
            "Pode ser encontrado em barras sólidas ou líquido em dispenser.",
            "Remove impurezas, oleosidade e bactérias da pele.",
            "Gera espuma perfumada durante o banho.",
        ],
        "Shampoo": [
            "Produto cosmético líquido formulado para higienizar o cabelo e couro cabeludo.",
            "Remove sujeira, sebo e resíduos acumulados nos fios.",
            "Faz bastante espuma ao ser massageado na cabeça molhada.",
            "Encontrado em fórmulas específicas para cada tipo de cabelo.",
        ],
        "Condicionador": [
            "Produto aplicado nos cabelos após o uso do shampoo.",
            "Fecha as cutículas dos fios, devolvendo maciez e brilho.",
            "Facilita o ato de desembaraçar o cabelo no banho.",
            "Deixa os fios mais hidratados e fáceis de pentear.",
        ],
        "Toalha": [
            "Peça de tecido felpudo projetada para absorver a água do corpo.",
            "Utilizada para secar a pele após o banho, piscina ou praia.",
            "Disponível em tamanhos variados para rosto e banho.",
            "Feita comumente de algodão macio e absorvente.",
        ],
        "Pente": [
            "Placa estreita de plástico ou metal com dentes alinhados.",
            "Utilizado para desembaraçar e arrumar os cabelos.",
            "Cabe facilmente no bolso ou em pequenas nécessaires.",
            "Ideal para cabelos curtos ou alinhamento rápido.",
        ],
        "Escova de cabelo": [
            "Utensílio com cerdas flexíveis em base ampla para pentear os cabelos.",
            "Desembaraça fios longos sem machucar o couro cabeludo.",
            "Auxilia na distribuição natural da oleosidade pelos fios.",
            "Usada também junto com secador para modelar o cabelo.",
        ],
        "Desodorante": [
            "Produto de higiene pessoal aplicado nas axilas.",
            "Controla e previne o odor causado pela transpiração.",
            "Pode ser encontrado em formato aerossol, roll-on ou bastão.",
            "Proporciona sensação de frescor ao longo do dia.",
        ],
        "Perfume": [
            "Cosmético líquido composto por óleos aromáticos e álcool.",
            "Borrifado na pele para deixar um aroma agradável e marcante.",
            "Possui notas olfativas variadas como amadeiradas, florais ou cítricas.",
            "Usado em ocasiões especiais ou no dia a dia.",
        ],
        "Barbeador": [
            "Aparelho manual ou elétrico usado para cortar pelos do rosto.",
            "Utiliza lâminas afiadas para fazer a barba ou raspar o cabelo.",
            "Pode requerer o uso de espuma de barbear para deslizar melhor.",
            "Garante um visual limpo e sem pelos na pele.",
        ],
        "Papel higiênico": [
            "Papel macio e absorvente desenvolvido para fins de higiene pessoal.",
            "Utilizado após o uso do banheiro para limpeza íntima.",
            "Fabricado em rolos picotados fáceis de destacar.",
            "Item indispensável em qualquer banheiro residencial ou público.",
        ],
        "Cortador de unhas": [
            "Pequeno utensílio metálico com alavanca e lâminas curvas.",
            "Utilizado para aparar e encurtar as unhas das mãos e pés.",
            "Possui uma pequena lixa integrada em sua estrutura.",
            "Mantém as unhas limpas e com tamanho adequado.",
        ],
        "Fio dental": [
            "Filme de náilon ou teflon fino usado para limpeza entre os dentes.",
            "Remove restos de alimentos onde a escova não consegue alcançar.",
            "Essencial para prevenir cáries e inflamações na gengiva.",
            "Utilizado diariamente antes ou depois da escovação.",
        ],
        "Algodão": [
            "Fibra têxtil macia e branca em formato de bolas ou discos.",
            "Utilizado para limpeza facial, remoção de maquiagem ou curativos.",
            "Altamente absorvente e delicado com a pele.",
            "Item coringa na farmacinha e no kit de higiene.",
        ],
    },
    "Utilidades & Ferramentas": {
        "Chave de carro": [
            "Dispositivo mecânico ou eletrônico para destravar e dar partida em veículos.",
            "Pode conter botões de alarme e chaveiro integrado.",
            "Modelos modernos possuem tecnologia presencial por aproximação.",
            "Item pessoal que exige cuidado para não ser extraviado.",
        ],
        "Capacete": [
            "Equipamento de proteção individual rígido para a cabeça.",
            "Obrigatório para motociclistas e ciclistas em vias públicas.",
            "Protege o crânio contra impactos em caso de quedas ou acidentes.",
            "Possui viseira transparente e jugular ajustável.",
        ],
        "Volante": [
            "Peça circular na cabine do veículo usada para direcionar as rodas.",
            "Controla a direção e o sentido para onde o carro vai.",
            "Geralmente possui buzina no centro e comandos de som.",
            "Manuseado com as duas mãos pelo motorista.",
        ],
        "Retrovisor": [
            "Espelho posicionado nas laterais e dentro do carro.",
            "Permite ao motorista enxergar o trânsito atrás e ao lado do veículo.",
            "Essencial para realizar manobras seguras, conversões e ultrapassagens.",
            "Deve ser ajustado corretamente antes de iniciar a viagem.",
        ],
        "Pneu": [
            "Anel de borracha inflada colocado ao redor das rodas do veículo.",
            "Mantém o contato e a aderência do carro com o solo.",
            "Possui sulcos que escoam a água da chuva para evitar derrapagens.",
            "Suporta todo o peso do automóvel em movimento.",
        ],
        "Cinto de segurança": [
            "Fita de tecido resistente presa ao banco do veículo.",
            "Obrigatório para reter os ocupantes em freadas bruscas ou colisões.",
            "Salva vidas ao impedir que o corpo seja lançado para frente.",
            "Dispositivo de segurança automotivo fundamental.",
        ],
        "Mochila": [
            "Bolsa de transporte resistente usada nas costas com alças duplas.",
            "Útil para carregar pertences em viagens curtas ou no dia a dia.",
            "Possui grande capacidade de armazenamento interno.",
            "Prática para manter as mãos livres enquanto se caminha.",
        ],
        "Guarda-chuva": [
            "Acessório portátil de lona impermeável aberto sobre uma haste.",
            "Protege a pessoa contra a chuva e tempestades na rua.",
            "Pode ser fechado e guardado de forma compacta quando não usado.",
            "Item indispensável nos dias de clima chuvoso.",
        ],
        "Óculos de sol": [
            "Acessório com lentes escuras usado para proteger os olhos da claridade.",
            "Bloqueia os raios ultravioleta (UV) prejudiciais à visão.",
            "Também serve como peça de estilo e composição de visual.",
            "Muito utilizado em dias ensolarados ao ar livre.",
        ],
        "Garrafa de água": [
            "Recipiente portátil reutilizável para transporte de líquidos.",
            "Ajuda a manter a hidratação corporal ao longo do dia.",
            "Pode ser feita de alumínio, plástico resistente ou inox térmico.",
            "Acompanha pessoas na academia, trabalho ou passeios.",
        ],
        "Martelo": [
            "Ferramenta manual com cabo e cabeça pesada de metal.",
            "Utilizada principalmente para golpear pregos e fixar estruturas.",
            "Possui uma orelha na parte traseira para arrancar pregos tortos.",
            "Presente em qualquer caixa de ferramentas básica.",
        ],
        "Chave de fenda": [
            "Ferramenta manual com haste metálica e ponta chata.",
            "Utilizada para apertar ou soltar parafusos com fenda simples.",
            "Possui cabo ergonômico emborrachado para firmeza na pega.",
            "Item essencial em reparos domésticos e montagem de móveis.",
        ],
        "Alicate": [
            "Ferramenta metálica articulada usada para segurar, puxar ou cortar fios.",
            "Possui mandíbulas resistentes acionadas por pressão manual.",
            "Muito útil em trabalhos elétricos, mecânicos e manutenções.",
            "Proporciona forte alavanca para prender objetos.",
        ],
        "Furadeira": [
            "Eletroferramenta potente usada para fazer furos em paredes e madeiras.",
            "Utiliza brocas rotativas encaixadas em seu mandril.",
            "Indispensável para pendurar quadros, prateleiras e suportes.",
            "Pode funcionar com fio na tomada ou a bateria recarregável.",
        ],
        "Parafuso": [
            "Pino metálico roscado usado para unir peças de forma firme.",
            "Possui cabeça com encaixe para chave de fenda ou Phillips.",
            "Fixa móveis, dobradiças e estruturas com segurança.",
            "Trabalha em conjunto com porcas ou buchas na parede.",
        ],
        "Prego": [
            "Haste metálica pontiaguda com cabeça chata em uma extremidade.",
            "Pregado diretamente na madeira com o auxílio de um martelo.",
            "Utilizado para unir peças de madeira em construções e carpintaria.",
            "Alternativa rápida de fixação sem necessidade de rosca.",
        ],
        "Trena": [
            "Instrumento de medição flexível enrolado dentro de uma caixa.",
            "Fita métrica metálica usada para medir comprimentos e distâncias.",
            "Possui trava para manter a fita esticada durante a medição.",
            "Fundamental para arquitetos, pedreiros e reformas.",
        ],
        "Serra": [
            "Ferramenta com lâmina dentada de metal usada para cortar materiais.",
            "Pode ser manual (para madeira ou metal) ou elétrica.",
            "Corta blocos, galhos e tubulações com precisão e atrito.",
            "Exige cuidado e uso de equipamentos de proteção.",
        ],
        "Chave inglesa": [
            "Ferramenta manual com abertura de mandíbula ajustável.",
            "Usada para apertar e afrouxar porcas e parafusos de tamanhos variados.",
            "Substitui várias chaves fixas graças à sua rosca regulável.",
            "Comum em reparos hidráulicos e manutenções gerais.",
        ],
        "Lanterna": [
            "Dispositivo portátil de iluminação alimentado por pilhas ou bateria.",
            "Emite um facho de luz concentrado para ambientes escuros.",
            "Muito útil em quedas de energia, trilhas ou emergências noturnas.",
            "Hoje em dia também integrada na maioria dos smartphones.",
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
     "Programador": [
            "Profissional que escreve códigos e instruções para computadores.",
            "Utiliza linguagens como Python, JavaScript ou C++.",
            "Cria softwares, sites e aplicativos do dia a dia.",
            "Passa boa parte do tempo corrigindo erros e bugs.",
        ],
        "Desenvolvedor de Software": [
            "Especialista focado no ciclo completo de criação de sistemas.",
            "Projeta, testa e mantém programas e aplicativos funcionais.",
            "Trabalha em equipe para atender às necessidades dos usuários.",
            "Atua em áreas como Front-End, Back-End ou Full-Stack.",
        ],
        "Engenheiro de Software": [
            "Aplica princípios de engenharia no desenvolvimento de sistemas.",
            "Focado na arquitetura, escalabilidade e qualidade de códigos.",
            "Projeta grandes estruturas de software para empresas.",
            "Trabalha com metodologias ágeis e padrões de projeto.",
        ],
        "Analista de Cibersegurança": [
            "Responsável por proteger dados e sistemas contra ataques digitais.",
            "Monitora redes em busca de vulnerabilidades e invasões.",
            "Implementa firewalls, criptografia e políticas de segurança.",
            "Atua para evitar vazamento de informações confidenciais.",
        ],
        "Hacker Ético": [
            "Profissional contratado para invadir sistemas com permissão.",
            "Realiza testes de penetração (pentests) para achar falhas.",
            "Ajuda empresas a fortalecerem suas defesas antes de ataques reais.",
            "Também conhecido como 'White Hat'.",
        ],
        "Cientista de Dados": [
            "Analisa grandes volumes de dados para extrair insights valiosos.",
            "Utiliza estatística, inteligência artificial e aprendizado de máquina.",
            "Cria modelos preditivos para apoiar decisões de negócios.",
            "Trabalha muito com ferramentas como Python, R e SQL.",
        ],
        "Engenheiro de Inteligência Artificial": [
            "Desenvolve algoritmos capaz de simular o raciocínio humano.",
            "Cria modelos de Machine Learning e redes neurais profundas.",
            "Atua em projetos como chatbots, visão computacional e automações.",
            "Trabalha na vanguarda da inovação tecnológica.",
        ],
        "Técnico de Informática": [
            "Profissional focado na manutenção de hardware e software.",
            "Formata computadores, troca peças e instala programas.",
            "Presta suporte presencial ou remoto para usuários com dúvidas.",
            "Resolve problemas operacionais de computadores e redes locais.",
        ],
        "Administrador de Redes": [
            "Gerencia a infraestrutura de conexão e servidores de uma empresa.",
            "Garante que a internet, cabos e roteadores funcionem sem quedas.",
            "Configura permissões de acesso e segurança de rede.",
            "Essencial para manter o fluxo de comunicação digital interno.",
        ],
        "Designer UX/UI": [
            "Projeta a experiência e a interface visual de sites e aplicativos.",
            "Focado em deixar as telas bonitas, intuitivas e fáceis de usar.",
            "Cria protótipos, fluxos de navegação e testes com usuários.",
            "Une estética visual com usabilidade prática.",
        ],
        "Médico": [
            "Profissional da saúde responsável por diagnosticar e tratar doenças.",
            "Realiza exames, consultas e prescreve medicamentos.",
            "Trabalha em hospitais, postos de saúde ou consultórios.",
            "Presta o juramento de Hipócrates ao se formar.",
        ],
        "Enfermeiro": [
            "Cuida diretamente do bem-estar e da recuperação de pacientes.",
            "Aplica medicações, faz curativos e monitora sinais vitais.",
            "Trabalha em parceria com médicos em triagens e UTIs.",
            "Acompanha o paciente durante todo o período de internação.",
        ],
        "Dentista": [
            "Especialista na saúde da boca, dentes e gengivas.",
            "Realiza limpezas, obturações, extrações e tratamentos de canal.",
            "Utiliza a famosa cadeira reclinável e broca odontológica.",
            "Ajuda a manter a estética e o funcionamento do sorriso.",
        ],
        "Psicólogo": [
            "Profissional que estuda a mente e o comportamento humano.",
            "Realiza sessões de terapia para escutar e orientar pacientes.",
            "Ajuda no tratamento de ansiedade, depressão e conflitos pessoais.",
            "Utiliza abordagens como a psicanálise ou cognitivo-comportamental.",
        ],
        "Veterinário": [
            "Médico responsável pela saúde e cuidados com animais.",
            "Atende desde pets domésticos até animais de grande porte no campo.",
            "Aplica vacinas, realiza cirurgias e orienta a nutrição animal.",
            "Garante a proteção e o bem-estar do mundo animal.",
        ],
        "Fisioterapeuta": [
            "Trata e previne lesões musculares e articulares.",
            "Utiliza exercícios, massagens e aparelhos de reabilitação.",
            "Ajuda pacientes a recuperarem os movimentos do corpo.",
            "Atua na área esportiva, pós-operatória e neurológica.",
        ],
        "Cardiologista": [
            "Médico especialista na saúde do coração e dos vasos sanguíneos.",
            "Solicita exames como eletrocardiograma e teste ergométrico.",
            "Trata condições como hipertensão, arritmias e infartos.",
            "Orienta hábitos saudáveis para prevenir problemas cardíacos.",
        ],
        "Dermatologista": [
            "Médico especialista no cuidado com a pele, cabelos e unhas.",
            "Trata condições como acne, manchas, alergias e lesões graves.",
            "Realiza procedimentos estéticos e preventivos na pele.",
            "Orienta sobre o uso correto de protetor solar.",
        ],
        "Nutricionista": [
            "Profissional focado em alimentação e hábitos alimentares saudáveis.",
            "Elabora dietas personalizadas para emagrecimento ou ganho de massa.",
            "Trabalha em consultórios, hospitais, academias e escolas.",
            "Avalia a composição corporal e necessidades de nutrientes.",
        ],
        "Cirurgião": [
            "Médico especializado em realizar intervenções operatórias manuais.",
            "Atua no centro cirúrgico com vestimenta e instrumentos estéreis.",
            "Realiza procedimentos para reparar, remover ou transplantar órgãos.",
            "Trabalha acompanhado de uma equipe com anestesista e enfermeiros.",
        ],
        "Advogado": [
            "Profissional licenciado para defender os interesses de seus clientes.",
            "Atua com leis, processos, contratos e audiências judiciais.",
            "Precisa passar no exame da Ordem dos Advogados (OAB).",
            "Trabalha em áreas como civil, penal, trabalhista e tributária.",
        ],
        "Juiz": [
            "Autoridade pública responsável por julgar processos e aplicar leis.",
            "Preside audiências e toma decisões finais em tribunal.",
            "Analisa provas e argumentos de advogados e promotores.",
            "Usa a toga em sessões oficiais de julgamento.",
        ],
        "Promotor": [
            "Membro do Ministério Público que defende os interesses da sociedade.",
            "Acusa réus em processos criminais e investiga irregularidades.",
            "Atua na fiscalização do cumprimento das leis e direitos coletivos.",
            "Conhecido como a acusação no Tribunal do Júri.",
        ],
        "Delegado": [
            "Autoridade policial responsável por comandar uma delegacia.",
            "Lidera investigações de crimes e assina inquéritos policiais.",
            "Determina prisões em flagrante e solicita mandados de busca.",
            "Garante a ordem pública e o cumprimento das leis na polícia civil.",
        ],
        "Policial": [
            "Agente de segurança pública responsável pelo patrulhamento e ordem.",
            "Atua no combate direto ao crime e na proteção dos cidadãos.",
            "Utiliza farda, viatura e equipamentos de proteção no trabalho.",
            "Responde a chamados de emergência no dia a dia das cidades.",
        ],
        "Perito Criminal": [
            "Especialista que analisa cenas de crimes em busca de provas físicas.",
            "Coleta digitais, vestígios e realiza exames balísticos e DNA.",
            "Elabora laudos técnicos que ajudam a esclarecer investigações.",
            "Aplica métodos científicos na investigação policial.",
        ],
        "Investigador": [
            "Agente policial focado em descobrir a autoria de crimes.",
            "Coleta depoimentos, faz campanas e reúne pistas em segredo.",
            "Trabalha para esclarecer casos complexos sob comando do delegado.",
            "Analisa evidências para montar o histórico dos fatos.",
        ],
        "Bombeiro": [
            "Profissional especializado em combater incêndios e salvar vidas.",
            "Realiza resgates em acidentes de trânsito, afogamentos e desabamentos.",
            "Utiliza caminhões com escadas, mangueiras e trajes térmicos.",
            "Atende chamados de emergência de alto risco.",
        ],
        "Segurança Particular": [
            "Profissional contratado para proteger estabelecimentos ou pessoas VIPs.",
            "Controla acessos, monitora câmeras e previne incidentes.",
            "Atua em eventos, bancos, shoppings ou escolta armada.",
            "Mantém a vigilância constante do local sob sua responsabilidade.",
        ],
        "Agente Federal": [
            "Membro da Polícia Federal responsável por crimes de âmbito nacional.",
            "Atua no combate ao tráfico internacional, corrupção e crimes federais.",
            "Trabalha na fiscalização de fronteiras e emissão de passaportes.",
            "Lida com investigações de grande porte no país.",
        ],
        "Jogador de Futebol": [
            "Atleta profissional que disputa partidas de futebol nos gramados.",
            "Treina diariamente tática, física e habilidade com a bola nos pés.",
            "Atua em clubes de futebol e pode ser convocado para a seleção.",
            "Entra em campo diante de torcidas em estádios lotados.",
        ],
        "Piloto de Fórmula 1": [
            "Atleta que guia carros monopostos em altíssimas velocidades.",
            "Disputa o campeonato mundial em circuitos por todo o planeta.",
            "Usa capacete, macacão antiflama e lida com altas forças G.",
            "Trabalha em sintonia fina com a equipe nos boxes.",
        ],
        "Jogador de Basquete": [
            "Atleta que compete em quadras tentando acertar a bola na cesta.",
            "Destaca-se pela altura, impulsão, enterradas e arremessos.",
            "A liga de maior prestígio do mundo nessa modalidade é a NBA.",
            "Partida disputada por cinco jogadores de cada lado na quadra.",
        ],
        "Lutador de MMA": [
            "Atleta de artes marciais mistas que combate dentro de um octógono.",
            "Combina técnicas de boxe, muay thai, jiu-jitsu e wrestling.",
            "Competição famosa no evento mundial conhecido como UFC.",
            "Luta usando luvas abertas e proteção bucal.",
        ],
        "Tenista": [
            "Atleta que utiliza raquete para rebater uma bola amarela sobre a rede.",
            "Disputa partidas individuais ou em duplas em quadras de saibro, grama ou dura.",
            "Compete em grandes torneios como o Grand Slam.",
            "Contabiliza pontos em games e sets durante a partida.",
        ],
        "Nadador": [
            "Atleta focado em velocidade na água em piscinas ou águas abertas.",
            "Domina estilos como crawl, costas, peito e borboleta.",
            "Treina resistência e ganho de milésimos de segundo nas braçadas.",
            "Usa touca, óculos de natação e sunga/maiô de alta performance.",
        ],
        "Atleta Olímpico": [
            "Esportista de alto rendimento que representa seu país nos Jogos Olímpicos.",
            "Dedica anos de treino para alcançar o topo de sua modalidade.",
            "Busca conquistar as medalhas de ouro, prata ou bronze.",
            "Participa da maior celebração do esporte mundial a cada 4 anos.",
        ],
        "Técnico Esportivo": [
            "Responsável pelo comando e estratégias de um time ou atleta.",
            "Define escalações, táticas, substituições e treinos intensos.",
            "Grita orientações à beira do campo ou quadra durante os jogos.",
            "Lida com a pressão por resultados positivos da torcida.",
        ],
        "Árbitro": [
            "Responsável por fazer cumprir as regras em uma competição esportiva.",
            "Aplica cartões, apita faltas e valida pontos ou gols.",
            "Precisa manter a imparcialidade durante todo o jogo.",
            "Também conhecido carinhosamente como 'juiz da partida'.",
        ],
        "Preparador Físico": [
            "Profissional focado no condicionamento e força muscular dos atletas.",
            "Planeja treinos de resistência, explosão e prevenção de lesões.",
            "Acompanha o desempenho físico da equipe antes e durante a temporada.",
            "Trabalha alinhado ao departamento médico e comissão técnica.",
        ],
        "Ator": [
            "Profissional masculino que interpreta personagens em obras artísticas.",
            "Atua em produções de teatro, cinema, televisão e novelas.",
            "Decora roteiros, estuda falas e encena emoções.",
            "Trabalha sob a orientação de diretores cênicos.",
        ],
        "Atriz": [
            "Profissional feminina que dá vida a personagens em produções artísticas.",
            "Interpreta papeis no cinema, teatro, séries e televisão.",
            "Transmite emoções e histórias através da atuação.",
            "Participa de ensaios e caracterização de personagens.",
        ],
        "Cantor": [
            "Artista que utiliza a própria voz como instrumento musical principal.",
            "Grava álbuns em estúdio e faz shows ao vivo em palcos.",
            "Interpreta músicas de diversos gêneros acompanhado de banda.",
            "Apresenta-se para públicos em turnês musicais.",
        ],
        "Cantora": [
            "Artista feminina que se expressa através do canto e da música.",
            "Grava videoclipes, músicas e se apresenta em festivais e shows.",
            "Pode compor suas próprias letras ou interpretar canções.",
            "Conquista fãs com seu alcance vocal e presença de palco.",
        ],
        "DJ": [
            "Profissional que seleciona e mistura músicas para um público.",
            "Utiliza mesas de som, pickups, controladores e fones de ouvido.",
            "Comanda a pista de dança em festas, baladas e festivais.",
            "Cria transições suaves entre faixas e produz remixes.",
        ],
        "Diretor de Cinema": [
            "Responsável por comandar a visão artística de um filme.",
            "Orienta a atuação dos atores e o posicionamento das câmeras.",
            "Supervisiona a gravação, iluminação e edição da obra.",
            "Transforma o roteiro escrito em uma produção audiovisual.",
        ],
        "Roteirista": [
            "Escritor responsável por criar a história e diálogos de um filme ou série.",
            "Desenvolve a narrativa, arcos de personagens e cenas do roteiro.",
            "Cria a base escrita para produções de cinema, TV ou jogos.",
            "Formata o texto com ações e falas para os atores.",
        ],
        "Modelo": [
            "Profissional que exibe roupas, acessórios ou produtos em desfiles e ensaios.",
            "Trabalha para grifes de moda, revistas e campanhas publicitárias.",
            "Desfila em passarelas e faz poses para fotógrafos de moda.",
            "Representa a imagem visual de marcas do mercado.",
        ],
        "Dançarino": [
            "Artista que se expressa corporalmente através do ritmo e da dança.",
            "Ensaia coreografias complexas para shows, peças e videoclipes.",
            "Domina estilos como balé, hip-hop, dança contemporânea ou salão.",
            "Utiliza flexibilidade, força e ritmo em suas apresentações.",
        ],
        "Influenciador Digital": [
            "Criador de conteúdo com grande alcance nas redes sociais.",
            "Publica vídeos, fotos e rotinas gerando alto engajamento.",
            "Faz parcerias com marcas e publicidades para seus seguidores.",
            "Impacta opiniões e tendências no ambiente online.",
        ],
        "Engenheiro Civil": [
            "Profissional que projeta e gerencia obras de infraestrutura.",
            "Supervisiona a construção de prédios, pontes, estradas e barragens.",
            "Garante a segurança estrutural e cálculos de materiais da obra.",
            "Usa capacete de proteção e analisa plantas em canteiros de obra.",
        ],
        "Engenheiro Mecânico": [
            "Projeta e desenvolve máquinas, motores e sistemas mecânicos.",
            "Atua na indústria automobilística, aeronáutica e fabril.",
            "Analisa forças, dinâmica, termodinâmica e peças metálicas.",
            "Cria protótipos de peças e equipamentos industriais.",
        ],
        "Engenheiro Elétrico": [
            "Especialista em geração, transmissão e distribuição de energia elétrica.",
            "Projeta circuitos elétricos, usinas e sistemas de alta tensão.",
            "Trabalha com eletrônica, automação e redes de energia.",
            "Garante o funcionamento seguro da fiação e redes elétricas.",
        ],
        "Arquiteto": [
            "Projeta espaços internos e externos unindo funcionalidade e estética.",
            "Desenvolve plantas baixas e maquetes de casas e edifícios.",
            "Planeja a iluminação, ventilação e design dos ambientes.",
            "Trabalha em parceria com a engenharia na criação de construções.",
        ],
        "Pedreiro": [
            "Profissional fundamental na construção e reforma de estruturas.",
            "Ergue paredes de tijolos, aplica reboco e faz contraprovas.",
            "Manuseia cimento, argamassa, colher de pedreiro e prumo.",
            "Transforma projetos no papel em estruturas físicas no canteiro.",
        ],
        "Eletricista": [
            "Especialista em instalação e manutenção de redes elétricas.",
            "Instala tomadas, disjuntores, fiação e lustres em imóveis.",
            "Mede voltagem e corrige curtos-circuitos com segurança.",
            "Utiliza ferramentas isoladas como alicates e multímetros.",
        ],
        "Encanador": [
            "Profissional focado em sistemas de tubulação de água e esgoto.",
            "Conserta vazamentos, desentope canos e instala torneiras.",
            "Monta tubulações de PVC ou cobre em construções e casas.",
            "Garante o fluxo correto de água potável e saneamento.",
        ],
        "Marceneiro": [
            "Artesão especializado em fabricar e reparar móveis de madeira.",
            "Cria armários, mesas e cadeiras sob medida.",
            "Utiliza ferramentas como serras, lixas, plainas e martelos.",
            "Trabalha com acabamentos em verniz, laca e MDF.",
        ],
        "Mestre de Obras": [
            "Responsável por fiscalizar e orientar o trabalho no canteiro de obras.",
            "Garante que os trabalhadores sigam as plantas e prazos do projeto.",
            "Distribui tarefas diárias para pedreiros e ajudantes.",
            "Faz a ponte entre os engenheiros e a equipe de execução.",
        ],
        "Topógrafo": [
            "Realiza medições e mapeamento detalhado de terrenos.",
            "Utiliza equipamentos de precisão como teodolitos e estações totais.",
            "Determina relevos, curvas de nível e limites de propriedades.",
            "Essencial na fase inicial antes do começo de qualquer construção.",
        ],
        "Empresário": [
            "Proprietário de um negócio ou empresa comercial.",
            "Investe recursos, assume riscos e busca o crescimento da marca.",
            "Gera empregos e toma decisões estratégicas para o mercado.",
            "Lidera o empreendimento em direção ao lucro e inovação.",
        ],
        "Administrador": [
            "Gerencia os recursos humanos, financeiros e materiais de uma organização.",
            "Planeja, organiza, lidera e controla os processos da empresa.",
            "Busca eficiência e cumprimento de metas corporativas.",
            "Toma decisões estratégicas para o funcionamento da empresa.",
        ],
        "Contador": [
            "Profissional responsável pela contabilidade e finanças de empresas.",
            "Cuida de balanços, declaração de impostos e fluxo de caixa.",
            "Garante o cumprimento das obrigações fiscais e tributárias.",
            "Analisa livros contábeis e demonstrativos financeiros.",
        ],
        "Economista": [
            "Estuda a produção, distribuição e consumo de bens e serviços.",
            "Analisa cenários de inflação, taxas de juros e mercado financeiro.",
            "Realiza projeções econômicas para governos e empresas.",
            "Compreende o funcionamento dos mercados e moedas.",
        ],
        "Gerente": [
            "Líder encarregado de supervisionar uma equipe ou departamento.",
            "Garante o cumprimento de metas e a rotina de trabalho dos funcionários.",
            "Organiza tarefas, resolve conflitos internos e cobra resultados.",
            "Ponte de comunicação entre a diretoria e os colaboradores.",
        ],
        "Diretor Executivo (CEO)": [
            "Cargo mais alto na hierarquia de gestão de uma grande empresa.",
            "Toma as decisões de maior impacto e define o futuro da organização.",
            "Presta contas aos acionistas e ao conselho de administração.",
            "Comanda as estratégias globais de expansão do negócio.",
        ],
        "Investidor": [
            "Aplica capital financeiro em ações, imóveis ou startups visando retorno.",
            "Analisa riscos, oportunidades e tendências do mercado financeiro.",
            "Aposta no crescimento de empresas para obter lucros futuros.",
            "Gera renda através do rendimento de seus ativos.",
        ],
        "Corretor de Imóveis": [
            "Intermedia a compra, venda e aluguel de imóveis residenciais ou comerciais.",
            "Acompanha clientes em visitas a casas, apartamentos e terrenos.",
            "Atua na negociação de valores e documentação imobiliária.",
            "Possui registro profissional no CRECI.",
        ],
        "Vendedor": [
            "Profissional focado em oferecer produtos ou serviços a clientes.",
            "Apresenta vantagens do produto, negocia preços e fecha vendas.",
            "Trabalha no comércio, lojas de shopping ou vendas corporativas.",
            "Atende o público com boa comunicação e persuasão.",
        ],
        "Analista Financeiro": [
            "Avalia dados financeiros para orientar decisões de investimento da empresa.",
            "Acompanha relatórios de custos, receitas, lucros e orçamentos.",
            "Monta planilhas e projeções de fluxo de caixa corporativo.",
            "Identifica oportunidades para otimizar os gastos da empresa.",
        ],
        "Motorista": [
            "Profissional habilitado que conduz veículos para transporte de pessoas ou cargas.",
            "Trabalha com táxis, aplicativos, ônibus ou frotas privadas.",
            "Conhece as rotas de trânsito e leis de circulação urbana.",
            "Garante o transporte seguro de passageiros até o destino.",
        ],
        "Piloto de Avião": [
            "Comanda aeronaves comerciais, privadas ou de carga nos céus.",
            "Realiza procedimentos de decolagem, voo em cruzeiro e pouso.",
            "Comunica-se com a torre de controle de tráfego aéreo.",
            "Trabalha na cabine de comando acompanhado do co-piloto.",
        ],
        "Caminhoneiro": [
            "Motorista de grandes veículos de carga que viaja pelas rodovias.",
            "Transporta mercadorias, alimentos e suprimentos por longas distâncias.",
            "Passa dias na estrada dormindo em postos e boleias.",
            "Crucial para o abastecimento do comércio e da indústria nacional.",
        ],
        "Mecânico": [
            "Especialista no conserto e manutenção de motores e veículos.",
            "Identifica falhas em carros, motos, caminhões ou máquinas.",
            "Troca óleos, peças, pastilhas de freio e faz revisões.",
            "Trabalha em oficinas mecânicas com ferramentas manuais.",
        ],
        "Engenheiro Automotivo": [
            "Projeta e desenvolve carros, motos e sistemas de mobilidade.",
            "Trabalha na criação de motores eficientes, suspensões e aerodinâmica.",
            "Testa segurança, desempenho e eficiência de veículos.",
            "Atua nas grandes montadoras da indústria automobilística.",
        ],
        "Motoboy": [
            "Entregador rápido que utiliza motocicleta para transporte na cidade.",
            "Realiza entregas de documentos, encomendas e refeições.",
            "Navega pelo trânsito urbano agitado para cumprir prazos curtos.",
            "Trabalha com baú ou mochila de entrega nas costas.",
        ],
        "Comissário de Bordo": [
            "Profissional responsável pela segurança e conforto em voos comerciais.",
            "Demonstra procedimentos de emergência na cabine de passageiros.",
            "Serve refeições, bebidas e atende necessidades durante o voo.",
            "Também conhecido carinhosamente como aeromoça ou aeromoço.",
        ],
        "Maquinista": [
            "Profissional que opera e conduz trens ou metrôs em trilhos.",
            "Controla aceleração, frenagem e paradas nas estações.",
            "Garante a segurança do transporte ferroviário de passageiros ou cargas.",
            "Monitora painéis e sinalizações ao longo das vias férreas.",
        ],
        "Marinheiro": [
            "Trabalhador que atua a bordo de navios, barcos e embarcações.",
            "Realiza tarefas de navegação, amarração e manutenção da embarcação.",
            "Enfrenta longos períodos no mar em viagens marítimas.",
            "Integra a tripulação de navios de carga, cruzeiros ou militares.",
        ],
        "Instrutor de Autoescola": [
            "Profissional que ensina alunos a dirigir carros ou pilotar motos.",
            "Leciona aulas práticas no trânsito e teóricas sobre regramento.",
            "Prepara novos condutores para passarem no exame de motorista.",
            "Acompanha o aluno no veículo de pedal duplo adaptado.",
        ],
        "Professor": [
            "Educador dedicado ao ensino e transmissão de conhecimento.",
            "Leciona aulas em escolas, prepara conteúdos e corrige provas.",
            "Ensina disciplinas como matemática, história, português ou ciências.",
            "Acompanha a formação e aprendizado dos estudantes.",
        ],
        "Diretor Escolar": [
            "Gestor responsável pela liderança geral de uma instituição de ensino.",
            "Coordena a equipe de professores, funcionários e administração.",
            "Garante o bom ambiente escolar e relação com pais e alunos.",
            "Zela pelo cumprimento das diretrizes pedagógicas e financeiras.",
        ],
        "Pedagogo": [
            "Especialista nos processos de ensino e aprendizagem infantil.",
            "Planeja métodos educativos e coordena projetos pedagógicos.",
            "Atua na alfabetização e desenvolvimento cognitivo de crianças.",
            "Acompanha o aprendizado individual e inclusão na escola.",
        ],
        "Pesquisador": [
            "Profissional dedicado à investigação científica e descoberta de conhecimentos.",
            "Coleta dados, realiza experimentos e publica artigos científicos.",
            "Atua em laboratórios, universidades e centros de pesquisa.",
            "Busca respostas para problemas complexos da sociedade.",
        ],
        "Cientista": [
            "Especialista que aplica o método científico para entender o mundo.",
            "Formula hipóteses, realiza testes e desenvolve teorias.",
            "Atua em áreas como física, química, biologia ou astronomia.",
            "Contribui para avanços medicinais e tecnológicos da humanidade.",
        ],
        "Bibliotecário": [
            "Profissional responsável por organizar, catalogar e preservar acervos.",
            "Gerencia bibliotecas físicas e bancos de dados digitais.",
            "Auxilia leitores e estudantes na busca por livros e pesquisas.",
            "Classifica obras por sistemas de catalogação temática.",
        ],
        "Orientador Educacional": [
            "Apoia o desenvolvimento pessoal, emocional e acadêmico de alunos.",
            "Auxilia estudantes na resolução de conflitos e escolha profissional.",
            "Trabalha em conjunto com professores, pais e a direção da escola.",
            "Acompanha o bem-estar dos alunos no ambiente de ensino.",
        ],
        "Professor Universitário": [
            "Docente focado no ensino superior e na formação acadêmica.",
            "Ministra aulas em faculdades, orienta teses e pesquisas de graduação.",
            "Normalmente possui títulos de mestre ou doutor em sua área.",
            "Combina atividades de ensino, pesquisa e extensão acadêmica.",
        ],
        "Tradutor": [
            "Profissional que converte textos escritos de um idioma para outro.",
            "Trabalha com livros, documentos oficiais, legendas e sites.",
            "Preserva o sentido original mantendo a adequação cultural.",
            "Domina profundamente a gramática e vocabulário de múltiplos idiomas.",
        ],
        "Intérprete": [
            "Especialista em traduzir a fala oral em tempo real entre idiomas.",
            "Atua em conferências internacionais, reuniões e eventos globais.",
            "Trabalha dentro de cabines acústicas com fones e microfones.",
            "Realiza tradução simultânea ou consecutiva de discursos.",
        ],
    },
    "Pessoas Famosas": {
        "Cristiano Ronaldo": [
            "Atleta português considerado um dos maiores jogadores da história.",
            "Famoso por sua dedicação física, impulsão e número de gols.",
            "Conhecido pela comemoração icônica gritando 'Siiuu!'.",
            "Venceu a Bola de Ouro múltiplas vezes.",
        ],
        "Lionel Messi": [
            "Lendário jogador argentino de genialidade e controle de bola.",
            "Conquistou a Copa do Mundo de 2022 pela Argentina.",
            "Fez história vestindo a camisa 10 do Barcelona.",
            "Coleciona múltiplos prêmios de melhor jogador do mundo.",
        ],
        "Neymar Jr.": [
            "Jogador brasileiro famoso por seus dribles e habilidade em campo.",
            "Destacou-se no Santos, Barcelona e Seleção Brasileira.",
            "Famoso pelo estilo ousado de jogar futebol.",
            "Gera enorme apelo e engajamento nas redes sociais.",
        ],
        "Kylian Mbappé": [
            "Atacante francês famoso por sua velocidade impressionante.",
            "Foi campeão mundial com a França em 2018 ainda jovem.",
            "Fez hat-trick em uma final de Copa do Mundo.",
            "Considerado um dos maiores astros do futebol atual.",
        ],
        "Erling Haaland": [
            "Centroavante norueguês conhecido por sua força física e faro de gol.",
            "Apelidado de 'Comedor de Gols' por suas marcas impressionantes.",
            "Destacou-se com números avassaladores no futebol inglês.",
            "Famoso por comemorar gols em posição de meditação.",
        ],
        "Vinícius Júnior": [
            "Atacante brasileiro de grande velocidade e drible agressivo.",
            "Revelado pelo Flamengo e destaque no futebol europeu.",
            "Autor de gol do título na final da Liga dos Campeões.",
            "Símbolo importante na luta contra o racismo no esporte.",
        ],
        "Ronaldinho Gaúcho": [
            "Craque brasileiro famoso pelo 'futebol arte' e o 'drible da vaca'.",
            "Conhecido pelo sorriso marcante e pela alegria de jogar.",
            "Foi aplaudido de pé no estádio do rival Real Madrid.",
            "Campeão do mundo em 2002 pela Seleção Brasileira.",
        ],
        "Pelé": [
            "O Rei do Futebol, único jogador a vencer três Copas do Mundo.",
            "Marcou mais de 1000 gols em sua carreira profissional.",
            "Fez história vestindo a camisa do Santos e da Seleção Brasileira.",
            "Considerado o atleta do século XX mundialmente.",
        ],
        "Jude Bellingham": [
            "Jovem meio-campista inglês de enorme talento e presença de área.",
            "Destacou-se com atuações decisivas na Europa em pouca idade.",
            "Comemora seus gols abrindo os braços para a torcida.",
            "Um dos nomes mais valorizados do futebol mundial.",
        ],
        "Mohamed Salah": [
            "Atacante egípcio famoso por sua velocidade e perna esquerda afiada.",
            "Ídolo nacional no Egito e grande astro do futebol inglês.",
            "Conhecido como o 'Rei do Egito' na Inglaterra.",
            "Múltiplas vezes artilheiro do campeonato inglês.",
        ],
        "Lamine Yamal": [
            "Jovem prodígio espanhol que estreou profissionalmente ainda adolescente.",
            "Bateu recordes de precocidade pela Seleção Espanhola.",
            "Famoso pelo drible pela ponta direita e chute colocado.",
            "Comemora fazendo o código postal do seu bairro com as mãos.",
        ],
        "Kaká": [
            "Meio-campista brasileiro famoso por suas arrancadas e elegância.",
            "Eleito o melhor jogador do mundo no ano de 2007.",
            "Campeão do mundo com a Seleção Brasileira em 2002.",
            "Conhecido por sua fé e comemoração apontando para o céu.",
        ],
        "Ronaldo Fenômeno": [
            "Atacante lendário conhecido por suas explosões de velocidade e dribles no goleiro.",
            "Artilheiro e herói do Penta da Seleção Brasileira em 2002.",
            "Eleito três vezes o melhor jogador do mundo.",
            "Jogou por grandes rivais no Brasil e na Espanha.",
        ],
        "David Beckham": [
            "Ex-jogador inglês famoso por seus chutes e cobranças de falta perfeitas.",
            "Ícone de moda e cultura pop mundial além do esporte.",
            "Fez parte da era dos 'Galácticos' na Espanha.",
            "Dono e gestor de clube de futebol nos Estados Unidos.",
        ],
        "Zinedine Zidane": [
            "Lenda do futebol francês famosa pela elegância extrema com a bola.",
            "Campeão do mundo em 1998 marcando gols de cabeça na final.",
            "Autor de um dos gols de voleio mais bonitos da história.",
            "Teve carreira vitoriosa também como treinador.",
        ],
        "Michael Jackson": [
            "Eternizado como o 'Rei do Pop' mundialmente.",
            "Criador do famoso passo de dança 'Moonwalk'.",
            "Dono do álbum mais vendido de todos os tempos, 'Thriller'.",
            "Famoso por suas luvas brilhantes e performances históricas.",
        ],
        "Beyoncé": [
            "Uma das maiores artistas da música pop e R&B de todos os tempos.",
            "Conhecida por performances vocais e coreografias perfeitas.",
            "Fez parte do grupo Destiny's Child antes da carreira solo.",
            "É a artista mais premiada da história do Grammy.",
        ],
        "Rihanna": [
            "Cantora caribenha de grandes sucessos como 'Diamonds' e 'Umbrella'.",
            "Construiu um império milionário no ramo da maquiagem e moda.",
            "Fez uma apresentação marcante no intervalo do Super Bowl.",
            "Famosa por seu estilo único e vocal inconfundível.",
        ],
        "Taylor Swift": [
            "Cantora e compositora de gigantesco sucesso mundial.",
            "Famosa por lotar estádios com sua turnê 'The Eras Tour'.",
            "Transitou do gênero country para o pop dominando as paradas.",
            "Possui uma das fã-bases mais engajadas da música.",
        ],
        "Justin Bieber": [
            "Astro canadense descoberto no YouTube quando criança.",
            "Estourou mundialmente com a música 'Baby'.",
            "Evoluiu do pop teen para estilos como R&B e Pop urbano.",
            "Acompanhado pela mídia desde a sua adolescência.",
        ],
        "The Weeknd": [
            "Cantor canadense de R&B e Pop com visual e sonoridade marcantes.",
            "Dono de sucessos globais como 'Blinding Lights'.",
            "Conhecido por álbuns conceituais e estética cinematográfica.",
            "Fez show solo no intervalo do Super Bowl.",
        ],
        "Eminem": [
            "Um dos rappers mais influentes e de maior venda da história.",
            "Famoso por sua velocidade lírica e rimas complexas.",
            "Protagonizou o filme autobiográfico '8 Mile'.",
            "Conhecido também pelo alter ego 'Slim Shady'.",
        ],
        "Drake": [
            "Rapper canadense que domina as paradas de streaming global.",
            "Mistura rap com R&B e ritmos caribenhos.",
            "Conhecido por lançar dezenas de hits no topo das paradas.",
            "Famoso por bordões e presença forte na cultura pop.",
        ],
        "50 Cent": [
            "Rapper norte-americano icônico dos anos 2000.",
            "Estourou mundialmente com o álbum 'Get Rich or Die Tryin''.",
            "Famoso pelo hit 'In Da Club'.",
            "Tornou-se um empresário de sucesso e produtor de séries.",
        ],
        "Travis Scott": [
            "Rapper e produtor famoso por shows de alta energia e estética própria.",
            "Criador do álbum de enorme sucesso 'Astroworld'.",
            "Possui parcerias icônicas de tênis muito cobiçados.",
            "Pioneiro em realizar um grande show virtual dentro do Fortnite.",
        ],
        "Bruno Mars": [
            "Cantor e performer completo famoso pelo carisma e dança.",
            "Mistura Pop, Funk clássico, R&B e Soul em seus sucessos.",
            "Dono de hits como 'Uptown Funk' e 'Just the Way You Are'.",
            "Famoso por suas apresentações impecáveis ao vivo.",
        ],
        "Anitta": [
            "Cantora brasileira de projeção e carreira internacional.",
            "Atingiu o topo do ranking global do Spotify com a música 'Envolver'.",
            "Famosa por misturar funk carioca com pop e reggaeton.",
            "Conhecida por sua gestão de carreira e empreendedorismo.",
        ],
        "Ludmilla": [
            "Grande nome do funk e do pagode no Brasil.",
            "Criadora do projeto de imenso sucesso 'Numanice'.",
            "Primeira cantora negra afro-latina a alcançar 1 bilhão de streams no Spotify.",
            "Compositora de dezenas de hits nacionais.",
        ],
        "MC Cabelinho": [
            "Artista carioca de destaque no Trap e Funk nacional.",
            "Atuou em novelas de grande audiência na televisão brasileira.",
            "Conhecido por suas letras românticas no estilo 'Trapstar'.",
            "Famoso por seu cabelo platinado e estilo marcante.",
        ],
        "Teto": [
            "Jovem baiano considerado uma das maiores revelações do Trap nacional.",
            "Ganhou prévia popularidade vazando trechos de músicas na internet.",
            "Dono de hits como 'M4' e 'Groupies'.",
            "Conhecido por suas melodias marcantes e agudos.",
        ],
        "KayBlack": [
            "Rapper e compositor de grande sucesso na cena de Trap brasileira.",
            "Conhecido por suas faixas românticas e voz marcante.",
            "Superou milhões de ouvintes mensais com seus EPs.",
            "Irmão de outro artista famoso no cenário do funk/trap.",
        ],
        "Post Malone": [
            "Artista norte-americano que mistura Trap, Pop e Rock.",
            "Dono de grandes hits como 'Sunflower' e 'Circles'.",
            "Famoso por suas muitas tatuagens no rosto e corpo.",
            "Conhecido por sua personalidade carismática e humilde.",
        ],
        "Adele": [
            "Cantora britânica de voz potente e baladas emotivas.",
            "Famosa por nomear seus álbuns com a idade em que os compôs.",
            "Dona de sucessos estrondosos como 'Hello' e 'Rolling in the Deep'.",
            "Vencedora de dezenas de prêmios Grammy e um Oscar.",
        ],
        "Shakira": [
            "Cantora colombiana conhecida mundialmente por sua dança do ventre.",
            "Intérprete da música oficial da Copa de 2010, 'Waka Waka'.",
            "Uma das maiores artistas latinas de todos os tempos.",
            "Mistura Pop com ritmos árabes e latinos em suas músicas.",
        ],
        "Bad Bunny": [
            "Astro porto-riquenho e maior nome do Reggaeton e Trap latino.",
            "Foi o artista mais ouvido do mundo no Spotify por vários anos consecutivos.",
            "Famoso por quebrar barreiras de estilo e moda masculina.",
            "Protagonizou shows gigantescos em estádios pelo mundo.",
        ],
        "Angelina Jolie": [
            "Atriz de Hollywood famosa por papéis como Tomb Raider e Malévola.",
            "Conhecida por seu trabalho humanitário e ativismo social pelo mundo.",
            "Vencedora do Oscar de Melhor Atriz Coadjuvante.",
            "Um dos rostos mais reconhecidos do cinema mundial.",
        ],
        "Brad Pitt": [
            "Astro de Hollywood famoso por filmes como 'Clube da Luta' e 'Troia'.",
            "Vencedor do Oscar como ator e também produtor.",
            "Considerado um dos maiores galãs da história do cinema.",
            "Trabalhou frequentemente com grandes diretores de cinema.",
        ],
        "Leonardo DiCaprio": [
            "Ator consagrado por papéis em 'Titanic' e 'O Lobo de Wall Street'.",
            "Venceu o Oscar de Melhor Ator pelo filme 'O Regresso'.",
            "Conhecido por seu forte engajamento em causas ambientais.",
            "Iniciou a carreira como astro jovem nos anos 90.",
        ],
        "Tom Cruise": [
            "Astro de ação famoso pela franquia 'Missão Impossível'.",
            "Famoso por dispensar dublês e gravar suas próprias cenas perigosas.",
            "Protagonizou o clássico do cinema 'Top Gun'.",
            "Uma das figuras mais duradouras da bilheteria de Hollywood.",
        ],
        "Will Smith": [
            "Ator e rapper famoso por estrelar 'Um Maluco no Pedaço'.",
            "Protagonista de grandes sucessos como 'Homens de Preto' e 'Em Busca da Felicidade'.",
            "Venceu o Oscar de Melhor Ator por interpretar o pai das irmãs Williams.",
            "Conhecido pelo carisma marcante em comédias e dramas.",
        ],
        "Dwayne Johnson": [
            "Conhecido pelo apelido 'The Rock', começou sua carreira no wrestling.",
            "Tornou-se um dos atores mais bem pagos de Hollywood em filmes de ação.",
            "Estrelou diversos filmes da franquia 'Velozes e Furiosos' e 'Jumanji'.",
            "Famoso por seu porte físico impressionante e carisma.",
        ],
        "Johnny Depp": [
            "Ator famoso por interpretar o Capitão Jack Sparrow em 'Piratas do Caribe'.",
            "Conhecido por papéis excêntricos em parcerias com o diretor Tim Burton.",
            "Protagonizou clássicos como 'Edward Mãos de Tesoura'.",
            "Possui um estilo visual marcante e rocker fora das telas.",
        ],
        "Tom Holland": [
            "Ator britânico que interpreta o Homem-Aranha no Universo Marvel.",
            "Famoso por sua habilidade com acrobacias e dança.",
            "Estrelou a adaptação do jogo 'Uncharted' para o cinema.",
            "Conhecido por dar 'spoilers' acidentais em entrevistas.",
        ],
        "Zendaya": [
            "Atriz e ícone de moda famosa por 'Euphoria' e 'Duna'.",
            "Iniciou a carreira no Disney Channel quando jovem.",
            "Venceu o prêmio Emmy de Melhor Atriz em Série Dramática.",
            "Mundialmente aclamada por seus visuais em tapetes vermelhos.",
        ],
        "Scarlett Johansson": [
            "Atriz famosa por interpretar a Viúva Negra no Universo Marvel.",
            "Aclamada por papéis dramáticos em filmes como 'História de um Casamento'.",
            "Uma das atrizes de maior bilheteria da história do cinema.",
            "Atuou desde muito jovem em produções premiadas.",
        ],
        "Margot Robbie": [
            "Atriz australiana que protagonizou o filme de grande sucesso 'Barbie'.",
            "Ganhou destaque internacional no filme 'O Lobo de Wall Street'.",
            "Interpretou a personagem Arlequina em filmes da DC.",
            "Também atua como produtora de cinema bem-sucedida.",
        ],
        "Jenna Ortega": [
            "Atriz que ganhou projeção mundial ao interpretar 'Wandinha' (Wednesday).",
            "Trabalhou em filmes de terror populares como a franquia 'Pânico'.",
            "Começou a atuar ainda criança em séries e produções da TV.",
            "Famosa pela dança icônica que viralizou nas redes sociais.",
        ],
        "Emma Watson": [
            "Ficou famosa mundialmente interpretando Hermione Granger em 'Harry Potter'.",
            "Protagonizou o live-action de 'A Bela e a Fera'.",
            "Ativista e embaixadora da ONU na luta pelos direitos das mulheres.",
            "Formada em Literatura Inglesa por uma universidade renomada.",
        ],
        "Robert Downey Jr.": [
            "Ator consagrado por dar vida ao Homem de Ferro nos cinemas.",
            "Venceu o Oscar por sua atuação marcante no filme 'Oppenheimer'.",
            "Interpretou também o detetive 'Sherlock Holmes' no cinema.",
            "Considerado um dos maiores retornos de carreira de Hollywood.",
        ],
        "Ryan Reynolds": [
            "Ator canadense famoso por interpretar o anti-herói 'Deadpool'.",
            "Conhecido por seu humor sarcástico nas telas e nas redes sociais.",
            "Dono e investidor de empresas e de um clube de futebol britânico.",
            "Estrelou diversas comédias românticas e de ação.",
        ],
        "Jennifer Lawrence": [
            "Atriz que alcançou o estrelato mundial com a franquia 'Jogos Vorazes'.",
            "Venceu o Oscar de Melhor Atriz ainda muito jovem por 'O Lado Bom da Vida'.",
            "Conhecida por sua personalidade autêntica e sem filtros em entrevistas.",
            "Interpretou a mutante Mística nos filmes de 'X-Men'.",
        ],
        "Chris Hemsworth": [
            "Ator australiano famoso por interpretar o Deus do Trovão, Thor, na Marvel.",
            "Conhecido por sua forma física impressionante e treinos de alta intensidade.",
            "Estrelou o filme de ação e resgate 'Extraction' da Netflix.",
            "Famoso pelo carisma e humor em suas produções.",
        ],
        "Keanu Reeves": [
            "Ator canadense amado por papéis icônicos como Neo em 'Matrix' e 'John Wick'.",
            "Famoso por gravar grande parte de suas cenas de ação intensas.",
            "Conhecido por sua simplicidade e atitudes generosas longe dos holofotes.",
            "Possui forte ligação com o universo de artes marciais no cinema.",
        ],
        "Millie Bobby Brown": [
            "Atriz britânica que alcançou a fama mundial interpretando 'Eleven' em 'Stranger Things'.",
            "Protagonizou e produziu os filmes da detetive 'Enola Holmes'.",
            "Tornou-se uma das embaixadoras mais jovens da UNICEF.",
            "Lançou sua própria marca de maquiagem e cuidados com a pele.",
        ],
        "Anne Hathaway": [
            "Atriz premiada famosa por 'O Diabo Veste Prada' e 'O Diário da Princesa'.",
            "Venceu o Oscar de Melhor Atriz Coadjuvante por 'Os Miseráveis'.",
            "Interpretou a Mulher-Gato no filme 'O Cavaleiro das Trevas Ressurge'.",
            "Reconhecida por sua versatilidade em comédias, dramas e musicais.",
        ],
        "MrBeast": [
            "Maior criador do YouTube mundial em número de inscritos.",
            "Famoso por vídeos de desafios extremos e distribuição de grandes prêmios em dinheiro.",
            "Conhecido por projetos filantrópicos gigantescos de plantio de árvores e poços de água.",
            "Criou marcas próprias de chocolates e lanches.",
        ],
        "Virginia Fonseca": [
            "Uma das maiores influenciadoras digitais do Brasil.",
            "Famosa por compartilhar sua rotina diária em família nas redes sociais.",
            "Empresária fundadora de uma linha de cosméticos de grande faturamento.",
            "Apresentadora de programa de auditório na televisão.",
        ],
        "Felipe Neto": [
            "Pioneiro na criação de conteúdo para o YouTube no Brasil.",
            "Construiu um canal gigante voltado para entretenimento e jogos.",
            "Influenciador ativo em debates políticos e sociais nas redes.",
            "Empresário fundador de agências e produtoras de conteúdo.",
        ],
        "Whindersson Nunes": [
            "Humorista e criador de conteúdo que teve um dos maiores canais do Brasil.",
            "Conhecido por seus shows de stand-up comedy lotados pelo país.",
            "Migrou também para o mundo do boxe em lutas exibição internacionais.",
            "Começou gravando vídeos simples no interior do Piauí.",
        ],
        "Kim Kardashian": [
            "Empresária e estrela de reality show que redefiniu a fama digital.",
            "Criadora de uma marca bilionária de roupas modeladoras e cosméticos.",
            "Estudou para se tornar advogada e atua na reforma do sistema prisional.",
            "Uma das personalidades mais seguidas do Instagram no mundo.",
        ],
        "Kylie Jenner": [
            "Empresária mais jovem do clã Kardashian-Jenner.",
            "Construiu um império bilionário no setor de maquiagem e cosméticos.",
            "Uma das personalidades com maior engajamento comercial nas redes.",
            "Ícone de estilo e tendências de beleza para gerações jovens.",
        ],
        "Charli D'Amelio": [
            "Tornou-se uma das maiores personalidades do TikTok com dancinhas virais.",
            "Foi a primeira pessoa a ultrapassar 100 milhões de seguidores na plataforma.",
            "Migrou para o mercado da moda, reality shows e empreendedorismo.",
            "Teve formação em dança desde muito jovem.",
        ],
        "Khaby Lame": [
            "Criador de conteúdo do TikTok mais seguido do planeta.",
            "Famoso por reagir a vídeos complicados de 'lifehacks' de forma simples e sem falar nada.",
            "Possui um gesto icônico com as mãos mostrando o óbvio.",
            "Tornou-se embaixador de grandes marcas de luxo mundiais.",
        ],
        "Lewis Hamilton": [
            "Piloto britânico heptacampeão mundial de Fórmula 1.",
            "Dono dos recordes de mais vitórias e pole positions na história da categoria.",
            "Forte ativista pela diversidade, inclusão e causas ambientais.",
            "Recebeu o título de cidadão honorário do Brasil.",
        ],
        "Max Verstappen": [
            "Piloto holandês prodígio e multicampeão mundial de Fórmula 1.",
            "Conhecido por seu estilo de pilotagem agressivo e determinado.",
            "Tornou-se o piloto mais jovem a estrear e vencer uma corrida na F1.",
            "Domina as pistas correndo pela equipe Red Bull Racing.",
        ],
        "Charles Leclerc": [
            "Piloto monegasco e astro principal da equipe Ferrari na Fórmula 1.",
            "Conhecido por sua velocidade impressionante em voltas de classificação.",
            "Venceu a histórica corrida de casa no Grande Prêmio de Mônaco.",
            "Também toca piano e lança músicas nas plataformas digitais.",
        ],
        "Lando Norris": [
            "Piloto britânico de Fórmula 1 jovem e muito popular na internet.",
            "Famoso por fazer lives de jogos eletrônicos e interagir com fãs.",
            "Piloto titular da tradicional equipe McLaren.",
            "Conhecido por seu humor e estilo de capacetes personalizados.",
        ],
        "Fernando Alonso": [
            "Bicampeão mundial de Fórmula 1 e lenda viva do automobilismo espanhol.",
            "Conhecido por sua longevidade e habilidade de extrair o máximo do carro.",
            "Já competiu nas 500 Milhas de Indianápolis e na 24 Horas de Le Mans.",
            "Um dos pilotos mais experientes de toda a história da F1.",
        ],
        "Oscar Piastri": [
            "Piloto australiano da nova geração de grandes talentos da Fórmula 1.",
            "Campeão consecutivo da Fórmula 3 e Fórmula 2 antes de chegar à F1.",
            "Conhecido por sua calma e frieza sob pressão nas corridas.",
            "Piloto de destaque na equipe McLaren.",
        ],
        "Ayrton Senna": [
            "Lendário tricampeão mundial de Fórmula 1 e herói nacional do Brasil.",
            "Famoso por seu domínio absoluto em pistas molhadas e voltas rápidas.",
            "Dono do capacete amarelo mais icônico da história do esporte.",
            "Sua memória vive através do instituto que apoia a educação infantil.",
        ],
        "Michael Schumacher": [
            "Lenda alemã e heptacampeão mundial de Fórmula 1.",
            "Marcou época dominando a categoria e fazendo história na Ferrari.",
            "Conhecido por sua ética de trabalho e preparo físico impecável.",
            "Um dos maiores nomes de todos os tempos no esporte a motor.",
        ],
        "Sebastian Vettel": [
            "Tetracampeão mundial de Fórmula 1 pela equipe Red Bull.",
            "O campeão mundial mais jovem da história da categoria.",
            "Conhecido por baptizar seus carros de corrida com nomes femininos.",
            "Notabilizou-se por seu forte ativismo ambiental e social nos últimos anos.",
        ],
        "George Russell": [
            "Piloto britânico de Fórmula 1 integrante da equipe Mercedes.",
            "Passou pela academia de jovens pilotos até chegar ao time principal.",
            "Conhecido pela precisão nas corridas e postura profissional.",
            "Apelidado carinhosamente de 'Mr. Saturday' por seu desempenho aos sábados.",
        ],
    },
        "Marcas": {
        "Nike": [
            "É uma marca de produtos esportivos famosa no mundo todo.",
            "Seu símbolo lembra um cheque ou verificação visual.",
            "Produz tênis, roupas e acessórios esportivos.",
            "Patrocina grandes atletas e clubes de futebol.",
        ],
        "Adidas": [
            "Famosa marca esportiva alemã reconhecida mundialmente.",
            "Seu logotipo clássico é composto por três listras paralelas.",
            "Fabricante de tênis, uniformes esportivos e acessórios.",
            "Patrocina grandes eventos de futebol e seleções mundiais.",
        ],
        "Puma": [
            "Empresa alemã que produz artigos e vestuário esportivo.",
            "Seu logotipo exibe a silhueta de um felino saltando.",
            "Famosa por parcerias com atletas de velocidade e times de futebol.",
            "Conhecida por seus tênis e roupas com design esportivo e casual.",
        ],
        "Gucci": [
            "Grife de luxo italiana famosa no mundo da alta moda.",
            "Seu logotipo icônico possui duas letras 'G' entrelaçadas.",
            "Conhecida por bolsas, roupas, cintos e acessórios de alto valor.",
            "Utiliza frequentemente as cores verde e vermelho em seus designs.",
        ],
        "Zara": [
            "Rede espanhola de lojas de roupas e moda rápida (fast-fashion).",
            "Famosa por lançar tendências de moda a preços acessíveis.",
            "Possui lojas em shoppings e centros comerciais por todo o mundo.",
            "Oferece coleções masculinas, femininas e infantis.",
        ],
        "Toyota": [
            "Fabricante japonesa de veículos conhecida pela confiabilidade.",
            "Seu logotipo é formado por elipses ovais sobrepostas.",
            "Pioneira na produção em massa de carros híbridos e elétricos.",
            "Criadora de modelos mundialmente famosos como o Corolla e a Hilux.",
        ],
        "BMW": [
            "Fabricante alemã de automóveis e motocicletas de luxo.",
            "Seu logotipo redondo possui setores azuis e brancos que remetem à Baviera.",
            "Famosa por seus carros esportivos e executivos de alto desempenho.",
            "Conhecida pelo slogan focado no prazer de dirigir.",
        ],
        "Mercedes-Benz": [
            "Uma das marcas de carros mais antigas e prestigiadas do mundo.",
            "Seu logotipo icônico é uma estrela de três pontas dentro de um círculo.",
            "Produz veículos executivos de luxo, ônibus e caminhões.",
            "Possui forte presença e história na Fórmula 1.",
        ],
        "Ferrari": [
            "Lendária fabricante italiana de carros esportivos e superesportivos.",
            "Seu logotipo apresenta um cavalo empinado sobre um fundo amarelo.",
            "Sua cor mais tradicional e famosa é o vermelho vibrante.",
            "Equipe histórica e extremamente vitoriosa na Fórmula 1.",
        ],
        "Ford": [
            "Uma das empresas pioneiras na indústria automobilística mundial.",
            "Seu logotipo clássico é um óvalo azul com o nome escrito em caligrafia.",
            "Revolucionou a fabricação de veículos com a linha de montagem.",
            "Famosa por modelos históricos como o Mustang e picapes icônicas.",
        ],
        "Apple": [
            "É uma gigante de tecnologia e inovação.",
            "Seu logotipo é uma maçã com uma mordida.",
            "Conhecida por celulares, computadores e tablets de alto padrão.",
            "Possui um sistema operacional próprio e exclusivo.",
        ],
        "Samsung": [
            "Gigante sul-coreana de tecnologia e eletrônicos de consumo.",
            "Fabricante global de smartphones, televisores e eletrodomésticos.",
            "Líder de vendas no mercado mundial de celulares Android.",
            "Possui um logotipo azul com o nome da empresa em destaque.",
        ],
        "Microsoft": [
            "Uma das maiores empresas de software e tecnologia do mundo.",
            "Seu logotipo é composto por quatro quadrados coloridos formando uma janela.",
            "Desenvolvedora do sistema operacional Windows e do pacote Office.",
            "Criadora do console de jogos Xbox.",
        ],
        "Xiaomi": [
            "Empresa chinesa de tecnologia conhecida pelo excelente custo-benefício.",
            "Seu logotipo apresenta as letras 'Mi' brancas em um quadrado laranja.",
            "Famosa por seus smartphones, pulseiras inteligentes e aparelhos conectados.",
            "Possui um ecossistema gigante de produtos eletrônicos para casa.",
        ],
        "Nestlé": [
            "Maior empresa de alimentos e bebidas do mundo, de origem suíça.",
            "Seu logotipo representa passarinhos em um ninho.",
            "Fabricante de chocolates, leites, cafés e cereais matinais.",
            "Dona de marcas famosas como KitKat, Nescau e Nespresso.",
        ],
        "Coca-Cola": [
            "Uma das marcas de refrigerante mais valiosas e conhecidas do planeta.",
            "Seu logotipo possui uma caligrafia vermelha e branca inconfundível.",
            "Famosa por suas campanhas publicitárias e pela garrafa de vidro clássica.",
            "A bebida escura e gaseificada é vendida em quase todos os países.",
        ],
        "Pepsi": [
            "Famosa marca global de refrigerante de cola.",
            "Seu logotipo é um círculo dividido com cores azul, branca e vermelha.",
            "Sua principal concorrente histórica é a Coca-Cola.",
            "Patrocina grandes eventos esportivos e de entretenimento.",
        ],
        "McDonald's": [
            "Rede de lanchonetes de fast-food mais famosa do mundo.",
            "Seu logotipo é composto pelos icônicos 'Arcos Dourados' em forma de M.",
            "Famosa por sanduíches como o Big Mac e por suas batatas fritas.",
            "Presente em centenas de países com atendimento rápido e drive-thru.",
        ],
        "Honda": [
            "Multinacional japonesa famosa por seus carros, motocicletas e motores.",
            "Seu logotipo para carros utiliza uma letra 'H' estilizada.",
            "Uma das maiores fabricantes de motos e veículos confiáveis do mundo.",
            "Fabricante de modelos icônicos como o Civic e a moto CG.",
        ],
        "Yamaha": [
            "Empresa japonesa famosa por motocicletas e instrumentos musicais.",
            "Seu logotipo exibe três diapagões cruzados em um círculo.",
            "Competidora de destaque em campeonatos mundiais de motovelocidade.",
            "Produz desde motos de alta cilindrada até pianos e teclados.",
        ],
        "Ducati": [
            "Famosa fabricante italiana de motocicletas de alto desempenho.",
            "Suas motos são reconhecidas pelo design agressivo e pela cor vermelha.",
            "Destaca-se pelo uso de motores com tecnologia desmodrômica.",
            "Possui forte tradição e títulos na categoria MotoGP.",
        ],
        "Kawasaki": [
            "Fabricante japonesa de motocicletas de grande porte e alta performance.",
            "Sua cor de identidade visual mais famosa é o verde lima.",
            "Conhecida mundialmente pela linha de motos esportivas 'Ninja'.",
            "Também produz jet-skis, quadriciclos e motores industriais.",
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
        "Superman": [
            "Herói alienígena vindo do planeta Krypton.",
            "Possui superpoderes como voo, superforça e visão de raio-X.",
            "Trabalha como repórter em um jornal quando não está salvando o mundo.",
            "Sua principal fraqueza é a radiação da Kryptonita.",
        ],
        "Mulher-Maravilha": [
            "Princesa amazona e guerreira imortal da Ilha Paraíso.",
            "Utiliza braceletes defletores, um laço mágico e uma tiara.",
            "Foi criada na mitologia grega e luta pela paz e justiça.",
            "Possui força sobre-humana e a habilidade de voar.",
        ],
        "Flash": [
            "Herói conhecido como o homem mais rápido do vivo.",
            "Conectado à Força de Aceleração após um acidente científico.",
            "Capaz de correr tão rápido que pode viajar no tempo e entre dimensões.",
            "Usa um traje vermelho com um raio dourado no peito.",
        ],
        "Lanterna Verde": [
            "Membro de uma força policial intergaláctica mantida pelos Guardiões do Universo.",
            "Usa um anel energético que cria qualquer coisa que sua imaginação puder conceber.",
            "Sua maior arma é a força de vontade.",
            "Faz parte de uma tropa que veste uniformes verdes e pretos.",
        ],
        "Aquaman": [
            "Rei de Atlântida e soberano dos oceanos.",
            "Pode respirar debaixo d'água, nadar em alta velocidade e se comunicar com a vida marinha.",
            "Usa um tridente dourado como sua arma principal.",
            "Divide sua vida entre a superfície e o reino submarino.",
        ],
        "Homem de Ferro": [
            "Gênio, bilionário, playboy e filantropo.",
            "Criou uma armadura tecnológica avançada equipada com armas e propulsores para combater o crime.",
            "Sua identidade secreta é amplamente conhecida pelo mundo.",
            "É um dos fundadores e principais líderes dos Vingadores.",
        ],
        "Capitão América": [
            "Super-soldado da Segunda Guerra Mundial aprimorado por um soro experimental.",
            "Usa um escudo indestrutível feito de vibranium.",
            "Ficou congelado em gelo por décadas antes de acordar no mundo moderno.",
            "É conhecido por seu forte senso de moralidade e liderança exemplar.",
        ],
        "Thor": [
            "Deus do Trovão originário da mitologia nórdica e do reino de Asgard.",
            "Manipula raios, tempestades e possui força sobre-humana.",
            "Usa um martelo místico chamado Mjolnir (ou o machado Rompe-Tormentas).",
            "Gosta de batalhar com honra e valoriza muito seus amigos.",
        ],
        "Pantera Negra": [
            "Rei e protetor da nação tecnologicamente avançada de Wakanda.",
            "Seu traje é feito de vibranium e possui garras retráteis.",
            "Recebeu força e agilidade sobre-humanas ao consumir a Erva em Forma de Coração.",
            "Lidera uma das nações mais secretas e poderosas do mundo.",
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
        "Roblox": [
            "Plataforma online onde os usuários podem criar e jogar seus próprios jogos.",
            "Os avatares e mundos são formados por blocos e formas tridimensionais.",
            "Possui milhares de minigames de diferentes estilos criados pela comunidade.",
            "É extremamente popular entre o público jovem.",
        ],
        "Fortnite": [
            "Jogo do gênero Battle Royale onde 100 jogadores lutam para ser o último sobrevivente.",
            "Permite coletar materiais para construir paredes e rampas rapidamente durante o combate.",
            "Famoso por suas danças comemorativas (emotes) e eventos ao vivo.",
            "Possui um estilo visual colorido e skins de vários universos da cultura pop.",
        ],
        "Pokémon": [
            "Franquia onde os jogadores capturam e treinam criaturas com poderes especiais.",
            "O objetivo principal é colecioná-los e derrotar os líderes de ginásio.",
            "O mascote mais famoso e conhecido mundialmente é o Pikachu.",
            "A frase clássica dos treinadores é 'Temos que pegar todos!'.",
        ],
        "Grand Theft Auto": [
            "Série de jogos de mundo aberto focada em crime, missões e direção de veículos.",
            "Permite explorar cidades fictícias inspiradas em locais reais dos Estados Unidos.",
            "Oferece grande liberdade de ação aos jogadores em um ambiente urbano.",
            "Um dos títulos mais famosos e influentes da história dos videogames.",
        ],
        "League of Legends": [
            "Jogo do gênero MOBA onde duas equipes de cinco jogadores se enfrentam.",
            "O objetivo principal é destruir a base inimiga (o Nexus).",
            "Cada jogador controla um campeão único com habilidades especiais.",
            "É um dos maiores e mais populares eSports do mundo.",
        ],
        "Zelda": [
            "Franquia de aventura e exploração da Nintendo.",
            "O protagonista heróico que usa túnica verde se chama Link.",
            "A missão principal costuma envolver salvar a Princesa Zelda e o reino de Hyrule.",
            "Mistura quebra-cabeças, exploração de masmorras e combates com espada.",
        ],
        "Sonic": [
            "Famoso ouriço azul criado pela SEGA.",
            "Sua principal característica é a velocidade supersônica.",
            "Passa os níveis coletando anéis dourados e derrotando o Doutor Eggman.",
            "Um dos maiores clássicos dos jogos de plataforma.",
        ],
        "Among Us": [
            "Jogo multiplayer de dedução social em uma nave espacial.",
            "A tripulação deve realizar tarefas enquanto tenta descobrir quem são os impostores.",
            "Os impostores precisam sabotar a nave e eliminar os tripulantes em segredo.",
            "Famoso pelas reuniões de emergência para debater quem é suspeito.",
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
        "Tornado": [
            "Coluna de ar em rotação violenta e rápida que toca o solo.",
            "Forma um funil escuro conectado a uma nuvem de tempestade.",
            "Possui ventos extremamente destrutivos capazes de arrancar árvores e casas.",
            "É frequente em regiões como o centro dos Estados Unidos.",
        ],
        "Tsunami": [
            "Grande série de ondas oceânicas gigantescas causadas por perturbações subaquáticas.",
            "Geralmente originado por terremotos ou erupções vulcânicas no fundo do mar.",
            "Perde velocidade mas ganha altura colossal ao se aproximar da costa.",
            "Pode causar inundações catastróficas nas regiões litorâneas.",
        ],
        "Aurora Boreal": [
            "Espetáculo de luzes coloridas visível nos céus das regiões polares.",
            "Causado pela interação de partículas solares com o campo magnético da Terra.",
            "Exibe tons brilhantes de verde, rosa, roxo e azul dançando no céu noturno.",
            "Também conhecida como luz do norte.",
        ],
        "Terremoto": [
            "Tremor violento da superfície da Terra causado pelo movimento de placas tectônicas.",
            "Pode destruir edifícios inteiros e alterar a paisagem em segundos.",
            "Sua intensidade é frequentemente medida na escala Richter.",
            "Pode dar origem a ondas gigantes se ocorrer no oceano.",
        ],
        "Furacão": [
            "Gigantesca tempestade tropical com ventos extremamente fortes e chuvas torrenciais.",
            "Possui uma área central calma conhecida como 'olho' da tempestade.",
            "Forma-se sobre águas oceânicas quentes e perde força ao atingir a terra firme.",
            "Gera ondas imensas e inundações severas nas regiões costeiras.",
        ],
        "Avalanche": [
            "Queda rápida e massiva de neve, gelo e rochas encosta abaixo em uma montanha.",
            "Geralmente desencadeada por vibrações, ventos fortes ou excesso de peso na neve.",
            "Pode soterrar trilhas, estradas e esquiadores em poucos segundos.",
            "Comum em cordilheiras de grande altitude durante o inverno.",
        ],
    },
}

# Inicialização dos estados na sessão do Streamlit
if "estado" not in st.session_state:
    st.session_state.estado = "CONFIGURACAO"
if "num_jogadores" not in st.session_state:
    st.session_state.num_jogadores = 4
if "num_impostores" not in st.session_state:
    st.session_state.num_impostores = 1
if "categoria_selecionada" not in st.session_state:
    st.session_state.categoria_selecionada = "Comidas & Bebidas"
if "palavra_secreta" not in st.session_state:
    st.session_state.palavra_secreta = ""
if "impostores_indices" not in st.session_state:
    st.session_state.impostores_indices = []
if "dicas_impostores" not in st.session_state:
    st.session_state.dicas_impostores = {}
if "jogador_atual" not in st.session_state:
    st.session_state.jogador_atual = 0
if "revelado" not in st.session_state:
    st.session_state.revelado = False
if "nomes_jogadores" not in st.session_state:
    st.session_state.nomes_jogadores = []

# ---------------------------------------------------------
# TELA 1: CONFIGURAÇÃO DO JOGO (NÚMEROS E NOMES)
# ---------------------------------------------------------
if st.session_state.estado == "CONFIGURACAO":
    st.header("⚙️ Configurações da Partida")

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

    st.markdown("### ✏️ Insira o Nome dos Jogadores")
    nomes_temp = []
    for i in range(int(num_jogadores)):
        nome_padrao = (
            st.session_state.nomes_jogadores[i]
            if i < len(st.session_state.nomes_jogadores)
            else f"Jogador {i+1}"
        )
        nome = st.text_input(f"Nome do Jogador {i+1}:", value=nome_padrao, key=f"nome_{i}")
        nomes_temp.append(nome.strip() if nome.strip() else f"Jogador {i+1}")

    st.markdown("---")
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
        st.session_state.nomes_jogadores = nomes_temp

        cat = st.session_state.categoria_selecionada
        palavra = random.choice(list(CATEGORIAS[cat].keys()))
        st.session_state.palavra_secreta = palavra

        # Sorteia os índices dos impostores (0 até num_jogadores - 1)
        todos_indices = list(range(st.session_state.num_jogadores))
        impostores_idx = random.sample(
            todos_indices, st.session_state.num_impostores
        )
        st.session_state.impostores_indices = impostores_idx

        # Sorteia dicas diferentes para cada impostor
        dicas_disponiveis = CATEGORIAS[cat][palavra].copy()
        random.shuffle(dicas_disponiveis)

        st.session_state.dicas_impostores = {}
        for count, idx in enumerate(impostores_idx):
            dica_atribuida = dicas_disponiveis[count % len(dicas_disponiveis)]
            st.session_state.dicas_impostores[idx] = dica_atribuida

        st.session_state.jogador_atual = 0
        st.session_state.revelado = False
        st.session_state.estado = "DISTRIBUICAO"
        st.rerun()

# ---------------------------------------------------------
# TELA 2: REVELAÇÃO DOS PAPÉIS (PASSE O DISPOSITIVO)
# ---------------------------------------------------------
elif st.session_state.estado == "DISTRIBUICAO":
    idx_atual = st.session_state.jogador_atual
    nome_atual = st.session_state.nomes_jogadores[idx_atual]
    total = st.session_state.num_jogadores

    st.header(f"👤 Vez de: **{nome_atual}** ({idx_atual + 1} de {total})")

    if not st.session_state.revelado:
        st.info(f"Passe o dispositivo para **{nome_atual}**.")
        if st.button(f"👁️ Ver Meu Papel ({nome_atual})", use_container_width=True):
            st.session_state.revelado = True
            st.rerun()
    else:
        # Se for um dos impostores
        if idx_atual in st.session_state.impostores_indices:
            st.error("🚨 **VOCÊ É UM IMPOSTOR!** 🚨")

            dica = st.session_state.dicas_impostores.get(
                idx_atual, "Pense em algo relacionado à categoria."
            )
            st.warning(f"💡 **Sua dica secreta:** *{dica}*")

            st.write(
                "Use essa dica com cuidado para dar uma pista sutil sem revelar que não sabe a palavra exata!"
            )

            if st.session_state.num_impostores > 1:
                parceiros = [
                    st.session_state.nomes_jogadores[i]
                    for i in st.session_state.impostores_indices
                    if i != idx_atual
                ]
                st.write(
                    f"🤝 **Seu(s) parceiro(s) impostor(es):** {', '.join(parceiros)}"
                )

        # Se for inocente
        else:
            st.success(
                f"🔑 A palavra secreta é: **{st.session_state.palavra_secreta}**"
            )
            st.write("Sua missão: Dê uma pista sutil sobre a palavra!")

        st.markdown("---")

        if idx_atual < total - 1:
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
    3. **Votação:** Ao sinal de todos, apontem para quem acham ser o impostor!
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

    nomes_impostores = [
        st.session_state.nomes_jogadores[i]
        for i in sorted(st.session_state.impostores_indices)
    ]
    impostores_str = ", ".join(nomes_impostores)

    st.error(f"🤫 O(s) Impostor(es) era(m): **{impostores_str}**")
    st.success(
        f"🔑 A palavra secreta era: **{st.session_state.palavra_secreta}**"
    )

    st.markdown("---")

    if st.button("🔄 Jogar Novamente", use_container_width=True):
        st.session_state.estado = "CONFIGURACAO"
        st.rerun()