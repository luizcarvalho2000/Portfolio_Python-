from alterarBanco import *


janela = tk.Tk()
janela.geometry('380x425')

# Criando Objetos de classe banco Conectado

objFrmBancoConectado = FrmBancoConectado(janela)
objFrmBancoConectado.pack(fill=tk.BOTH, expand=True)

janela.mainloop()
