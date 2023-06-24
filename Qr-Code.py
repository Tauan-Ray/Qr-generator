from tkinter import *
from PIL import Image, ImageTk
import qrcode

# Cores
background = '#FFFFFF'
font = '#242424'
button = '#353535'

app = Tk()
app.title('Gerador de Qr Code')
app.geometry('400x400')
app.config(bg=background)

# Fazendo cabeçalho
header = Frame(app, width=401, height=45, relief='raised', bg=background, borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Qr Code Generator', width=15, height=1, font=('Arial 15 bold') ,relief='flat', bg=background, fg=font)
titleHeader.place(x=110, y=8)

# Criando Label e entry para link
urlText = Label(app, text='Insira a URL aqui \u2192', width=15, height=1, font=('Arial 11'), relief='flat', bg=background, fg=font)
urlText.place(x=10, y=65)

urlEntry = Entry(app, width=20, justify='left', relief='solid', borderwidth=1)
urlEntry.place(x=150, y=67)

# Criando função que gera Qr Code
def generator():
    url = urlEntry.get()


    imgQr_Code = Label(app, width=80, height=80, compound='center', anchor='center', bg=background, relief='flat')
    imgQr_Code.place(x=10, y=190)



# Criando botão para fazer qr code
qr_button = Button(app, command=generator ,text='Gerar Qr Code', width=13, height=1, anchor='center', font=('Ivy 10 bold'), relief='raised', overrelief='sunken', bg=button, fg='white', borderwidth=2)
qr_button.place(x=280, y=61)

app.mainloop()
