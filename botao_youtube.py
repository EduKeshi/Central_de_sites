import pyautogui
import time

import Central_de_Sites as cds

def defina_o_tempo_de_execucao_das_linhas():
    pyautogui.PAUSE = 1
    
def minimiza_a_central_de_sites_e_esperando_1_segundo_para_continuar():
    pyautogui.hotkey('win', 'down')
    time.sleep(1)
    
def mostre_a_confirmacao_de_inicio():
    confirmacao = pyautogui.confirm(text = cds.texto_de_confirmacao, title = 'Confirmação de Inicio', buttons = ['Continuar', 'Cancelar'])
    
    return confirmacao

def confirme_que_a_confirmacao_foi_continuar_e_pergunte_qual_guia_vai_ser_aberta(confirmacao):
    # If da confirmação
    if confirmacao == 'Continuar':
        # Prompt 1 "Você está com o google aberto?"
        pergunta_google_aberto = pyautogui.prompt(text = 'Você está com o google aberto?').casefold()
        # if do prompt 1
        if pergunta_google_aberto:
                while pergunta_google_aberto != 'sim' and pergunta_google_aberto != 'não' and pergunta_google_aberto != 'nao':
                    pyautogui.alert(text = 'Resposta inválida, responda novamente.', title = 'Resposta inválida', button = 'Ok')
                    pergunta_google_aberto = pyautogui.prompt(text = 'Você está com o google aberto?').casefold()
                    if pergunta_google_aberto == None:
                        pyautogui.alert('O código não será executado, pode mexr no computador.')
                        break
                if pergunta_google_aberto == 'sim':
                    qual_guia = pyautogui.prompt('É guia anônima ou normal?').casefold()
                    if qual_guia:
                        # Validando a resposta
                        while qual_guia != 'normal' and qual_guia != 'anônima' and qual_guia != 'anonima':
                            pyautogui.alert(f'{qual_guia} é uma resposta inválida, preencha novamente', title = 'Resposta inválida')
                            qual_guia = pyautogui.prompt('É guia anônima ou normal?').casefold()
                        # Caso a resposta seja normal
                        if qual_guia == 'normal':
                            pyautogui.alert('O código vai começar, não mexa em NADA até o código acabar.')
                            try:
                                if pyautogui.locateOnScreen('recarregar_pagina.png', confidence=0.9):
                                    pyautogui.hotkey('ctrl', 't')
                                    while not(pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png', confidence=0.9)):
                                        time.sleep(1)
                                    pyautogui.write('youtube.com')
                                    pyautogui.press('enter')
                                    while not(pyautogui.locateOnScreen('inicio_yt.png')):
                                        time.sleep(1)
                                    trocar_conta_yt()    
                                else:
                                    # Aqui ele vai tentar achar o google pela barra de tarefas
                                    x, y = pyautogui.locateCenterOnScreen('google aberto.png', confidence=0.9)
                                    pyautogui.moveTo(x, y)
                                    x, y = pyautogui.locateCenterOnScreen('google aberto barra de tarefas.png', confidence=0.9)
                                    pyautogui.moveTo(x, y)
                                    pyautogui.click(x, y)
                                    pyautogui.hotkey('ctrl', 't')
                                    while not(pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png')):
                                        time.sleep(1)
                                    pyautogui.write('youtube.com')
                                    pyautogui.press('enter')
                                    while not(pyautogui.locateOnScreen('inicio_yt.png')):
                                        time.sleep(1)
                                    trocar_conta_yt()
                            except:
                                contador_vezes = 0
                                # Aqui ele vai tentar achar apertando "Alt + Shift + Tab"
                                while not(pyautogui.locateOnScreen('recarregar_pagina.png', confidence=0.9)) and not(pyautogui.locateCenterOnScreen('recarregar_pagina_modojanela.png', confidence=0.9)):
                                    pyautogui.hotkey('alt', 'shift', 'tab')
                                    time.sleep(0.7)
                                    contador_vezes += 1
                                    if contador_vezes == 15:
                                        break
                                if contador_vezes == 15:
                                    aviso_guia_nao_encontrada = pyautogui.alert(text=f'O código não será executado pois a guia {qual_guia} não foi encontrada, clique no mesmo botão que você havia clicado para fazer novamente.', title='Guia não encontrada')
                                else:
                                    pyautogui.hotkey('win', 'up')
                                    pyautogui.hotkey('ctrl', 't')
                                    while not(pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png')):
                                        time.sleep(1)
                                    pyautogui.hotkey('win', 'up')
                                    pyautogui.hotkey('win', 'm')
                                    pyautogui.hotkey('alt', 'tab')
                                    pyautogui.write('youtube.com')
                                    pyautogui.press('enter')
                                    while not(pyautogui.locateOnScreen('inicio_yt.png')):
                                        time.sleep(1)
                                    trocar_conta_yt()
        return qual_guia

def gui_anonima(confirmacao, qual_guia):              
    if confirmacao:
        if 'anônima' in qual_guia or 'anonima' in qual_guia:
            contador_vezes = 0
            while not(pyautogui.locateOnScreen('recarregar_pagina_anonimo.png', confidence = 0.9)) and not(pyautogui.locateOnScreen('recarregar_pagina_anonimo_modojanela.png', confidence = 0.9)):
                pyautogui.hotkey('alt', 'shift', 'tab')
                time.sleep(0.7)
                contador_vezes += 1
                if contador_vezes == 15:
                    break
                else:
                    pass
            if contador_vezes == 15:
                aviso_guia_nao_encontrada = pyautogui.alert(text=f'O código não será executado pois a guia {qual_guia} não foi encontrada', title='Guia não encontrada')    
            else:
                pyautogui.hotkey('win', 'up')
                pyautogui.hotkey('win', 'm')
                pyautogui.hotkey('alt', 'tab')
                pyautogui.hotkey('ctrl', 't')
                pyautogui.write('youtube.com')
                pyautogui.press('enter')
                pyautogui.alert(cds.alerta_de_fim)
        else:
            pyautogui.alert(cds.aviso_programa_nao_sera_executado)
                else:
                    pyautogui.press('win')
                    pyautogui.write('Chrome')
                    contador_vezes = 0 # Esse contador é para limitar as vezes que o "while" vai fazer o loop
                    tempo_inicial = time.time() # Vai começar a contar os segundos aqui
                    while not(pyautogui.locateOnScreen('app do google na barra de pesquisa do windows.png')): # Achando a foto do app do google
                        time.sleep(2.8)
                        contador_vezes += 1#Cada vez que o "while" passar vai aumentar 1 
                        if contador_vezes == 20:#Quando o "while" fizer o loop 20 vezes ele para 
                            break
                        else:
                            pass
                    tempo_final = time.time() # Aqui o tempo vai parar de contar
                    tempo_total = tempo_final - tempo_inicial # Fazendo o calculo de quanto tempo deu 
                    # Depois que o tempo limite estourar
                    if contador_vezes < 20: # Se sair do "while" antes das 20 vezes ele executa 
                        pyautogui.press('enter')
                        while not(pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png')):
                            time.sleep(1)
                        else:
                            pass
                        pyautogui.hotkey('win', 'up') # Maximizando a janela
                        pyautogui.write('youtube.com')
                        pyautogui.press('enter')
                        while not(pyautogui.locateOnScreen('inicio_yt.png')):
                            time.sleep(1)
                        trocar_conta_yt()
                    # Caso contrario ele vai aparecer uma mensagem   
                    else:
                        pyautogui.press('esc') # Fechando a barra de pesquisa do Windows
                        time.sleep(1)
                        pyautogui.alert(text=f'O código não será executado pois o tempo limite de {tempo_total:.0f} segundos foi atingido', title='Tempo expirado') # Aviso de tempo expirado  
        
    else:
        pyautogui.alert(cds.aviso_programa_nao_sera_executado)