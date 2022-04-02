# Central de sites
A Central de Sites é uma automação feita 100% em Python, ela reune os principais sites que eu costumava usar quando estava em lockdown em 2021.<br>
Eu reformulei ela pois ela havia sido feita em agosto de 2021 e já não funcionava mais.

# Tecnologias usadas
## Para fazer a janela:
- Figma: Eu utilizei o Figma para desenhar a janela.
- Proxlight Designer: Essa é uma ferramenta Open Source que pega os seus projetos desenhados no Figma e exporta eles para código Python.

## IDE utilizada:
- Vscode: O Vscode é uma IDE desenvolvida pela Microsoft.

## Linguagem utilizada:
- Python

## Bibliotecas utilizadas:
- Pyautogui: O Pyautogui é uma biblioteca que tem como objetivo fazer automações, ela controla o seu mouse e seu teclado.
- Selenium: O Selenium é uma biblioteca que tem como objetivo o web scraping, ela utiliza 100% o navegador.
- Tkinter: O Tkinter é um construtor de janela, toda a parte visual da janela foi feita com ele.
- SpeechRecognition: O SpeechRecognition é uma biblioteca para trabalhar com voz.
- Time: A biblioteca Time é utilizada para mexer com o tempo.

# Como a Central de Sites funciona?
Ela é orientada a imagens, eu faço screenshots dos lugares onde eu quero que ela clique, ela tembém tem uma funcionalidade que usa comandos de voz, quando ela reconhece o comando as respectivas funções são chamadas.

# Vantagens
- Você consegue reunir todos os aplicativos/sites que deja entrar e um lugar só;
- Ela é totalmente autonoma, ninguém precisa ficar olhando pro computador quando ela estiver em execução;
- Fica mais fácil de implementar novas funcionalidades;
- Fácil de mexer.

# Desvantagens
- A biblioteca Pyautogui não funciona em outras telas, somente ma tela principal do seu computador;
- O Pyautogui não consegui identificar a imagem se a screenshot não for tirada no seu computador, pois ele identifica a resolução da tela, e se for diferente da tela que ele esá em execução ele não consegue ver a imagem;
- Você não pode mexer no computador se a funcionalidade utilizar o Pyautogui, pois ele controla o seu mouse e seu teclado;
- Se a imagem ficar diferente no futuro você vai ter que tirar uma nova screenshot;
- A interface gráfica não tem eventos se o código está em execução. Como o Python tem um fluxo sincrono (uma coisa depois a outra) isso não permite fazer uma interface que tenha eventos fora da funcionalidade.
