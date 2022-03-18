#Import's
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import speech_recognition as sr
from tkinter import *

#Alertas do botao_yt, botao_class e botao_hash
texto_alerta_inicio_google_fechado = '''
O código vai começar, não mexa em NADA até aparecer a proxima mensagem.
Obs: O navegador será aberto

Deseja começar?
'''
texto_alerta_inicio_google_aberto = '''
O código vai começar, não mexa em NADA até aparecer a proxima mensagem.

Deseja começar?
'''

texto_de_confirmacao = '''
Siga os Prompts que aparecerão na sua tela para execução correta do código,
se não quiser continuar aperte em 'Cancelar'.

Obs: Depois desse aviso você ainda poderá cancelar.
'''

texto_alerta_cmsp = '''
O código vai começar, você pode mexer no computador 
enquanro o código roda

Obs: Um novo navegardor será aberto.
Deseja continuar?
'''

alerta_de_fim = '''
Pode mexer
'''

aviso_programa_nao_sera_executado = '''
O programa não será executado, pode mexr no computador.
'''

#Function auxiliar do "botao_yt" para trocar de conta
def trocar_conta_yt():
    try:
        if not pyautogui.locateOnScreen('usuario_do_edu.png'):#Se eu não estiver logado no yt
            pyautogui.click(1839, 162)#Ele vai clicar na bolinha do usuário
            while not pyautogui.locateOnScreen('alterar_conta_yt.png'):#Vai esperar o "Alterar conta" aparecer
                time.sleep(1)
            time.sleep(3)
            x, y = pyautogui.locateCenterOnScreen('alterar_conta_yt.png')#Clicando no "Alterar conta"
            pyautogui.click(x, y)
            while not pyautogui.locateOnScreen('nome_usuario_yt.png', confidence=0.9):#Esperando o meu usuário aparecer
                time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('nome_usuario_yt.png', confidence=0.9)#Clicando no meu usuário
            pyautogui.click(x, y)
            pyautogui.alert(alerta_de_fim)
        else:
            pyautogui.alert(alerta_de_fim)
    except:
        pyautogui.alert(text='Não será possível trocar de conta pois algo deu errado.', title='Não foi possível trocar a conta')

#fun auxiliar para entrar na plataforma do curso
def entrar_curso():
    try:
        while not pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png'):#Enquanto ele não achar a barra de pesquisa do Google que fica na parte de baixo.
            time.sleep(1)#Espera 1 segundo.
        x, y = pyautogui.locateCenterOnScreen('Curso_barra_favoritos.png', confidence=0.9)#Vai localizar o curso e fazer o unpacking da imagem.
        pyautogui.click(x, y)#Ele vai clicar no meio do curso na barra de favoritos.
    except:
        pyautogui.alert(text='Não foi possivel achar o curso na barra de favoritos.')#Mensagem de "erro".
    try:
        while not pyautogui.locateOnScreen('nome_campo_senha_curso.png', confidence=0.9):#Enquanto ele não achar o campo de senha.
            time.sleep(1)#Espera 1 segundo.
            if pyautogui.locateOnScreen('primeiro_modulo_curso.png'):#Se ele achar o primeiro módulo do curso primeiro.
                pyautogui.alert(alerta_de_fim)#Mensagem de fim.
                break#Quebra o loop.
            elif pyautogui.locateOnScreen('botao_entrar_curso.png'):#Se ele achar o botão de entrar no curso.
                x, y = pyautogui.locateCenterOnScreen('botao_entrar_curso.png', confidence=0.9)#Ele vai procurar o botão de "Entrar" do site e fazer o unpacking da imagem.
                pyautogui.click(x, y)#Ele vai clicar no meio do botão.
                while pyautogui.locateOnScreen('botao_entrar_curso_laranja.png', confidence=0.9):#Caso ele clique no botão de login antes das credenciais estarem lá.
                    pyautogui.click(button='left')#Aperta com o botão esquerdo do mouse.
                while not pyautogui.locateOnScreen('primeiro_modulo_curso.png'):#Enquanto ele não achar o módulo do curso.
                    time.sleep(1)#Espera 1 segundo.
                pyautogui.alert(alerta_de_fim)#Mensagem de fim.
                break#Quebra o loop.
    except:
        pyautogui.alert(text='Não foi possivel fazer o login na plataforma, tente novamente.')#Mensagem de "erro".

