from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

# Cores
Colorbackground = '#FFFFFF'
Colorfont = '#242424'
Colorbutton = '#353535'
Fontbutton = '#FFFFFF'

app = Tk()
app.title('Gerador de Qr Code')
app.geometry('400x480')
app.config(bg=Colorbackground)

# Fazendo cabeçalho
header = Frame(app, width=401, height=45, relief='raised',
               bg=Colorbackground, borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Qr Code Generator', width=15, height=1, font=(
    'Arial 15 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
titleHeader.place(x=110, y=8)

# Criando Label e entry para link
urlText = Label(app, text='Insira a URL aqui \u2192', width=15, height=1, font=(
    'Arial 11'), relief='flat', bg=Colorbackground, fg=Colorfont)
urlText.place(x=10, y=65)

urlEntry = Entry(app, width=20, justify='left', relief='solid', borderwidth=1)
urlEntry.place(x=150, y=67)

# Criando função que gera Qr Code
def generator():
    # Pegando url e criando imagem Qr Code
    url = urlEntry.get()
    qr = qrcode.make(url)
    imageQr = ImageTk.PhotoImage(qr)

    # Fazendo label que mostra Qr Code
    imgQr_Code = Label(app, image=imageQr, width=320, height=320,
                       compound='center', anchor='center', bg=Colorbackground, relief='flat')
    imgQr_Code.place(x=18, y=110)
    imgQr_Code.image = imageQr

    # Função para salvar imagem
    def download():
        imgSave = asksaveasfilename()

        if imgSave == '':
            pass

        else:
            qr.save(imgSave + '.png')

            messagebox.showinfo('Sucesso!!!!',
                                'Sua imagem foi baixada com sucesso.')

    # Função para resetar app   
    def reset():
        urlEntry.delete(0, END)
        imgQr_Code.destroy()
        download_button.destroy()
        reset_button.destroy()

    download_button = Button(app, command=download, text='Clique aqui para download', width=21, height=1, anchor='center', font=(
        'Arial 10 bold'), relief='raised', overrelief='sunken', bg=Colorbutton, fg=Fontbutton, borderwidth=2)
    download_button.place(x=30, y=440)

    reset_button = Button(app, command=reset ,text='Reset', width=10, height=1, anchor='center', font=(
        'Arial 10 bold'), relief='raised', overrelief='sunken', bg=Colorbutton, fg=Fontbutton, borderwidth=2)
    reset_button.place(x=220, y=440)

# Criando botão para fazer qr code
qr_button = Button(app, command=generator, text='Gerar Qr Code', width=13, height=1, anchor='center', font=(
    'Ivy 10 bold'), relief='raised', overrelief='sunken', bg=Colorbutton, fg=Fontbutton, borderwidth=2)
qr_button.place(x=280, y=61)

app.mainloop()
