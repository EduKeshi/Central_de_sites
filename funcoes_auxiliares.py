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
            pyautogui.alert(text = f"Tempo limite de {int(tempo_real)} segundos atingido, o aplicativo será fechado após apertar o botão.")
            exit()

        # Se o tempo que ficar no while for atingido
        if tempo_real > tempo_limite and apertar_esc == False:
            pyautogui.alert(text = f"Tempo limite de {int(tempo_real)} segundos atingido, o aplicativo será fechado após apertar o botão.")
            exit()

def procurar_elementos_apertando_alt_tab(caminho_da_imagem: str, tempo_limite: int, minimizar_tudo_quando_acabar_o_tempo: bool):
    # Começando o tempo
    tempo_inicial = time.time()

    # Fazendo loop de procura
    while not(pyautogui.locateOnScreen(caminho_da_imagem)):
        tempo_final = time.time()
        pyautogui.hotkey("alt", "shift", "tab")
        
        # Fazendo o calculo do tempo final
        tempo_real = tempo_final - tempo_inicial

        # Se o tempo que ficar no while for atingido
        if tempo_real > tempo_limite and minimizar_tudo_quando_acabar_o_tempo == True:
            pyautogui.hotkey("win", "m")
            pyautogui.alert(text = f"O tempo limite de busca ({int(tempo_real)} sengundos) pelo aplicativo ou site foi excedido, o aplicativo será fechado após apertar o botão.")
            exit()
        
        # Se o tempo que ficar no while for atingido
        if tempo_real > tempo_limite and minimizar_tudo_quando_acabar_o_tempo == False:
            pyautogui.alert(text = f"O tempo limite de busca ({int(tempo_real)} sengundos) pelo aplicativo ou site foi excedido, o aplicativo será fechado após apertar o botão.")
            exit()