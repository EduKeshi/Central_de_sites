from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import speech_recognition as sr
from tkinter import *

import botao_youtube
import botao_classroom
import botao_hashtag
import botao_cmsp

# def comando_voz():
#     #Criando o reconhecedor
#     rec = sr.Recognizer()

#     #Escutando o mic
#     with sr.Microphone(device_index=3) as microfone:
#         #Tratando o ruido
#         pyautogui.alert('Ajustando ruido...')
#         rec.adjust_for_ambient_noise(microfone)
#         pyautogui.alert('Pode começar a falar:')
#         audio = rec.listen(microfone)
#     try:
#         global comandos
#         comandos = rec.recognize_google(audio, language='pt-BR')
#     except:
#         pyautogui.alert('Você não falou nada, logo o código não será executado.')        
#     #Funções para as falas
#     if 'YouTube' in comandos:
#         print('YouTube')
#     else:
#         pass

def comando_voz():
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
    command = botao_cmsp.entra_no_site_da_aula,
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
    command = botao_classroom.abrir_classroom,
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
    command = botao_hashtag.entrar_no_curso,
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
    command = botao_youtube.abre_em_uma_janela_nova_ou_uma_existente,
    relief = "flat")

b4.place(
    x = 267, y = 49,
    width = 72,
    height = 68)

window.resizable(False, False)
window.mainloop()
