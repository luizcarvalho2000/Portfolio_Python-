from Preferencias import *

janela = tk.Tk()
janela.geometry("380x425")

objFrmBancoConectado = FrmBancoConectado(janela)
objFrmBancoConectado.pack(fill=tk.BOTH, expand=True)

janela.mainloop()