#Hashtag
def botao_hash():
    
    pyautogui.PAUSE = 1#Tempo entre a execução das linhas
    
    pyautogui.hotkey('win', 'down')#MInimizando a Central de Sites
    
    aviso_confirmacao = pyautogui.confirm(text=texto_de_confirmacao, buttons=['Entendi', 'Cancelar'])#"Explicação" sobre como vai funcionar.
    
    if aviso_confirmacao == 'Entendi':#Se o "aviso_confirmacao" for "Entendi".
        confirmacao_google_aberto = pyautogui.confirm(text='Você está com o google aberto?', buttons=['Sim', 'Não'])#Pergunta se o Google está aberto.

        if confirmacao_google_aberto == 'Sim':#Se a "confirmacao_google_aberto" for "Sim" ele executa.
            confirmacao2= pyautogui.confirm(text=texto_alerta_inicio_google_aberto, buttons=['Sim', 'Não'])#Aviso de inicio.
            if confirmacao2 == 'Sim':
                if pyautogui.locateOnScreen('recarregar_pagina.png', confidence=0.9):#Se ele achar o botão de recarregar página do Google.
                    pyautogui.hotkey('ctrl', 't')#Abrindo uma nova aba.
                    entrar_curso()#Function para entrar no curso.
                else:
                    #Aqui ele vai tentar achar o google pela barra de tarefas
                    x, y = pyautogui.locateCenterOnScreen('google aberto.png', confidence=0.9)
                    pyautogui.moveTo(x, y)
                    x, y = pyautogui.locateCenterOnScreen('google aberto barra de tarefas.png', confidence=0.9)
                    pyautogui.moveTo(x, y)
                    pyautogui.click(x, y)
                    pyautogui.hotkey('ctrl', 't')
                    entrar_curso()#Function para entrar no curso.
            else:
                pyautogui.alert(aviso_programa_nao_sera_executado)
        else:
            confimacao = pyautogui.confirm(text=texto_alerta_inicio_google_fechado, buttons=['Sim', 'Não'])#Aviso de inicio.
            if confimacao == 'Sim':
                pyautogui.press('win')#Aperta a tecla "Windows".
                pyautogui.write('Chrome')#Escreve "Chrome".
                tempo_inicial = time.time()#Começar a contar os segundos.
                contador_vezes = 0#Vai contar quantas vezes ele vai passar.
                while not pyautogui.locateOnScreen('app do google na barra de pesquisa do windows.png'):#Enquanto ele não achar a foto do app do google na barra de pesquisa do windows.
                    time.sleep(2.8)#Espera 2.8 segundos.
                    contador_vezes += 1#Cada vez que o "While" passar ele vai acrescentar 1 na variável auxiliar.
                    if contador_vezes == 20:#Se o contador de vezes for igual a 20.
                        break#Quebra o loop.
                    else:
                        pass#Não faz nada 
                tempo_final = time.time()#Parando de contar.
                tempo_total = tempo_final - tempo_inicial#Calculando tempo final.
                if contador_vezes < 20:#Se o contador de vezes for menor que 20.
                    pyautogui.press('enter')#Vai apertar enter.
                    pyautogui.hotkey('win', 'up')#Atalho para maximizar.
                    entrar_curso()#Function para entrar no curso.
                else:
                    pyautogui.press('esc')#Apertando o esc.
                    time.sleep(0.3)#Espera 0.3 segundos.
                    pyautogui.alert(text=f'Não será possivel abrir o Google pois o tempo limite de espera de {tempo_total:.0f} segundos foi atingido.', title='Tempo limite atingido')#Mensagem de "erro".
            else:
                pyautogui.alert(aviso_programa_nao_sera_executado)#Mensagem avisando que o programa não será executado.
    else:
        pyautogui.alert(aviso_programa_nao_sera_executado)#Mensagem avisando que o programa não será executado.

def abrir_google_fechado():
    pyautogui.press('win')
    pyautogui.write('Chrome')
    tempo_inicial = time.time()
    contador_vezes = 0
    while not pyautogui.locateOnScreen('app do google na barra de pesquisa do windows.png'):
        time.sleep(2.8)
        contador_vezes += 1
        if contador_vezes == 20:
            break
        else:
            pass
    if contador_vezes < 20:
        pyautogui.press('enter')
        pyautogui.hotkey('win', 'up')
        while not pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png'):
            time.sleep(1)
        pyautogui.write('classroom.google.com')
        apagar_sugestoes()
        while not pyautogui.locateOnScreen('googleclassroom.png', confidence=0.9):
            time.sleep(1)
        fun_trocar_conta_classroom()
    else:
        tempo_final = time.time()
        tempo_total = tempo_final - tempo_inicial
        pyautogui.press('esc')
        time.sleep(0.3)
        pyautogui.alert(text=f'O programa não será executado pois o tempo limite de {tempo_total:.0f} segundos foi atingido', title='Tempo expirado')#Aviso de tempo expirado

