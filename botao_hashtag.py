import pyautogui

from funcoes_auxiliares import loop_de_espera
from emails_e_senhas_de_login import email_curso_python, senha_curso_python

def entrar_no_curso():
    # Tempo de execução entre as linhas
    pyautogui.PAUSE = 1

    # Perguntado se ele quer executar
    pergunta_confirmacao = pyautogui.confirm(text = "O programa vai começar a ser executado, você deseja continuar?", buttons = ["Sim", "Não"])

    # Condicional
    if pergunta_confirmacao == "Sim":
        pyautogui.alert(text = "Não mexa em nada até aparecer a mensagem de fim")
        # Abrindo o menu de navegação e escrevendo "Chrome"
        pyautogui.press("win")
        pyautogui.write("Chrome")
        # Esperando o chrome da barra de pesquisa aparecer e apertando enter
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/chrome_pesquisar_windows.png", tempo_limite = 5, apertar_esc = True)
        pyautogui.press("enter")
        # Esperando abrir a página de selecionar usuário e entrendo nele
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/selecionar_usuario_chrome.png", tempo_limite = 5, apertar_esc = False)
        clicar_no_meu_usuario_chrome = pyautogui.locateCenterOnScreen("imagens_de_busca/meu_usuario_chrome.png", confidence = 0.9)
        pyautogui.click(clicar_no_meu_usuario_chrome)
        # Esperando aparecer as pastas do google e clicando na pasta
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/pasta_do_chrome.png", tempo_limite = 15, apertar_esc = False)
        clica_na_minha_pasta = pyautogui.locateCenterOnScreen("imagens_de_busca/pasta_do_chrome.png", confidence = 0.9)
        pyautogui.click(clica_na_minha_pasta)
        # Esperando as pastas carregarem e apertando na pasta do curso
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/nome_curso_python.png", tempo_limite = 10, apertar_esc = False)
        aperta_na_pasta_do_curso = pyautogui.locateCenterOnScreen("imagens_de_busca/nome_curso_python.png", confidence = 0.9)
        pyautogui.click(aperta_na_pasta_do_curso)
        # Esperando as páginas aparecerem e apertando no site do curso
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/site_curso.png", tempo_limite = 7, apertar_esc = False)
        clica_no_site_do_curso = pyautogui.locateCenterOnScreen("imagens_de_busca/site_curso.png", confidence = 0.9)
        pyautogui.click(clica_no_site_do_curso)
        # Esperando o site carregar e fazendo login
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/botoes_login_hashtag.png", tempo_limite = 15, apertar_esc = False)
        # Colocando os dados de acesso
        pyautogui.write(email_curso_python)
        pyautogui.press("tab")
        pyautogui.write(senha_curso_python)
        pyautogui.typewrite(["tab", "tab", "enter"], interval = 1)
        # Esperando o curso carregar
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/dentro_do_curso_python.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.alert(text = "Pode mexer.")
    else:
        pyautogui.alert(text = "A função não vai ser usada")