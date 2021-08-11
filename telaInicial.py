# -- coding: utf-8 --
from tkinter import * # GUI nativo do python
from PIL import ImageTk, Image # responsavel pela entrada de imagens para a linguagem e fornece recursos de edicao
from colour import Color # permite atribuir cores rgb a um objeto
import popUpMessage # classe responsavel por apresentar um popup antes de iniciar a aplicacao em si
import pygame # responsavel pela reproducao e edicao de arquivos de som
import os


red = Color('#6b0000')

# Criando e configurando a tela
root = Tk(className=' Tela Inicial')
root.resizable(0,0)

canvas = Canvas(root, width=600, height=600)
canvas.grid(columnspan=5,rowspan=16)

icon = PhotoImage(file='imagens/logoPI_v5.png')
root.iconphoto(False, icon)

# Criando as funções para cada botão
def onBotIniciar():
    popUpMessage.callme()
    os.system('python detect_mask_video.py')

def onBotConfig():
    os.system('python rodaTelaConfig.py')

def onBotSair():
    quit()

# Criando funções para o botão quando o mouse passar em cima
def mouseEmcimaA(e):
    bot1['background'] = 'gray'
    getSomMouseOn()

def mouseEmcimaB(e):
    bot2['background'] = 'gray'
    getSomMouseOn()

def mouseEmcimaC(e):
    bot3['background'] = red
    getSomMouseOn()

def mouseFora(e):
    bot1['background'] = 'black'
    bot2['background'] = 'black'
    bot3['background'] = 'black'

def getSomMouseOn():
	pygame.mixer.init()
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.load("audios/alerta_click.mp3")
	pygame.mixer.music.play(loops = 0)

# Criando os botões 'Iniciar', 'Configurações' e 'Sair'
bot1 = Button(root, text="Iniciar", borderwidth=0, height=2, width=15, fg="white", bg="black", font=('Raleway', 10, 'bold'), command=onBotIniciar) 
bot2 = Button(root, text="Configurações", borderwidth=0, height=2, width=15, fg="white", bg="black", font=('Raleway', 10, 'bold'), command=onBotConfig) 
bot3 = Button(root, text="Sair", borderwidth=0, height=2, width=15, fg="white", bg="black", font=('Raleway', 10, 'bold'), command=onBotSair)

# Inserindo a logo
img_logo = Image.open("imagens/logoPI_v6.png")
resize_logo = img_logo.resize((300,300), Image.ANTIALIAS)
get_logo = ImageTk.PhotoImage(resize_logo)
logo = Label(root, image=get_logo)

# Posicionando o necessário na tela
logo.grid(row=3,column=2)

bot1.grid(row=7, column=2)
bot2.grid(row=8, column=2)
bot3.grid(row=9, column=2)

bot1.bind("<Enter>", mouseEmcimaA)
bot2.bind("<Enter>", mouseEmcimaB)
bot3.bind("<Enter>", mouseEmcimaC)

bot1.bind("<Leave>", mouseFora)
bot2.bind("<Leave>", mouseFora)
bot3.bind("<Leave>", mouseFora)

# Rodando o software
root.mainloop()