#Function auxiliar para apagar sugestões que o google faz
def apagar_sugestoes():
    if pyautogui.locateAllOnScreen('calendario_sugestão_pesquisagoogle.png', confidence=0.9):
        pyautogui.press('delete')
        time.sleep(0.5)
        pyautogui.press('enter')
    else:
        pyautogui.press('enter')

#Function auxiliar para trocar de conta no Google Classroom
def fun_trocar_conta_classroom():
    try:
        if pyautogui.locateOnScreen('tentar_outra_conta_googleclassroom.png'):
            x, y = pyautogui.locateCenterOnScreen('tentar_outra_conta_googleclassroom.png')
            pyautogui.click(x, y)
            while not pyautogui.locateOnScreen('contas_google.png'):
                time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('nome_conta_class.png', confidence=0.9)
            pyautogui.click(x, y)
            pyautogui.moveTo(1740, 245)
            if pyautogui.locateOnScreen('confirmar identidade conta escola.png'):
                pyautogui.write('12345678')
                pyautogui.moveTo(1740, 245)
                pyautogui.press('enter')
            else:
                pass
            #Entrando na minha sala do classroom
            while not pyautogui.locateOnScreen('nome_da_sala.png'):
                time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('nome_da_sala.png')
            pyautogui.click(x, y)
            time.sleep(1)
            pyautogui.alert(alerta_de_fim)
        else:
            pyautogui.alert(text=alerta_de_fim)
    except:
        pyautogui.alert(text='Algo deu errado, tente novamente.', title='Algo deu errado')

def botao_class():
    pyautogui.PAUSE = 1  # Tempo de execução entre as linhas.

    pyautogui.hotkey('win', 'down')  # Atalho para minimizar a Central de Sites.

    confirmacao = pyautogui.confirm(text=texto_de_confirmacao, title='Confirmação de inicio',
                                    buttons=['Ok', 'Cancelar'])  # Aviso de confirmação.

    if confirmacao == 'Ok':
        pergunta_google_aberto = pyautogui.confirm(text='Você está com o Google aberto?', buttons=['Sim', 'Não'])
        if pergunta_google_aberto == 'Sim':
            pergunta_de_inicio = pyautogui.confirm(text=texto_alerta_inicio_google_aberto, buttons=['Sim', 'Não'])
            if pergunta_de_inicio == 'Sim':
                try:
                    if pyautogui.locateOnScreen('recarregar_pagina.png', confidence=0.9):
                        pyautogui.hotkey('ctrl', 't')
                        while not pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png'):
                            time.sleep(1)
                        pyautogui.write('classroom.google.com')
                        apagar_sugestoes()
                        while not pyautogui.locateOnScreen('googleclassroom.png', confidence=0.9):
                            time.sleep(1)
                        fun_trocar_conta_classroom()
                    else:
                        x, y = pyautogui.locateCenterOnScreen('google aberto.png', confidence=0.9)
                        pyautogui.moveTo(x, y)
                        x, y = pyautogui.locateCenterOnScreen('google aberto barra de tarefas.png', confidence=0.9)
                        pyautogui.moveTo(x, y)
                        time.sleep(0.2)
                        pyautogui.click(x, y)
                        pyautogui.hotkey('ctrl', 't')
                        while not pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png'):
                            time.sleep(1)
                        pyautogui.write('classroom.google.com')
                        apagar_sugestoes()
                        while not pyautogui.locateOnScreen('googleclassroom.png', confidence=0.9):
                            time.sleep(1)
                        fun_trocar_conta_classroom()
                except:
                    contador_vezes2 = 0
                    while not pyautogui.locateOnScreen('recarregar_pagina.png', confidence=0.9):
                        pyautogui.hotkey('alt', 'shift', 'tab')
                        time.sleep(1)
                        contador_vezes2 += 1
                        if contador_vezes2 > 12:
                            break
                        else:
                            pass
                    if contador_vezes2 <= 12:
                        pyautogui.hotkey('ctrl', 't')
                        while not pyautogui.locateOnScreen('barra_pesquisa_google_partedebaixo.png'):
                            time.sleep(1)
                        pyautogui.hotkey('win', 'm')
                        pyautogui.hotkey('alt', 'tab')
                        pyautogui.write('classroom.google.com')
                        apagar_sugestoes()
                        while not pyautogui.locateOnScreen('googleclassroom.png', confidence=0.9):
                            time.sleep(1)
                        fun_trocar_conta_classroom()
                    else:
                        navegador_nao_encontrado = pyautogui.confirm(
                            text='Não foi possivel achar o navegador, posso abrir um novo navegador para o programa ser executado?',
                            title='Navegador não encontrado', buttons=['Sim', 'Não'])
                        if navegador_nao_encontrado == 'Sim':
                            abrir_google_fechado()
                        else:
                            pyautogui.alert(aviso_programa_nao_sera_executado)
            else:
                pyautogui.alert(aviso_programa_nao_sera_executado)
        else:
            confirmar_abrir_google = pyautogui.confirm(text=texto_alerta_inicio_google_fechado, buttons=['Sim', 'Não'])
            if confirmar_abrir_google == 'Sim':
                abrir_google_fechado()
            else:
                pyautogui.alert(aviso_programa_nao_sera_executado)
    else:
        pyautogui.alert(aviso_programa_nao_sera_executado)


