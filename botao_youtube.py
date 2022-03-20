import pyautogui

from funcoes_auxiliares import loop_de_espera, procurar_elementos_apertando_alt_tab

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
        # Esperando o chrome da barra de pesquisa aparecer e apertando enter
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/chrome_pesquisar_windows.png", tempo_limite = 5, apertar_esc = True)
        pyautogui.press("enter")
        # Esperando abrir a página de selecionar usuário e entrendo nele
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/selecionar_usuario_chrome.png", tempo_limite = 5, apertar_esc = False)
        clicar_no_meu_usuario_chrome = pyautogui.locateCenterOnScreen("imagens_de_busca/meu_usuario_chrome.png", confidence = 0.9)
        pyautogui.click(clicar_no_meu_usuario_chrome)
        # Esperando aparecer o elemento padrão do google para depois digitar o site e apertendo enter
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/imagem_do_botao_gmail_imagens_e_minha_conta.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.write("youtube.com")
        pyautogui.press("enter")
        # Esperado aparecer a logo do Youtube e depois mostrando a mensagem de fim
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/inicio_youtube.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.alert(text = "Pronto, youtube aberto. Pode mexer")
    
    # Condicional da "Janela Existente"
    if prompt_de_pergunta_para_saber_como_vai_abrir == "Janela Existente":
        # Mensagem de aviso que o código vai começar
        pyautogui.alert(text = "Depois dessa mensagem o código vai começar, não mexa em nada até aparecer a mensagem de fim")
        # Procurando o google aberto
        procurar_elementos_apertando_alt_tab(caminho_da_imagem = "imagens_de_busca/pasta_do_chrome.png", tempo_limite = 15, minimizar_tudo_quando_acabar_o_tempo = True)
        # Abrindo uma nova guia, digitando o nome do site e apertando enter
        pyautogui.hotkey("ctrl", "t")
        pyautogui.write("Youtube.com")
        pyautogui.press("enter")
        # Esperado aparecer a logo do Youtube e depois mostrando a mensagem de fim
        loop_de_espera(caminho_da_imagem = "imagens_de_busca/inicio_youtube.png", tempo_limite = 15, apertar_esc = False)
        pyautogui.alert(text = "Pronto, youtube aberto. Pode mexer")