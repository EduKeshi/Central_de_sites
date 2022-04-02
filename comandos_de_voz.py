import pyautogui
import speech_recognition as sr

import botao_youtube
import botao_classroom
import botao_hashtag
import botao_cmsp

def comando_voz():
    # Criando o reconhecedor
    reconhecedor_de_voz = sr.Recognizer()

    # Escutando o mic
    with sr.Microphone() as microfone:
        # Tratando o ruido
        pyautogui.alert("Ajustando ruido...")
        reconhecedor_de_voz.adjust_for_ambient_noise(microfone)
        pyautogui.alert("Aperte 'Ok' e comece a falar")
        audio_do_microfone = reconhecedor_de_voz.listen(microfone)
        
    try:
        comandos = reconhecedor_de_voz.recognize_google(audio_do_microfone, language = "pt-BR")
        print(comandos)       
    except sr.UnknownValueError:
        print("Não consegui te escutar")
        return
    
    # Funções para as falas
    if "YouTube" in comandos:
        botao_youtube.abre_em_uma_janela_nova_ou_uma_existente()
    elif "lições" in comandos:
        botao_classroom.abrir_classroom()
    elif "curso" in comandos:
        botao_hashtag.entrar_no_curso()
    elif "aulas" in comandos:
        botao_cmsp.entra_no_site_da_aula()