#CMSP
def botao_cmsp():
    pyautogui.hotkey('win', 'down')
    time.sleep(1)
    confirmacao = pyautogui.confirm(text=texto_alerta_cmsp, title='Confimação', buttons=['Sim', 'Não'])
    
    if confirmacao == 'Sim':
        navegador = webdriver.Chrome()
        navegador.get('https://cmspweb.ip.tv/')
        #Esperando o site carregar
        while len(navegador.find_elements_by_id('logoImg')) == 0:
            time.sleep(1)
        navegador.find_element_by_id('access-student').click()
        time.sleep(1)
        #Fazendo login
        navegador.find_element_by_id('ra-student').send_keys('000109115172')
        navegador.find_element_by_id('digit-student').send_keys('6')
        navegador.find_element_by_id('password-student').send_keys('sseq7dns')
        navegador.find_element_by_id('btn-login-student').click()
        #Esperando a página principal carregar
        while len(navegador.find_elements_by_name('Canal da 2ª série do Ensino Médio')) == 0:
            time.sleep(1)
        time.sleep(1)
        #Clicando em "Turmas"
        navegador.find_element_by_xpath('//*[@id="chng"]/div[2]').click()
        #Esperando "Turmas" carregar
        while len(navegador.find_elements_by_xpath('//*[@id="lproom_r487e06a2c95e42396-l"]/div/div')) == 0:
            time.sleep(1)
        time.sleep(1)
        #Clicando em "[Turma]2º C ANTONIO LISBOA"
        navegador.find_element_by_xpath('//*[@id="lproom_r487e06a2c95e42396-l"]/div/div').click()
        #Esperando "[Turma]2º C ANTONIO LISBOA" carregar
        while len(navegador.find_elements_by_id('hp__Channel__')) == 0:
            time.sleep(1)
        time.sleep(1)
        #Clicando nas tarefas
        navegador.find_element_by_xpath('//*[@id="channelTaskList"]').click()
        #Mensagem falando que acabou
        time.sleep(1)
        pyautogui.alert('Acabou.')
    else:
        pyautogui.alert(aviso_programa_nao_sera_executado)


def comando_voz():
    #Criando o reconhecedor
    rec = sr.Recognizer()

    #Escutando o mic
    with sr.Microphone(device_index=3) as microfone:
        #Tratando o ruido
        pyautogui.alert('Ajustando ruido...')
        rec.adjust_for_ambient_noise(microfone)
        pyautogui.alert('Pode começar a falar:')
        audio = rec.listen(microfone)
    try:
        global comandos
        comandos = rec.recognize_google(audio, language='pt-BR')
    except:
        pyautogui.alert('Você não falou nada, logo o código não será executado.')        
    #Funções para as falas
    if 'YouTube' in comandos:
        print('YouTube')
    else:
        pass


window = Tk()
window.title('Central de Sites')

window.geometry("744x394")
window.configure(bg = "#4b9990")
canvas = Canvas(
    window,
    bg = "#4b9990",
    height = 394,
    width = 744,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    102.0, 197.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = comando_voz,
    relief = "flat")

b0.place(
    x = 594, y = 350,
    width = 142,
    height = 28)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_cmsp,
    relief = "flat")

b1.place(
    x = 267, y = 165,
    width = 72,
    height = 68)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_class,
    relief = "flat")

b2.place(
    x = 594, y = 49,
    width = 72,
    height = 68)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_hash,
    relief = "flat")

b3.place(
    x = 428, y = 49,
    width = 72,
    height = 68)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_yt,
    relief = "flat")

b4.place(
    x = 267, y = 49,
    width = 72,
    height = 68)

window.resizable(False, False)
window.mainloop()


# time.sleep(5)
# reca = pyautogui.locateOnScreen('Alterar_conta_yt.png', confidence=0.9)
# pyautogui.moveTo(reca)
# #print(len(reca))

# import time
# import pyautogui
# time.sleep(5)
# print(pyautogui.position())