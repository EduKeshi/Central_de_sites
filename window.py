from tkinter import *

def btn_clicked():
    print("Button Clicked")


window = Tk()

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
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 267, y = 165,
    width = 72,
    height = 68)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 594, y = 49,
    width = 72,
    height = 68)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 428, y = 49,
    width = 72,
    height = 68)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 267, y = 49,
    width = 72,
    height = 68)

window.resizable(False, False)
window.mainloop()
