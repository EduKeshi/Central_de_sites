from tkinter import *

import botao_youtube
import botao_classroom
import botao_hashtag
import botao_cmsp
import comandos_de_voz

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

fundo_da_tela = PhotoImage(file = "imagens_da_tela_principal/background.png")
fundo = canvas.create_image(
    102.0, 
    197.0,
    image=fundo_da_tela)

botao_comandos_de_voz = PhotoImage(file = "imagens_da_tela_principal/botao_comandos_de_voz.png")
botao_1 = Button(
    image = botao_comandos_de_voz,
    borderwidth = 0,
    highlightthickness = 0,
    command = comandos_de_voz.comando_voz,
    relief = "flat")

botao_1.place(
    x = 594, 
    y = 350,
    width = 142,
    height = 28)

imagem_botao_cmsp = PhotoImage(file = "imagens_da_tela_principal/imagem_botao_cmsp.png")
botao_2 = Button(
    image = imagem_botao_cmsp,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_cmsp.entra_no_site_da_aula,
    relief = "flat")

botao_2.place(
    x = 267, 
    y = 165,
    width = 72,
    height = 68)

imagem_botao_classroom = PhotoImage(file = "imagens_da_tela_principal/imagem_botao_classroom.png")
botao_3 = Button(
    image = imagem_botao_classroom,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_classroom.abrir_classroom,
    relief = "flat")

botao_3.place(
    x = 594, 
    y = 49,
    width = 72,
    height = 68)

imagem_botao_curso = PhotoImage(file = "imagens_da_tela_principal/imagem_botao_curso.png")
botao_4 = Button(
    image = imagem_botao_curso,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_hashtag.entrar_no_curso,
    relief = "flat")

botao_4.place(
    x = 428, 
    y = 49,
    width = 72,
    height = 68)

imagem_botao_youtube = PhotoImage(file = "imagens_da_tela_principal/imagem_botao_youtube.png")
botao_5 = Button(
    image = imagem_botao_youtube,
    borderwidth = 0,
    highlightthickness = 0,
    command = botao_youtube.abre_em_uma_janela_nova_ou_uma_existente,
    relief = "flat")

botao_5.place(
    x = 267, 
    y = 49,
    width = 72,
    height = 68)

window.resizable(False, False)
window.mainloop()