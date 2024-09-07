from frmPreferencias import *

janela = tk.Tk()
janela.geometry("415x450")
janela.resizable(False, False)

objFrmBancoConectado = FrmBancoConectado(janela)
objFrmBancoConectado.pack(fill=tk.BOTH, expand=True)

janela.mainloop()
