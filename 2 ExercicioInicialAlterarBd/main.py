import tkinter

from alterarBanco import *

janela = tk.Tk()
janela.geometry("380x425")

# Criando objeto de classe banco conectado

objFrmBancoConectado = FrmBancoConectado(janela)
objFrmBancoConectado.pack(fill=tkinter.BOTH, expand=True)

janela.mainloop()