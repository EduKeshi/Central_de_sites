import pyautogui
import time

from funcoes_auxiliares import loop_de_espera, procurar_elementos_apertando_alt_tab
from emails_e_senhas_de_login import email_conta_escola, senha_conta_escola

def fazer_login_conta_escola(caminho_da_imagem: str, tempo_limite_para_esperar_a_tela_aparecer: int):
    # Começando a contar o tempo
    tempo_inicial = time.time()
    # Enquanto a imagem não aparecer ele vai ficar no loop
    while not(pyautogui.locateOnScreen(caminho_da_imagem, confidence = 0.9)):
        # Parando de contar
        tempo_final = time.time()
        # Fazendo o calculo do tempo final
        tempo_real = tempo_final - tempo_inicial
        # Se o tempo final for maior do que o tempo estipulado pelo usuário
        if tempo_real > tempo_limite_para_esperar_a_tela_aparecer:
            # Saindo da função pro código continuar
            return
    
    # Se ele achar a imagem ele vai clicar no botão de login
    botao_de_login = pyautogui.locateCenterOnScreen("imagens_de_busca/botao_de_fazer_login_conta_escola.png", confidence = 0.9)
    pyautogui.click(botao_de_login)
    # Vai esperar a tela de login aparecer, digitar o e-mail e apertar enter
    loop_de_espera(caminho_da_imagem = "imagens_de_busca/tela_de_login_google.png", tempo_limite = 10, apertar_esc = False)
    pyautogui.write(email_conta_escola)
    pyautogui.press("enter")
    # Vai esperar a tela de senha aparecer, digitar a senha e apertar enter
    loop_de_espera(caminho_da_imagem = "imagens_de_busca/campo_de_senha_conta_escola.png", tempo_limite = 10, apertar_esc = False)
    pyautogui.write(senha_conta_escola)
    pyautogui.press("enter")

def abrir_classroom():
    # Tempo de execução entre as linhas 
    pyautogui.PAUSE = 1

    # Avisando que o programa vai ser executado
    confirmacao = pyautogui.confirm(text = "O programa vai começar a ser executado, você deseja continuar?", buttons = ["Sim", "Não"])
    
    # Se a resposta for sim
    if confirmacao == "Sim":
        # Abrindo o menu de navegação e escrevendo "Chrome"
        pyautogui.press("win")
        pyautogui.write("Chrome")
        # Esperando o chrome da barra de pesquisa aparecer e apertando enter depois
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/chrome_pesquisar_windows.png", tempo_limite = 5, apertar_esc = True)
        pyautogui.press("enter")
        # Esperando abrir a página de selecionar usuário e entrendo nele depois
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/selecionar_usuario_chrome.png", tempo_limite = 5, apertar_esc = False)
        clicar_no_meu_usuario_chrome = pyautogui.locateCenterOnScreen("imagens_de_busca/usuario_conta_escola.png", confidence = 0.9)
        pyautogui.click(clicar_no_meu_usuario_chrome)
        # Antes de entrar no site ele vai esperar para ver se aparece a guia de fazer login
        fazer_login_conta_escola(caminho_da_imagem = "imagens_de_busca/fazer_login_conta_esccola.png", tempo_limite_para_esperar_a_tela_aparecer = 12)
        if pyautogui.size() == (1920, 1080):
            pyautogui.hotkey("win", "up")
        # Dogotando o nome do site e apertando enter
        pyautogui.write("classroom.google.com")
        pyautogui.press("enter")
        # Esperando o site carregar e depois mostrar a mensagem de fim
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/nome_turma_classroom.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.alert("Pronto, pode mexer.")
        
    else:
        pyautogui.alert(text = "O programa não será executado.")