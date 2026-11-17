#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_all_recipes.py
Generates 20 recipe markdown files, downloads their images,
updates mkdocs.yml navigation and lista.js TODAS_RECEITAS array.
"""
import sys, os, re, urllib.request
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
IMGS_DIR = os.path.join(DOCS_DIR, 'imagens')
PP_DIR   = os.path.join(DOCS_DIR, 'pratos-principais')
SO_DIR   = os.path.join(DOCS_DIR, 'sopas')
SB_DIR   = os.path.join(DOCS_DIR, 'sobremesas')
CDN      = "https://cdn.albo.inc/file/sortd-images-kq4508yjh/"

RECIPES = [
    # ─── PRATOS PRINCIPAIS ───────────────────────────────────────────────────
    {
        'slug': 'noodles-curry-coco',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '82e59aa2-ba35-49ab-930d-49fa6b86471d.jpg',
        'nav_title':  'Noodles de Curry com Leite de Coco',
        'lista_nome': 'Noodles de Curry com Leite de Coco',
        'content': r"""# Noodles de Curry com Leite de Coco numa Frigideira

![Noodles de Curry com Leite de Coco numa Frigideira](../imagens/82e59aa2-ba35-49ab-930d-49fa6b86471d.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Fusão Asiática
- Dificuldade: Fácil

## Ingredientes

- 120 g de noodles de arroz grossos
- ½ chávena de cenoura às fatias
- ½ chávena de brócolos picados
- ½ chávena de pimento vermelho cortado em tiras
- ½ chávena de edamame
- ¼ chávena de cajus
- 2 dentes de alho, picados
- 1 colher de sopa de molho de soja
- 1 colher de chá de caril em pó
- ½ colher de chá de pimenta preta moída
- ½ colher de chá de paprika
- ½ colher de chá de cominhos em pó
- ¼ colher de chá de flocos de malagueta
- ½ chávena de caldo de legumes
- ¾ chávena de leite de coco

## Preparação

1. **Numa frigideira grande**, coloque os noodles, a cenoura, os brócolos, o pimento, o edamame, os cajus e o alho.
2. **Adicione as especiarias**: o molho de soja, o caril, a pimenta, a paprika, os cominhos e os flocos de malagueta.
3. **Verta** o caldo de legumes e o leite de coco sobre todos os ingredientes.
4. **Tape a frigideira** e cozinhe em lume médio durante 10 minutos, mexendo a meio do tempo.
5. **Sirva** de imediato, decorado com salsa fresca picada e cajus extra.
""",
    },
    {
        'slug': 'feijoes-miso-verde',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '957111ee-9a99-4163-920f-343279b12236.jpg',
        'nav_title':  'Feijões com Miso, Tahine e Sementes Tostadas',
        'lista_nome': 'Feijões com Miso, Tahine e Sementes Tostadas',
        'content': r"""# Feijões com Miso, Tahine e Sementes Tostadas

![Feijões com Miso, Tahine e Sementes Tostadas](../imagens/957111ee-9a99-4163-920f-343279b12236.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Fusão Asiática
- Dificuldade: Fácil

## Ingredientes

- 2 mãos grandes de couve-negra, sem talos, grosseiramente picada
- 2 alhos-franceses grandes, cortados em meias-luas finas
- 3 latas de 400 g de feijões manteiga (guardar a água de conserva se forem biológicos; caso contrário usar 250 ml de caldo de legumes)
- 6 dentes de alho, picados finamente
- 100 g de tofu sedoso
- 50 g de cajus, demolhados em água quente por 10 minutos
- 2 colheres de sopa de levedura nutricional
- 2 colheres de sopa de pasta de miso branco
- 1 colher de chá de coentros em pó
- 1 colher de chá de cominhos em pó
- Pimenta preta moída a gosto

### Para o Molho de Tahine

- 2 colheres de sopa de tahine fluido
- 1 colher de sopa e meia de sumo de limão fresco
- 1 a 3 colheres de sopa de água para diluir

### Para Servir

- 3 colheres de sopa de sementes de abóbora, tostadas com sal marinho
- Sementes de sésamo a gosto
- Fio de azeite
- Torradas de pão de massa mãe

## Preparação

1. **Numa frigideira grande** em lume médio, adicione um fio de azeite. Junte o alho-francês e refogue durante 5 minutos até ficar macio e translúcido.
2. **Adicione o alho** picado e cozinhe por mais 2 minutos, mexendo sempre.
3. **Junte os coentros e os cominhos** em pó. Mexa bem para tostar as especiarias durante 1 minuto.
4. **Adicione os feijões manteiga** com a sua água de conserva (ou o caldo de legumes). Leve a lume brando por 5 minutos.
5. **Prepare o creme**: triture o tofu sedoso com os cajus demolhados e escorridos e a levedura nutricional até obter um creme homogéneo.
6. **Junte o creme** à frigideira e mexa suavemente. Cozinhe por mais 5 minutos em lume brando.
7. **Desligue o lume** e incorpore a pasta de miso (nunca ferva o miso para preservar as suas propriedades). Mexa até dissolver completamente.
8. **Adicione a couve-negra**, tape a frigideira e cozinhe por 3 a 4 minutos até ficar macia mas ainda verde e vibrante. Tempere com pimenta preta.
9. **Para o molho de tahine**: misture o tahine com o sumo de limão e adicione a água aos poucos até obter um molho suave e fluido.
10. **Sirva** sobre torradas de massa mãe. Regue com o molho de tahine e polvilhe com as sementes de abóbora tostadas e sésamo. Termine com um fio de azeite.
""",
    },
    {
        'slug': 'arroz-abobora-cogumelos-roma',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '388d67a5-823f-4b47-890d-8a3a2f251235.jpg',
        'nav_title':  'Arroz de Abóbora, Cogumelos e Romã',
        'lista_nome': 'Arroz de Abóbora, Cogumelos e Romã',
        'content': r"""# Arroz de Abóbora, Cogumelos e Romã

![Arroz de Abóbora, Cogumelos e Romã](../imagens/388d67a5-823f-4b47-890d-8a3a2f251235.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Portuguesa
- Dificuldade: Médio

## Ingredientes

- 2 chávenas de arroz vaporizado
- 1 cebola grande, laminada
- 4 dentes de alho
- 2 folhas de louro
- 200 g de cogumelos marron, picados
- Azeite q.b.
- ⅓ chávena de vinho tinto
- 1 abóbora-manteiga média
- 1 ramo de alecrim fresco
- 100 g de cogumelos shiitake
- 100 g de cogumelos pleurotus
- 1 mão de amêndoas
- Sementes de romã q.b.

### Especiarias para o Arroz

- 2 colheres de chá de colorau
- ½ colher de chá de gengibre em pó
- Noz-moscada a gosto
- Pimenta preta a gosto
- Sal a gosto

### Tempero para o Topping

- 1 colher de sopa de melaço de romã (ou 1 c.s. de vinagre balsâmico + ½ c.s. de xarope de agave)
- 1 colher de chá de paprika fumada
- 1 colher de chá de alho em pó
- Sal a gosto

## Preparação

1. **Num tacho**, refogue a cebola laminada com o alho e as folhas de louro em azeite, em lume médio, durante 5 minutos.
2. **Adicione os cogumelos marron** picados e deixe caramelizar bem, mexendo regularmente, por 8 a 10 minutos.
3. **Corte a abóbora-manteiga** em cubos pequenos. Junte metade ao tacho, adicione as especiarias e o vinho tinto. Deixe estufar em lume brando até a abóbora ficar macia, cerca de 10 minutos.
4. **Adicione o arroz**, o dobro da água e o ramo de alecrim. Tape e deixe cozer completamente.
5. **Transfira o arroz** para uma travessa de forno. Disponha por cima o restante da abóbora, os cogumelos shiitake, os pleurotus e as amêndoas.
6. **Numa tigela**, misture os ingredientes do tempero do topping e regue os legumes por cima.
7. **Leve ao forno** a 200°C até os legumes ficarem dourados e estaladiços, cerca de 20 minutos.
8. **Sirva** com sementes de romã fresca por cima.
""",
    },
    {
        'slug': 'gnocchi-cremoso-abobora',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '662977a6-8e27-4ba1-8531-cae9e2ab503d.jpg',
        'nav_title':  'Gnocchi Cremoso com Abóbora',
        'lista_nome': 'Gnocchi Cremoso com Abóbora',
        'content': r"""# Gnocchi Cremoso com Abóbora

![Gnocchi Cremoso com Abóbora](../imagens/662977a6-8e27-4ba1-8531-cae9e2ab503d.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Italiana
- Dificuldade: Fácil

## Ingredientes

- 500 g de gnocchi (de compra ou caseiros)
- ½ chávena de puré de abóbora (em lata ou caseiro)
- 1 chávena de natas de coco
- 2 colheres de sopa de levedura nutricional
- 2 dentes de alho, picados
- 2 colheres de sopa de manteiga vegetal
- 1 colher de chá de paprika fumada
- 1 colher de chá de cebolinho seco
- ½ colher de chá de alho em pó
- ½ colher de chá de cebola em pó
- ½ colher de chá de mistura de ervas italianas
- ½ colher de chá de noz-moscada
- Sal e pimenta a gosto
- Flocos de malagueta (opcional)
- Levedura nutricional extra para polvilhar

## Preparação

1. **Coza o gnocchi** de acordo com as instruções da embalagem. Escorra e reserve, guardando um pouco da água de cozedura.
2. **Numa frigideira grande**, derreta a manteiga vegetal em lume médio. Adicione o alho picado e cozinhe por 1 a 2 minutos até ficar dourado e perfumado.
3. **Adicione o puré de abóbora** e mexa bem para combinar com o alho.
4. **Verta as natas de coco** e adicione a levedura nutricional. Mexa para incorporar.
5. **Tempere** com a paprika, o cebolinho, o alho em pó, a cebola em pó, as ervas italianas e a noz-moscada. Mexa bem.
6. **Junte o gnocchi** cozido à frigideira e envolva cuidadosamente no molho. Se o molho estiver demasiado espesso, adicione um pouco da água de cozedura do gnocchi.
7. **Ajuste** o sal e a pimenta a gosto.
8. **Sirva** de imediato, polvilhado com levedura nutricional e flocos de malagueta a gosto.
""",
    },
    {
        'slug': 'feijoes-brancos-toscana',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  'ddc02ce2-e43a-4c98-8d83-5967f5a1a111.jpg',
        'nav_title':  'Feijões Brancos Cremosos à Toscana',
        'lista_nome': 'Feijões Brancos Cremosos à Toscana',
        'content': r"""# Feijões Brancos Cremosos à Toscana

![Feijões Brancos Cremosos à Toscana](../imagens/ddc02ce2-e43a-4c98-8d83-5967f5a1a111.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Italiana
- Dificuldade: Fácil

## Ingredientes

- 2 latas de 400 g de feijões brancos (cannellini ou Great Northern), escorridos e lavados
- 1 ½ chávenas de tomates cherry, cortados ao meio
- ⅓ chávena de tomates secos, picados
- 1 cebola pequena amarela, cortada em cubinhos
- 4 dentes de alho, picados finamente
- 1 colher de sopa de azeite
- 1 colher de chá de mistura de ervas italianas
- ½ colher de chá de paprika fumada
- ¼ colher de chá de flocos de malagueta, a gosto
- 1 colher de sopa de farinha
- 1 ½ chávenas de caldo de legumes
- ½ chávena de leite de soja sem açúcar
- 1 colher de chá de mostarda de Dijon
- 2 colheres de sopa de queijo vegano ralado (ou levedura nutricional)
- 2 a 3 chávenas de couve-portuguesa picada, sem talos duros
- 1 colher de sopa de sumo de limão
- 1 colher de chá de xarope de ácer
- ½ colher de chá de pimenta preta moída
- Sal a gosto
- Azeite extra virgem para finalizar
- Pão rústico torrado para acompanhar

## Preparação

1. **Aqueça** uma frigideira em lume médio. Adicione o azeite e a cebola em cubinhos com uma pitada de sal. Cozinhe por 4 a 5 minutos, mexendo ocasionalmente, até ficar macia e ligeiramente dourada.
2. **Adicione os tomates cherry** cortados ao meio e cozinhe por 3 a 4 minutos, mexendo ocasionalmente, até ficarem estufados e a começar a desfazer. Reserve alguns tomates blistados para decorar.
3. **Junte o alho** e os tomates secos. Cozinhe por 30 a 60 segundos até ficar perfumado.
4. **Adicione as ervas italianas**, a paprika, os flocos de malagueta e a pimenta preta. Mexa bem.
5. **Polvilhe com a farinha** e mexa durante cerca de 30 segundos. Verta o caldo de legumes aos poucos enquanto mexe, seguido do leite de soja e da mostarda.
6. **Leve a um suave ferver** e cozinhe por 2 a 3 minutos, mexendo, até engrossar ligeiramente.
7. **Adicione os feijões** e cozinhe em lume brando por 5 a 7 minutos. Esmague cerca de ⅓ dos feijões contra a lateral da frigideira com as costas de uma colher para engrossar o molho.
8. **Junte a couve-portuguesa**, tape e cozinhe por 3 a 5 minutos, mexendo uma ou duas vezes, até ficar macia mas ainda vibrante.
9. **Reduza o lume** e incorpore o queijo vegano ralado (ou levedura nutricional) até derreter e o molho ficar brilhante.
10. **Adicione o sumo de limão** e o xarope de ácer. Prove e ajuste o sal, a pimenta e os flocos de malagueta.
11. **Sirva** com os tomates blistados reservados por cima, um fio de azeite extra virgem e pão rústico torrado para acompanhar.
""",
    },
    {
        'slug': 'estrogonofe-grao-de-bico',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  'ec937e3d-bb1c-4847-a988-3ce85a7a0f1b.jpg',
        'nav_title':  'Estrogonofe de Grão-de-Bico',
        'lista_nome': 'Estrogonofe de Grão-de-Bico',
        'content': r"""# Estrogonofe de Grão-de-Bico

![Estrogonofe de Grão-de-Bico](../imagens/ec937e3d-bb1c-4847-a988-3ce85a7a0f1b.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Fusão
- Dificuldade: Fácil

## Ingredientes

- 200 g de grão-de-bico cru (demolhar em água por 24h, trocando a água a meio)
- ½ cebola, picada
- 3 dentes de alho, picados
- 1 colher de sopa de óleo
- 200 a 250 g de cogumelos paris (ou portobello), fatiados
- 250 ml de polpa de tomate
- 2 colheres de sopa de mostarda
- Sal a gosto

### Para o Creme Branco Vegano

- 100 g de tofu firme
- ¼ chávena de cajus (demolhados em água por 2 horas)
- 200 ml de água (adicionar mais se necessário)
- 1 colher de sopa de sal
- 2 colheres de sopa de levedura nutricional
- 1 colher de chá de alho em pó
- Pimenta preta a gosto

### Para Servir

- Arroz branco cozido
- Batatas fritas (opcional)

## Preparação

### Preparar o Creme Branco

1. **Triture** o tofu, os cajus demolhados e escorridos, a água, o sal, a levedura nutricional, o alho em pó e a pimenta num liquidificador até obter um creme homogéneo e suave. Reserve.

### Preparar o Estrogonofe

1. **Depois do demolho de 24 horas**, lave bem o grão-de-bico e coza em água com sal durante 40 a 50 minutos até ficar macio. Escorra e reserve.
2. **Numa frigideira grande**, aqueça o óleo em lume médio. Adicione a cebola e refogue por 6 a 7 minutos até ficar macia.
3. **Junte o alho** e refogue por mais 1 a 2 minutos, sempre em lume baixo.
4. **Adicione os cogumelos**, mexa e tape a frigideira. Deixe cozinhar por 5 minutos.
5. **Junte o grão-de-bico** cozido e o sal. Mexa bem.
6. **Adicione a polpa de tomate**. Deixe cozinhar até o molho reduzir ligeiramente.
7. **Verta o creme branco**, a mostarda e a pimenta preta. Mexa e prove o sal.
8. **Desligue** o lume e sirva de imediato com arroz e batatas fritas.
""",
    },
    {
        'slug': 'caril-beringela-lentilhas',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '1bb509ae-a1b9-4aeb-b05f-8959f3565133.jpg',
        'nav_title':  'Caril de Beringela e Lentilhas com Coco',
        'lista_nome': 'Caril de Beringela e Lentilhas com Coco',
        'content': r"""# Caril de Beringela e Lentilhas com Coco e Damasco

![Caril de Beringela e Lentilhas com Coco e Damasco](../imagens/1bb509ae-a1b9-4aeb-b05f-8959f3565133.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Indiana
- Dificuldade: Fácil

## Ingredientes

### Beringela

- 350 g de beringela, cortada em cubos de 2 cm
- Azeite q.b.
- ½ malagueta vermelha, às rodelas (sem sementes para menos picante)
- 2 dentes de alho, picados

### Base do Caril

- Azeite q.b.
- 1 cebola castanha, cortada em cubinhos
- 4 dentes de alho, picados
- ½ nó de gengibre fresco, ralado
- ½ malagueta vermelha, às rodelas
- 2 colheres de chá de caril suave em pó
- 1 colher de chá de cúrcuma
- 1 colher de chá de cominhos
- 1 colher de chá de malagueta em pó picante
- ½ colher de chá de coentros em pó
- 1 colher de chá de garam masala
- 1 colher de sopa de concentrado de tomate
- 1 folha de louro

### Caril

- 1 lata de 400 g de tomate picado
- 2 latas de 400 g de lentilhas castanhas, escorridas
- 1 lata de 400 g de leite de coco
- 8 damascos secos, picados
- 2 colheres de sopa de levedura nutricional
- Sal e pimenta a gosto

### Para Servir

- Rodelas de limão
- Coentros frescos
- Arroz basmati e/ou pão naan
- Iogurte de soja
- Sementes de sésamo (opcional)

## Preparação

1. **Frite a malagueta e o alho** num fio de azeite por 30 segundos. Adicione a beringela e cozinhe por 8 a 10 minutos, mexendo, até ficar estufada e ligeiramente tostada. Reserve.
2. **Na mesma frigideira**, refogue a cebola, o alho, o gengibre e a malagueta em azeite por 5 minutos até ficarem translúcidos.
3. **Adicione as especiarias** (caril, cúrcuma, cominhos, malagueta em pó, coentros, garam masala) e torre durante 1 minuto, mexendo sempre. Junte o concentrado de tomate.
4. **Adicione as lentilhas escorridas**, depois o tomate picado, o leite de coco, a folha de louro e meia lata de água. Leve a lume brando por 15 a 20 minutos, adicionando os damascos secos a meio do tempo.
5. **Fora do lume**, misture a levedura nutricional. Ajuste o sal e a pimenta.
6. **Sirva** com a beringela tostada por cima, rodelas de limão, coentros frescos, arroz basmati ou naan, iogurte de soja e sementes de sésamo.
""",
    },
    {
        'slug': 'tofu-laranja',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '9a252c26-b806-427c-8861-8754669b41ac.jpg',
        'nav_title':  'Tofu com Molho de Laranja',
        'lista_nome': 'Tofu com Molho de Laranja',
        'content': r"""# Tofu com Molho de Laranja

![Tofu com Molho de Laranja](../imagens/9a252c26-b806-427c-8861-8754669b41ac.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Chinesa
- Dificuldade: Fácil

## Ingredientes

### Para o Tofu

- ½ kg de tofu firme
- Sal e pimenta a gosto
- Amido de milho para envolver
- Cebolinho às fatias para servir

### Para o Molho de Laranja

- 200 ml de sumo de laranja fresco
- Raspas de 1 laranja
- 2 dentes de alho, picados
- 1 nó de gengibre fresco, ralado
- 1 colher de sopa de açúcar
- 2 colheres de sopa de talos de cebolinho picados
- 2 colheres de sopa de molho de soja
- 1 colher de sopa de miso
- 1 colher de sopa de vinagre de arroz
- Um fio de óleo de sésamo tostado
- 1 colher de sopa de amido de milho

## Preparação

### Preparar o Tofu

1. **Escorra bem** o tofu em folhas de papel de cozinha para remover o excesso de água. Corte em pedaços pequenos.
2. **Tempere** o tofu com sal e pimenta. Cubra todos os pedaços com amido de milho para criar uma camada crocante.
3. **Frite** os pedaços de tofu em óleo quente por 3 a 4 minutos de cada lado até ficarem dourados e crocantes; ou coloque na airfryer a 200°C durante 20 minutos, virando a meio do tempo.

### Preparar o Molho

1. **Numa pequena frigideira**, combine todos os ingredientes do molho: o sumo de laranja, as raspas, o alho, o gengibre, o açúcar, o cebolinho, o molho de soja, o miso, o vinagre de arroz, o óleo de sésamo e o amido de milho.
2. **Cozinhe** em lume médio, mexendo constantemente, até o molho engrossar e ficar brilhante, cerca de 3 a 4 minutos.

### Montagem

1. **Envolva** o tofu dourado no molho de laranja e sirva de imediato.
2. **Acompanhe** com arroz branco e polvilhe com cebolinho às fatias.
""",
    },
    {
        'slug': 'massa-alta-proteina',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  'e9afd5b4-5ed5-41d9-90ac-a2e338b74461.jpg',
        'nav_title':  'Massa de Alta Proteína',
        'lista_nome': 'Massa de Alta Proteína',
        'content': r"""# Massa de Alta Proteína

![Massa de Alta Proteína](../imagens/e9afd5b4-5ed5-41d9-90ac-a2e338b74461.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Italiana
- Dificuldade: Fácil

## Ingredientes

- 200 g de esparguete (de leguminosas para mais proteína)
- 100 g de soja texturizada fina
- 50 g de espinafres frescos
- 50 g de cogumelos paris laminados
- 500 ml de leite de soja sem açúcar
- 200 ml de caldo de legumes
- 200 ml de natas vegetais (de amêndoa ou aveia)
- 40 g de levedura nutricional
- Sal e pimenta preta a gosto
- ½ colher de chá de paprika
- ½ colher de chá de gengibre em pó
- ½ colher de chá de noz-moscada
- 1 colher de chá de ervas de Provence
- Floretes de brócolos a gosto

## Preparação

1. **Numa frigideira grande** ou tacho fundo, coloque o esparguete partido ao meio, a soja texturizada, os espinafres, os cogumelos, os brócolos e as especiarias.
2. **Verta** o leite de soja, o caldo de legumes e as natas vegetais por cima de tudo.
3. **Tape** e cozinhe em lume médio, mexendo de vez em quando, para evitar que a massa se cole.
4. **Adicione mais caldo** se reduzir demasiado depressa.
5. **Quando a massa estiver al dente** e o molho cremoso, retire do lume.
6. **Adicione a levedura nutricional**, mexa bem e prove o tempero.
7. **Sirva** de imediato, polvilhado com levedura nutricional adicional se desejar.
""",
    },
    {
        'slug': 'filetes-tofu-russos',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '3f3372fc-1348-40a5-8a37-ecc3bd8c7ecd.jpg',
        'nav_title':  'Filetes de Tofu à Russa',
        'lista_nome': 'Filetes de Tofu à Russa',
        'content': r"""# Filetes de Tofu à Russa

![Filetes de Tofu à Russa](../imagens/3f3372fc-1348-40a5-8a37-ecc3bd8c7ecd.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Russa
- Dificuldade: Fácil

## Ingredientes

- 400 g de tofu firme, bem escorrido
- 1 cebola roxa, picada finamente
- 2 dentes de alho, picados
- Um punhado de salsa fresca, picada
- 2 colheres de sopa de concentrado de tomate
- Sal e pimenta preta a gosto
- ½ colher de chá de paprika
- 100 g de farinha de grão-de-bico (adicionar 1 colher de sopa de vinagre de maçã para suavizar o sabor)

## Preparação

1. **Escorra e pressione** bem o tofu com papel de cozinha para remover o máximo de água possível.
2. **Numa tigela grande**, esmague o tofu com um garfo até obter uma textura granulada.
3. **Junte** a cebola, o alho, a salsa, o concentrado de tomate, o sal, a pimenta e a paprika. Misture bem.
4. **Adicione metade da farinha de grão-de-bico** com a colher de vinagre. Misture e avalie a consistência — a massa deve ser moldável mas não demasiado húmida. Adicione o resto da farinha se necessário.
5. **Molde** a mistura em filetes com as mãos, pressionando bem para compactar.
6. **Cozinhe** numa frigideira antiaderente com um fio de óleo em lume médio, 3 a 4 minutos de cada lado, até ficarem dourados e crocantes; ou asse no forno a 200°C durante 20 minutos, virando a meio.
7. **Sirva** com arroz branco, puré de batata ou salada fresca. Os filetes podem ser congelados antes de cozinhar para preparar com antecedência.
""",
    },
    {
        'slug': 'salada-molho-tahine',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  'b0f09471-f3f3-4b56-964f-caadbcad2bef.jpg',
        'nav_title':  'Salada Nutritiva com Molho de Tahine',
        'lista_nome': 'Salada Nutritiva com Molho de Tahine',
        'content': r"""# Salada Nutritiva com Molho de Tahine

![Salada Nutritiva com Molho de Tahine](../imagens/b0f09471-f3f3-4b56-964f-caadbcad2bef.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Mediterrânea
- Dificuldade: Fácil

## Ingredientes

### Grão-de-Bico Crocante

- 100 g de grão-de-bico cru (demolhar em água por pelo menos 12 horas)
- 1 colher de sopa de azeite
- ½ colher de sopa de paprika fumada
- ½ colher de sopa de cúrcuma
- Sal e pimenta preta a gosto

### Molho de Tahine

- ¼ chávena de tahine
- Sumo de 1 limão pequeno
- Sal a gosto
- 50 a 60 ml de água (adicionar aos poucos)

### Legumes Assados

- 1 a 2 curgetes, cortadas em rodelas
- Uma embalagem de tomates cherry
- 1 colher de sopa de azeite
- Sal e pimenta preta a gosto

### Base da Salada

- Folhas de alface ou rúcula
- Sementes de sésamo a gosto

## Preparação

### Preparar o Grão-de-Bico Crocante

1. **Depois do demolho**, coza o grão-de-bico em água com sal até ficar macio, cerca de 40 a 50 minutos. Escorra e deixe arrefecer.
2. **Transfira** o grão para uma tigela. Tempere com azeite, paprika fumada, cúrcuma, sal e pimenta.
3. **Leve à airfryer** por 15 a 18 minutos a 200°C, mexendo a meio. Deixe arrefecer para ficar crocante.

### Assar os Legumes

1. **Num tabuleiro**, disponha a curgete e os tomates cherry. Regue com azeite e tempere com sal e pimenta.
2. **Asse no forno** a 200°C até dourarem, cerca de 20 a 25 minutos.

### Preparar o Molho de Tahine

1. **Numa tigela**, misture o tahine com o sumo de limão e o sal. Adicione a água aos poucos, mexendo, até obter um molho suave e fluido.

### Montagem

1. **Num prato grande**, disponha as folhas de alface ou rúcula como base.
2. **Por cima**, coloque os legumes assados e o grão-de-bico crocante.
3. **Regue** generosamente com o molho de tahine e polvilhe com sementes de sésamo.
""",
    },
    {
        'slug': 'tofu-beringela-assada',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '3f9d972d-a5dc-4d6c-a384-bf39f4bc9514.jpg',
        'nav_title':  'Tofu com Beringela Assada',
        'lista_nome': 'Tofu com Beringela Assada',
        'content': r"""# Tofu com Beringela Assada

![Tofu com Beringela Assada](../imagens/3f9d972d-a5dc-4d6c-a384-bf39f4bc9514.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Mediterrânea
- Dificuldade: Fácil

## Ingredientes

- 400 g de tofu firme
- Sumo de ½ limão
- 2 a 3 colheres de sopa de molho de soja
- 2 colheres de sopa de azeite
- 1 colher de chá de alho em pó
- 2 colheres de sopa de levedura nutricional
- 2 beringelas, cortadas em rodelas ou cubos
- 500 ml de tomate triturado
- Azeite q.b.
- Orégãos a gosto
- Azeitonas pretas a gosto
- Salsa fresca a gosto
- Sementes de sésamo integral a gosto

## Preparação

### Preparar o Tofu

1. **Corte o tofu** em fatias ou cubos e coloque numa tigela.
2. **Marine** com o sumo de limão, o molho de soja, o azeite, o alho em pó e a levedura nutricional. Deixe marinar por pelo menos 15 minutos.
3. **Frite ou asse** o tofu marinado até ficar dourado e crocante — numa frigideira com azeite por 3 a 4 minutos de cada lado, ou no forno a 200°C por 25 minutos.

### Preparar a Beringela

1. **Num tabuleiro**, disponha as rodelas de beringela. Regue com azeite e tempere com orégãos e sal.
2. **Asse no forno** a 200°C por 20 a 25 minutos, virando a meio, até ficarem macias e douradas.

### Preparar o Molho de Tomate

1. **Numa frigideira**, aqueça um fio de azeite em lume médio. Adicione o tomate triturado e deixe cozinhar por 10 minutos até reduzir. Tempere com orégãos, sal e pimenta a gosto.

### Montagem

1. **Numa travessa**, coloque o molho de tomate como base.
2. **Disponha por cima** a beringela assada e o tofu dourado.
3. **Decore** com azeitonas pretas, salsa fresca picada e sementes de sésamo integral.
""",
    },
    {
        'slug': 'massa-pimento-cremosa',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '6bef5146-8794-44de-a061-3d4ac43813e5.jpg',
        'nav_title':  'Massa Cremosa de Pimento Vermelho Assado',
        'lista_nome': 'Massa Cremosa de Pimento Vermelho Assado',
        'content': r"""# Massa Cremosa de Pimento Vermelho Assado com Migas de Alho

![Massa Cremosa de Pimento Vermelho Assado com Migas de Alho](../imagens/6bef5146-8794-44de-a061-3d4ac43813e5.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Italiana
- Dificuldade: Fácil

## Ingredientes

- 200 g de massa (à escolha)
- 200 g de pimentos vermelhos assados (cerca de 3 pimentos)
- 1 colher de sopa de pasta de tomate seco
- 1 colher de chá de paprika
- 1 colher de chá de mistura de ervas
- 1 colher de chá de sal
- 2 dentes de alho
- 25 g de queijo vegano ralado
- 300 g de tofu sedoso
- Salsa fresca picada a gosto

### Para as Migas de Alho

- Azeite a gosto
- 20 g de pão ralado panko
- 1 dente de alho, esmagado
- Raspas de ½ limão
- 1 colher de sopa de queijo vegano ralado

## Preparação

1. **Prepare o molho**: no liquidificador, triture os pimentos assados, o tofu sedoso, a pasta de tomate seco, o queijo vegano, os dentes de alho, a paprika, as ervas, o sal e pimenta preta até obter um molho completamente suave.
2. **Coza a massa** de acordo com as instruções da embalagem. Escorra e reserve.
3. **Numa frigideira**, aqueça suavemente o molho em lume médio durante 3 a 4 minutos, mexendo.
4. **Adicione a massa** cozida e envolva tudo muito bem. Junte a salsa picada.
5. **Prepare as migas**: numa frigideira pequena, aqueça 1 colher de chá de azeite em lume médio-baixo. Adicione o pão ralado, o alho esmagado e as raspas de limão. Cozinhe até dourar, sem deixar queimar. Retire do lume e misture o queijo vegano.
6. **Sirva** a massa com as migas de alho polvilhadas generosamente por cima.
""",
    },
    {
        'slug': 'biryani-tofu-vegano',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '6cfc37ab-0ec4-4b9c-84ec-8cca6208f2f9.jpg',
        'nav_title':  'Biryani de Tofu Vegano',
        'lista_nome': 'Biryani de Tofu Vegano',
        'content': r"""# Biryani de Tofu Vegano

![Biryani de Tofu Vegano](../imagens/6cfc37ab-0ec4-4b9c-84ec-8cca6208f2f9.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Indiana
- Dificuldade: Médio

## Ingredientes

### Marinada do Tofu

- 400 g de tofu firme, cortado em cubos
- 2 colheres de sopa de iogurte de coco
- 1 colher de chá de sal
- 1 colher de chá de cúrcuma
- 1 colher de chá de cominhos
- 1 colher de chá de coentros em pó
- 1 colher de chá de malagueta em pó
- 1 colher de sopa de pasta de alho e gengibre
- 2 colheres de sopa de azeite
- 4 ramos de coentros frescos, picados
- 1 malagueta verde, picada
- Sumo de ½ limão

### Arroz

- 358 g de arroz basmati (demolhar em água por 30 minutos)
- 4 litros de água
- 2 colheres de sopa de sal
- 4 vagens de cardamomo
- ½ pau de canela
- 7 grãos de pimenta preta
- 3 cravos-da-índia
- 1 flor de macis
- 2 anis-estrelados
- 2 folhas de louro
- Algumas folhas de hortelã
- Alguns ramos de coentros

### Montagem

- 2 cebolas grandes, fatiadas e fritas até ficarem crocantes (cebola frita)
- 2 tomates, cortados em rodelas
- ½ pimento verde, cortado em tiras
- 2 colheres de sopa de iogurte de coco
- Folhas de hortelã e coentros para decorar

## Preparação

### Marinar o Tofu

1. **Numa tigela**, misture todos os ingredientes da marinada com o tofu. Deixe marinar no frigorífico por pelo menos 30 minutos.
2. **Adicione metade** da cebola frita ao tofu marinado e envolva.

### Cozer o Arroz

1. **Leve os 4 litros de água** a ferver num tacho grande com o sal e todas as especiarias inteiras, as folhas de hortelã e os coentros.
2. **Adicione o arroz** demolhado e escorrido. Coza a 90% (ainda ligeiramente firme ao centro). Escorra a água completamente.

### Montar o Biryani

1. **No mesmo tacho**, coloque o tofu marinado como primeira camada. Adicione os tomates, o pimento verde e o iogurte de coco.
2. **Cozinhe** em lume médio por alguns minutos.
3. **Cubra** com o arroz semi-cozido. Por cima do arroz, disponha a restante cebola frita, hortelã e coentros.
4. **Cubra bem** o tacho com papel de alumínio e a tampa. Cozinhe em lume muito baixo durante 20 a 25 minutos, até o arroz ficar completamente cozido e perfumado.
5. **Sirva** mexendo suavemente para juntar as camadas.
""",
    },
    {
        'slug': 'wellington-vegano',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '6851fed3-5d46-4091-9741-69c25b44f199.jpg',
        'nav_title':  'Wellington Vegano',
        'lista_nome': 'Wellington Vegano',
        'content': r"""# Wellington Vegano

![Wellington Vegano](../imagens/6851fed3-5d46-4091-9741-69c25b44f199.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Britânica
- Dificuldade: Difícil

## Ingredientes

- 3 colheres de sopa de azeite (dividido)
- ⅔ chávena de nozes
- ⅓ chávena de cajus
- 2 colheres de sopa de linhaça moída
- 5 colheres de sopa de água quente
- 1 cenoura, picada finamente
- 1 alho-francês, picado finamente
- 2 cebolas amarelas, picadas finamente
- 4 dentes de alho, picados
- 100 g de cogumelos shiitake, picados finamente
- 200 g de cogumelos castanhos, picados finamente
- 6 ramos de tomilho fresco (folhas removidas)
- 3 folhas de salva, picadas finamente
- 1 colher de sopa de tamari (de preferência com baixo teor de sódio)
- 1 colher de sopa de molho vegan Worcestershire
- 1 ½ chávenas de lentilhas castanhas cozidas
- ¾ chávena de flocos de aveia
- ⅓ chávena de salsa fresca, picada finamente
- Sal e pimenta a gosto
- 2 quadrados de massa folhada vegana (de compra)
- 2 colheres de chá de xarope de ácer
- 1 colher de sopa de leite vegetal

## Preparação

1. **Lave e pique** todos os legumes. Retire as folhas de tomilho dos ramos. Pique grosseiramente as nozes e os cajus.
2. **Prepare o "ovo" de linhaça**: misture a linhaça moída com a água quente numa tigela. Mexa bem e deixe repousar durante 5 minutos.
3. **Numa frigideira grande** em lume médio, aqueça 1 colher de sopa de azeite. Adicione as nozes e os cajus e cozinhe por cerca de 5 minutos até ficarem ligeiramente dourados, mexendo frequentemente. Vigile para não queimarem. Reserve.
4. **Na mesma frigideira**, em lume médio, aqueça 2 colheres de sopa de azeite. Adicione a cenoura, o alho-francês e as cebolas. Cozinhe por 10 minutos, mexendo regularmente.
5. **Junte o alho**, os cogumelos, o sal, o tomilho e a salva. Cozinhe por mais 10 minutos, mexendo regularmente.
6. **Adicione o tamari**, o molho Worcestershire e as lentilhas. Reduza o lume e cozinhe por mais 10 minutos.
7. **Transfira o recheio** para uma tigela grande. Adicione os flocos de aveia, a salsa, o "ovo" de linhaça e as nozes e cajus picados. Mexa bem até ficar tudo incorporado.
8. **Triture metade da mistura** levemente num processador de alimentos (consulte fotografias da receita para uma referência visual). Volte a juntar à tigela e misture. Prove e ajuste o sal e a pimenta. Leve ao frigorífico durante 20 minutos para arrefecer — isto facilitará a moldagem.
9. **Pré-aqueça o forno** com ventoinha a 190°C. Retire a massa folhada do congelador 10 minutos antes de usar.
10. **Coloque um quadrado** de massa folhada sobre papel vegetal. Deite metade da mistura do recheio no centro e molde num formato de rolo. Deixe cerca de 1 cm de massa nas extremidades superior e inferior.
11. **Com uma faca afiada**, faça cortes diagonais de 4 cm de comprimento e 1 cm de espaçamento de cima a baixo em ambos os lados da massa. Dobre a massa superior e inferior sobre o rolo. Entrelaça cada tira sobre o recheio em forma de tranças, começando do topo.
12. **Repita** com o segundo quadrado de massa e o restante recheio para fazer um segundo Wellington.
13. **Prepare a "gema"**: misture o xarope de ácer com o leite vegetal. Pincele suavemente sobre cada Wellington.
14. **Asse no forno** por 35 a 40 minutos até ficarem dourados, rodando o tabuleiro a meio do tempo para uma cozedura uniforme. Deixe repousar 10 minutos antes de fatiar.
""",
    },
    {
        'slug': 'massa-ragu-vegano',
        'cat':  'pratos-principais',
        'dir':  PP_DIR,
        'img':  '903712fc-173d-4c2a-9536-6f2388e90607.jpg',
        'nav_title':  'Massa al Ragù Vegano',
        'lista_nome': 'Massa al Ragù Vegano',
        'content': r"""# Massa al Ragù Vegano

![Massa al Ragù Vegano](../imagens/903712fc-173d-4c2a-9536-6f2388e90607.jpg)

## Informação

- Categoria: Pratos Principais
- Cozinha: Italiana
- Dificuldade: Médio

## Ingredientes

- 100 g de nozes
- 200 g de couve-flor
- 400 g de cogumelos
- Azeite a gosto
- Sal a gosto
- 1 cebola, picada finamente
- 2 talos de aipo, picados finamente
- 5 colheres de sopa de concentrado de tomate
- 1 colher de sopa de miso (opcional, mas recomendado)
- 60 ml de vinagre balsâmico
- 1 a 2 chávenas de água (250 a 500 ml)
- Pimenta preta a gosto
- 1 colher de chá de paprika e ervas secas a gosto
- 2 folhas de louro
- 350 g de massa (tagliatelle, pappardelle ou esparguete)
- Levedura nutricional para servir

## Preparação

1. **No processador**, triture as nozes, a couve-flor e os cogumelos grosseiramente. Misture com um fio de azeite e sal.
2. **Espalhe** a mistura num tabuleiro e asse a 200°C durante 30 minutos, mexendo aos 15 minutos, até ficar dourado e levemente estaladiço.
3. **Numa frigideira grande**, refogue a cebola e o aipo em azeite por 5 minutos até ficarem macios.
4. **Adicione o concentrado de tomate** e o miso. Cozinhe por 1 a 2 minutos, mexendo, para caramelizar.
5. **Deglaze** com o vinagre balsâmico e deixe evaporar quase completamente.
6. **Junte a mistura** de nozes, couve-flor e cogumelos assados.
7. **Adicione a água**, a pimenta, a paprika, as ervas e as folhas de louro. Mexa bem e deixe fervilhar em lume brando por pelo menos 20 minutos.
8. **Coza a massa** al dente de acordo com as instruções. Reserve um pouco da água de cozedura antes de escorrer.
9. **Junte a massa** à frigideira com o ragù e um pouco da água de cozedura. Cozinhe por mais 2 minutos para a massa absorver o molho.
10. **Sirva** com levedura nutricional polvilhada por cima.
""",
    },
    # ─── SOPAS ───────────────────────────────────────────────────────────────
    {
        'slug': 'guisado-grao-limao',
        'cat':  'sopas',
        'dir':  SO_DIR,
        'img':  'c139dff9-e970-49d1-bcd6-51745145e284.jpg',
        'nav_title':  'Guisado de Grão-de-Bico com Limão Caramelizado',
        'lista_nome': 'Guisado de Grão-de-Bico com Limão Caramelizado',
        'content': r"""# Guisado de Grão-de-Bico com Limão Caramelizado

![Guisado de Grão-de-Bico com Limão Caramelizado](../imagens/c139dff9-e970-49d1-bcd6-51745145e284.jpg)

## Informação

- Categoria: Sopas
- Cozinha: Mediterrânea
- Dificuldade: Fácil

## Ingredientes

- ½ limão cortado em rodelas (não demasiado finas para não se desfazerem durante a cozedura)
- 2 dentes de alho, picados
- 3 chalotas pequenas, picadas
- ¼ colher de chá de flocos de malagueta
- 200 ml de caldo de legumes
- Um punhado de salsa fresca, picada finamente
- 1 frasco de 570 g de grão-de-bico (ou 2 latas de 400 g), escorrido e lavado
- 2 colheres de sopa de natas de coco
- 1 colher de sopa de levedura nutricional
- 2 colheres de sopa de azeite
- Pimenta preta a gosto
- Torradas com manteiga vegetal para acompanhar

## Preparação

1. **Numa frigideira média**, aqueça o azeite em lume médio-alto. Assim que estiver quente, adicione as rodelas de limão. Deixe cozinhar e amolecer por cerca de 1 minuto de cada lado até ficarem ligeiramente caramelizadas.
2. **Adicione** o alho picado e as chalotas. Frite por 4 a 5 minutos até ficarem macios. Pode colocar uma tampa para evitar que o limão salte.
3. **Junte os flocos de malagueta** e cozinhe por 2 minutos.
4. **Verta o caldo de legumes**, deixe ferver e reduza para lume brando. Cozinhe até reduzir por 8 a 10 minutos.
5. **Retire as rodelas de limão** com uma espátula e reserve algumas para decorar.
6. **Adicione o grão-de-bico** à frigideira, envolvendo-o no molho.
7. **Junte as natas de coco**, a levedura nutricional e a pimenta preta. Mexa suavemente para incorporar sem desfazer o grão.
8. **Assim que estiver tudo bem quente**, sirva com as rodelas de limão caramelizadas por cima e as torradas para acompanhar.
""",
    },
    # ─── SOBREMESAS ──────────────────────────────────────────────────────────
    {
        'slug': 'bolachas-abobora-saudaveis',
        'cat':  'sobremesas',
        'dir':  SB_DIR,
        'img':  '76c27e4f-3139-44e6-888a-03acdaadcb4b.jpg',
        'nav_title':  'Bolachas de Abóbora Saudáveis',
        'lista_nome': 'Bolachas de Abóbora Saudáveis',
        'content': r"""# Bolachas de Abóbora Saudáveis

![Bolachas de Abóbora Saudáveis](../imagens/76c27e4f-3139-44e6-888a-03acdaadcb4b.jpg)

## Informação

- Categoria: Sobremesas
- Cozinha: Fusão
- Dificuldade: Fácil

## Ingredientes

- 400 g de abóbora assada
- 150 g de flocos de aveia
- 200 g de tâmaras sem caroço
- 100 g de pasta de amendoim
- Cerca de 200 ml de leite de soja (ajustar consoante a textura)
- 5 g de fermento em pó
- Baunilha a gosto
- Canela a gosto
- Gengibre em pó a gosto
- Noz-moscada a gosto
- Pepitas de cacau a gosto

## Preparação

1. **Num processador ou liquidificador**, triture a abóbora assada, os flocos de aveia, as tâmaras, a pasta de amendoim, o fermento em pó e as especiarias.
2. **Adicione o leite de soja** aos poucos até a massa ficar espessa e moldável — cerca de 200 ml.
3. **Incorpore as pepitas de cacau** à massa com uma colher.
4. **Molde as bolachas** com as mãos ou com uma colher de gelado e disponha num tabuleiro forrado com papel vegetal.
5. **Leve ao forno** pré-aquecido a 180°C até os bordos ficarem firmes e a base começar a dourar, cerca de 50 a 60 minutos.
6. **Deixe arrefecer** 10 minutos no tabuleiro antes de transferir para uma grelha — as bolachas ficam mais firmes ao arrefecer.
""",
    },
    {
        'slug': 'barras-amoras-crumble',
        'cat':  'sobremesas',
        'dir':  SB_DIR,
        'img':  '79316304-6e47-41a1-9135-9f3a232392a7.jpg',
        'nav_title':  'Barras de Crumble com Amoras',
        'lista_nome': 'Barras de Crumble com Amoras',
        'content': r"""# Barras de Crumble com Amoras

![Barras de Crumble com Amoras](../imagens/79316304-6e47-41a1-9135-9f3a232392a7.jpg)

## Informação

- Categoria: Sobremesas
- Cozinha: Inglesa
- Dificuldade: Fácil

## Ingredientes

### Para o Recheio de Amoras com Chia

- 2 chávenas de amoras (frescas ou congeladas)
- 2 colheres de sopa de sementes de chia
- 1 a 2 colheres de sopa de xarope de tâmaras (ou outro adoçante líquido)
- 2 colheres de chá de sumo de limão

### Para o Crumble

- 2 bananas médias maduras
- 2 colheres de sopa de manteiga de cajus (ou outra manteiga de frutos secos)
- 1 a 2 colheres de sopa de xarope de tâmaras
- ⅔ chávena de leite de soja
- 3 chávenas de flocos de aveia
- ½ chávena de farinha de amêndoa (substituir por farinha de aveia para versão sem frutos secos)
- 2 colheres de sopa de linhaça moída
- 2 colheres de sopa de sementes de cânhamo descascadas
- 2 colheres de sopa de sementes de abóbora
- 1 colher de chá de canela
- 1 colher de chá de fermento em pó
- Uma pitada de sal

## Preparação

1. **Num tacho pequeno** em lume médio, cozinhe as amoras por 5 a 7 minutos, mexendo frequentemente. Quando estiverem quentes, esmague com as costas de uma colher até obter uma consistência de compota. Retire do lume e misture as sementes de chia, o adoçante e o sumo de limão. Reserve para engrossar.
2. **Pré-aqueça o forno** a 180°C e forre uma forma quadrada com papel vegetal.
3. **Numa tigela**, esmague as bananas com um garfo. Misture a manteiga de frutos secos, o adoçante e o leite de soja até ficar incorporado.
4. **Adicione os ingredientes secos**: a aveia, a farinha de amêndoa, as sementes, a canela, o fermento e o sal. Misture bem.
5. **Transfira ⅔** da mistura de aveia para a base da forma forrada. Use as costas de uma colher ou espátula para pressionar e espalhar uniformemente. Coloque o recheio de amoras por cima e espalhe. Use os dedos para esfarelar o resto da mistura por cima para criar textura. Pressione suavemente para aderir.
6. **Leve ao forno** durante 30 minutos, rodando a meio.
7. **Deixe arrefecer** completamente antes de cortar em barras.
""",
    },
    {
        'slug': 'crumble-banana-doce-leite',
        'cat':  'sobremesas',
        'dir':  SB_DIR,
        'img':  '8dcbf206-ea91-4f0a-90dd-c10c5bc85841.jpg',
        'nav_title':  'Crumble de Banana com Doce de Leite Vegano',
        'lista_nome': 'Crumble de Banana com Doce de Leite Vegano',
        'content': r"""# Crumble de Banana com Doce de Leite Vegano

![Crumble de Banana com Doce de Leite Vegano](../imagens/8dcbf206-ea91-4f0a-90dd-c10c5bc85841.jpg)

## Informação

- Categoria: Sobremesas
- Cozinha: Fusão
- Dificuldade: Médio

## Ingredientes

### Para o Crumble

- 1 chávena de farinha de trigo
- ⅓ chávena de açúcar
- 90 g de manteiga vegetal (não derretida, fria)
- Canela a gosto (cerca de 3 colheres de chá)

### Para o Doce de Leite Vegano

- 1 chávena de cajus demolhados (demolhar em água quente por 5 minutos)
- 1 ½ chávenas de água
- Uma pitada de sal
- Extracto de baunilha a gosto
- ¾ chávena de açúcar

### Para a Base

- 4 a 5 bananas maduras (médias)

## Preparação

### Preparar o Crumble

1. **Numa tigela**, misture a farinha, o açúcar, a manteiga vegetal fria e a canela com as pontas dos dedos, esfarelando a manteiga na farinha até obter uma textura areada.

### Preparar o Doce de Leite Vegano

1. **Triture** os cajus demolhados com a água, o sal e a baunilha no liquidificador durante 3 a 5 minutos até obter um leite suave.
2. **Numa frigideira funda**, derreta o açúcar em lume médio, sem mexer, até formar um caramelo dourado.
3. **Adicione o leite de cajus** aos poucos (cuidado pois pode salpicar). Mexa constantemente em lume médio-baixo até o doce de leite atingir a consistência desejada, cerca de 15 a 20 minutos.

### Montagem

1. **Pré-aqueça o forno** a 180°C.
2. **Coloque as bananas** num tabuleiro de forno e leve ao forno por 10 a 15 minutos até ficarem douradas por cima.
3. **Transfira as bananas** para uma travessa de forno. Regue com o doce de leite vegano.
4. **Cubra com o crumble** e leve ao forno por mais 20 minutos até ficar dourado e estaladiço.
5. **Sirva** quente ou morno, com iogurte de coco ou gelado vegano.
""",
    },
]


def download_image(img_filename, dest_path):
    """Download an image from CDN if not already present."""
    if os.path.exists(dest_path):
        print(f'  [skip] {img_filename} already exists')
        return True
    url = CDN + img_filename
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp, open(dest_path, 'wb') as f:
            f.write(resp.read())
        print(f'  [ok]   downloaded {img_filename}')
        return True
    except Exception as e:
        print(f'  [err]  {img_filename}: {e}')
        return False


def write_recipe(r):
    """Write the markdown file for a recipe."""
    dest = os.path.join(r['dir'], r['slug'] + '.md')
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(r['content'])
    print(f'  [ok]   written {r["cat"]}/{r["slug"]}.md')


def update_mkdocs(recipes):
    """Insert new nav entries into mkdocs.yml under correct categories."""
    yml_path = os.path.join(BASE_DIR, 'mkdocs.yml')
    with open(yml_path, encoding='utf-8') as f:
        text = f.read()

    # Build sets of slugs already present
    for r in recipes:
        slug = r['slug']
        # Check if already present
        if slug in text:
            print(f'  [skip] {slug} already in mkdocs.yml')
            continue

        cat = r['cat']
        nav_title = r['nav_title']
        line = f"    - {nav_title}: {cat}/{slug}.md\n"

        if cat == 'pratos-principais':
            # Insert before the Sopas section
            marker = '  - Sopas:'
        elif cat == 'sopas':
            # Insert before the Sobremesas section
            marker = '  - Sobremesas:'
        else:  # sobremesas
            # Insert before Pesquisa section
            marker = '  - 🔍 Pesquisa'

        text = text.replace(marker, line + marker)
        print(f'  [ok]   added {slug} to mkdocs.yml')

    with open(yml_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('  mkdocs.yml updated.')


def update_lista_js(recipes):
    """Append new entries to TODAS_RECEITAS in lista.js."""
    js_path = os.path.join(DOCS_DIR, 'javascripts', 'lista.js')
    with open(js_path, encoding='utf-8') as f:
        text = f.read()

    new_entries = []
    for r in recipes:
        slug = r['slug']
        if slug in text:
            print(f'  [skip] {slug} already in lista.js')
            continue
        entry = (
            f"  {{ nome: '{r['lista_nome']}', "
            f"slug: '{slug}', "
            f"cat: '{r['cat']}' }},"
        )
        new_entries.append(entry)

    if new_entries:
        insertion = '\n'.join(new_entries) + '\n'
        text = text.replace('];', insertion + '];', 1)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'  lista.js updated with {len(new_entries)} new entries.')
    else:
        print('  lista.js already up to date.')


def main():
    print('\n=== Step 1: Writing recipe markdown files ===')
    for r in RECIPES:
        write_recipe(r)

    print('\n=== Step 2: Downloading images ===')
    for r in RECIPES:
        dest = os.path.join(IMGS_DIR, r['img'])
        download_image(r['img'], dest)

    print('\n=== Step 3: Updating mkdocs.yml ===')
    update_mkdocs(RECIPES)

    print('\n=== Step 4: Updating lista.js ===')
    update_lista_js(RECIPES)

    print('\nDone! All 20 recipes created.')


if __name__ == '__main__':
    main()
