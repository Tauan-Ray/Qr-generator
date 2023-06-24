import qrcode
from PIL import ImageTk
import tkinter as tk

# Criar a janela
janela = tk.Tk()
janela.geometry('800x800')

urlEntry = tk.Entry(janela, width=20, justify='left', relief='solid', borderwidth=1)
urlEntry.place(x=150, y=67)

qr_button = tk.Button(janela, text='Gerar Qr Code', width=13, height=1, anchor='center', font=('Ivy 10 bold'), relief='raised', overrelief='sunken', bg='gray', fg='white', borderwidth=2)
qr_button.place(x=280, y=61)

# Executar a janela
janela.mainloop()