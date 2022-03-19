import pyautogui
import time

def loop_de_espera(caminho_da_imagem: str, tempo_limite: int, apertar_esc: bool):
    # Começando a contar o tempo pro loop
    tempo_inicial = time.time()
    # Fazendo o loop de espera
    while not(pyautogui.locateOnScreen(caminho_da_imagem, confidence = 0.9)):
        # Parando de contar
        tempo_final = time.time()

        # Fazendo o calculo do tempo final
        tempo_real = tempo_final - tempo_inicial 
    
        # Se o tempo que ficar no while for atingido
        if tempo_real > tempo_limite and apertar_esc == True:
            pyautogui.press("esc")
            pyautogui.alert(text = f"Tempo limite atingido de {tempo_real: 1f} atingido, o aplicativo derá fechado após apertar o botão.")
            exit()

        if tempo_real > tempo_limite and apertar_esc == False:
            pyautogui.alert(text = f"Tempo limite atingido de {tempo_real: 1f} atingido, o aplicativo derá fechado após apertar o botão.")
            exit()

def procurar_elementos_apertando_alt_tab(caminho_da_imagem: str, tempo_limite: int, minimizar_tudo_quando_acabar_o_tempo: bool):
    # Começando o tempo
    tempo_inicial = time.time()

    # Fazendo loop de procura
    while not(pyautogui.locateOnScreen(caminho_da_imagem)):
        tempo_final = time.time()
        pyautogui.hotkey("alt", "shift", "tab")
        # Fazendo o calculo do tempo final com o inicial
        tempo_real = tempo_final - tempo_inicial

        if tempo_real > tempo_limite and minimizar_tudo_quando_acabar_o_tempo == True:
            pyautogui.hotkey("win", "m")
            pyautogui.alert(text = f"O tempo limite de busca ({tempo_real: 1f}) pelo aplicativo ou site foi excedido, o aplicativo será fechado após apertar o botão.")
            exit()
        
        if tempo_real > tempo_limite and minimizar_tudo_quando_acabar_o_tempo == False:
            pyautogui.alert(text = f"O tempo limite de busca ({tempo_real: 1f}) pelo aplicativo ou site foi excedido, o aplicativo será fechado após apertar o botão.")
            exit()

def abre_em_uma_janela_nova_ou_uma_existente():
    # Tempo de execução das linhas
    pyautogui.PAUSE = 1

    # Prompt de pergunta 
    prompt_de_pergunta_para_saber_como_vai_abrir = pyautogui.confirm(text = "O Youtube vai ser aberto em uma nova janela ou em uma janela existente?", buttons = ["Nova Janela", "Janela Existente"])

    # Condicional do "Nova Janela"
    if prompt_de_pergunta_para_saber_como_vai_abrir == "Nova Janela":
        # Abrindo o menu de navegação e escrevendo "Chrome"
        pyautogui.press("win")
        pyautogui.write("Chrome")
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/chrome_pesquisar_windows.png", tempo_limite = 5, apertar_esc = True)

        pyautogui.press("enter")
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/selecionar_usuario_chrome.png", tempo_limite = 5, apertar_esc = False)
        clicar_no_meu_usuario_chrome = pyautogui.locateCenterOnScreen("imagens_de_busca/meu_usuario_chrome.png", confidence = 0.9)
        pyautogui.click(clicar_no_meu_usuario_chrome)
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/imagem_do_botao_gmail_imagens_e_minha_conta.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.write("youtube.com")
        pyautogui.press("enter")
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/inicio_youtube.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.alert(text = "Pronto, youtube aberto. Pode mexer")
    
    # Condicional da "Janela Existente"
    if prompt_de_pergunta_para_saber_como_vai_abrir == "Janela Existente":
        pyautogui.alert(text = "Depois dessa mensagem o código vai começar, não mexa em nada até aparecer a mensagem de fim")
        procurar_elementos_apertando_alt_tab(caminho_da_imagem = "imagens_de_busca/pasta_do_chrome.png", tempo_limite = 15, minimizar_tudo_quando_acabar_o_tempo = True)
        pyautogui.hotkey("ctrl", "t")
        pyautogui.write("Youtube.com")
        pyautogui.press("enter")
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/inicio_youtube.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.alert(text = "Pronto, youtube aberto. Pode mexer")
