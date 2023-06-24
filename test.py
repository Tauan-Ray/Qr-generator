import tkinter as tk
import qrcode
from PIL import ImageTk




# Criar a janela principal
root = tk.Tk()
root.geometry('400x400')

# Criar a Entry para inserir a URL
entry = tk.Entry(root)
entry.pack()

def gerar_qrcode():
    # Obter a URL da Entry
    url = entry.get()

    # Gerar o QR Code
    qr = qrcode.make(url)

    # Converter o QR Code em um objeto PhotoImage
    qr_image = ImageTk.PhotoImage(qr)
    # Exibir o QR Code na Label
    label = tk.Label(root, image=qr_image, width=330, height=330, compound='center', anchor='center', bg='white', relief='flat')
    label.place(x=10, y=190)
    label.image = qr_image

# Criar o botão para gerar o QR Code
button = tk.Button(root, text="Gerar QR Code", command=gerar_qrcode)
button.pack()

# Criar a Label para exibir o QR Code


root.mainloop()