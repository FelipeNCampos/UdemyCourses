# UdemyCourses | Portfólio de estudos em Python

Este repositório reúne projetos pessoais desenvolvidos durante minha jornada de estudos em Python, automação, web scraping, APIs, interfaces gráficas e desenvolvimento web. A proposta aqui não é apresentar um único produto final, mas mostrar evolução prática: da lógica básica aos projetos com integração externa, organização em módulos e uso de bibliotecas do ecossistema Python.

## O que este repositório demonstra

- Fundamentos de programação: variáveis, condicionais, loops, funções e estruturas de dados.
- Programação orientada a objetos aplicada em jogos e interfaces.
- Manipulação de arquivos, JSON, CSV e persistência simples de dados.
- Criação de interfaces com Turtle e Tkinter.
- Consumo de APIs REST com `requests`.
- Automação de navegador com Selenium.
- Web scraping com BeautifulSoup.
- Primeiros projetos web com HTML, CSS e Flask.
- Organização gradual de código em módulos, classes e camadas de responsabilidade.

## Tecnologias e ferramentas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## Projetos em destaque

| Pasta | Projeto | Principais aprendizados |
| --- | --- | --- |
| `day_20`, `day_21`, `day_24` | Snake Game | POO, controle de estado, colisões, placar e manipulação de tela com Turtle |
| `day_22` | Pong Game | Eventos de teclado, movimentação, detecção de colisões e placar |
| `day_23` | Turtle Crossing | Loop de jogo, progressão de dificuldade e composição de classes |
| `day_25/Game` | U.S. States Game | Leitura de CSV com Pandas, interação com usuário e posicionamento gráfico |
| `day_29` e `day_30` | Password Manager | GUI com Tkinter, geração de senhas, JSON e persistência local |
| `day_31` | Flash Cards | Interface gráfica, leitura de dados e acompanhamento de progresso |
| `day_32` e `day_33` | Automação com e-mail/APIs | SMTP, leitura de arquivos, integrações e automação de tarefas |
| `day_34` | Quiz App | Separação entre dados, lógica e interface |
| `day_37` e `day_38` | Habit/Nutrition Tracker | Consumo de APIs, autenticação por token, registros externos e JSON |
| `day_45` | Web Scraping | Extração e tratamento de dados com BeautifulSoup |
| `day_50` a `day_53` | Automação Web | Selenium, navegação automatizada, preenchimento de formulários e scraping |
| `day_56` | Primeiro app Flask | Rotas, templates, arquivos estáticos e estrutura básica de aplicação web |
| `Complementar/Tkinter/Calculator_UseCase` | Calculadora | Organização de caso de uso com interface desktop |

## Organização

O repositório está dividido por dias de estudo (`day_1`, `day_2`, ..., `day_56`), seguindo uma progressão incremental. Os primeiros diretórios concentram exercícios de lógica e sintaxe; os diretórios mais avançados trazem projetos com bibliotecas externas, automações e aplicações com mais de um arquivo.

```text
UdemyCourses/
|-- day_1 ... day_14        # Fundamentos, jogos simples e lógica
|-- day_15 ... day_24       # POO, Turtle, jogos e eventos
|-- day_25 ... day_35       # CSV, JSON, Tkinter, e-mail e APIs
|-- day_36 ... day_40       # APIs, autenticação e projetos com serviços externos
|-- day_41 ... day_56       # HTML/CSS, scraping, Selenium e Flask
`-- Complementar/           # Estudos extras e projetos complementares
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/FelipeNCampos/UdemyCourses.git
cd UdemyCourses
```

Execute um projeto Python específico:

```bash
python day_20/Main.py
```

Alguns projetos usam bibliotecas externas. Instale conforme a necessidade do projeto:

```bash
pip install requests pandas selenium beautifulsoup4 flask python-dotenv
```

Projetos que consomem APIs ou automatizam serviços externos podem exigir variáveis de ambiente, tokens ou credenciais locais em arquivos `.env`.

## Para recrutadores

Este repositório mostra meu processo de construção de repertório técnico. Ele evidencia constância, prática com problemas diferentes e capacidade de aprender ferramentas novas enquanto transformo conceitos em código funcional.

Os projetos mais interessantes para avaliar evolução técnica estão especialmente entre `day_20` e `day_56`, onde aparecem organização em classes, uso de bibliotecas externas, automação, integração com APIs e primeiros passos em desenvolvimento web.

## Próximos passos

- Adicionar `requirements.txt` por projeto ou um arquivo geral de dependências.
- Padronizar nomes de arquivos e pastas.
- Separar os projetos principais em repositórios próprios.
- Incluir testes automatizados nos projetos com maior complexidade.
- Melhorar tratamento de erros, configuração por ambiente e documentação individual dos projetos.
