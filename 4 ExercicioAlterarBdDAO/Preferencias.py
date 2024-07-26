from tkinter import *
from tkinter import ttk, messagebox, Scrollbar
import tkinter as tk
from Business import Preferencias

# Criando cores

corPreta = "#000000"
corBranca = "#feffff"
corPrata = "#c9c9c9"
corCinza = "#708090"
corVerde = "#00b812"


class FrmBancoConectado(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        master.title("Banco Conectado")

        objFrmLstbxPreferencias = FrmLstbxPreferencias(self)
        objFrmLstbxPreferencias.place(x=190, y=5, width=225, height=280)
        objFrmLstbxPreferencias.config(bg=corPrata)

        objFrmBotoesLstbx = FrmBotoesLstbx(self, objFrmLstbxPreferencias, Preferencias)
        objFrmBotoesLstbx.place(x=0, y=5, width=190, height=280)
        objFrmBotoesLstbx.config(bg=corPrata)

        objFrmDtgvwPreferencias = FrmDtgvwPreferencias(self, Preferencias)
        objFrmDtgvwPreferencias.place(x=190, y=280, width=225, height=170)
        objFrmDtgvwPreferencias.config(bg=corPrata)

        objFrmBotoesGrid = FrmBotoesGrid(self, objFrmDtgvwPreferencias)
        objFrmBotoesGrid.place(x=0, y=280, width=190, height=255)
        objFrmBotoesGrid.config(bg=corPrata)


class FrmBotoesLstbx(tk.Frame):
    def __init__(self, master, objFrmLstbxPreferencias, Preferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmLstbxPreferencias = objFrmLstbxPreferencias
        self.Preferencias = Preferencias

        # criando botoes

        btnMensagem = Button(self, text="Mensagem", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.mensagem)
        btnMensagem.grid(row=0, column=0, pady=1, padx=5)
        btnMensagem.config(width=25, height=1)

        btnDesvCond = Button(self, text="Desvio Condicional", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.desvCond)
        btnDesvCond.grid(row=1, column=0, pady=1)
        btnDesvCond.config(width=25, height=1)

        btnDesvEncad = Button(self, text="Desvio Encadeado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.desvEncad)
        btnDesvEncad.grid(row=2, column=0, pady=1)
        btnDesvEncad.config(width=25, height=1)

        btnMatchCase = Button(self, text="Match Case", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.matchCase)
        btnMatchCase.grid(row=3, column=0, pady=1)
        btnMatchCase.config(width=25, height=1)

        btnImpTxtWhile = Button(self, text="Importar Texto While", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impTxtWhile)
        btnImpTxtWhile.grid(row=4, column=0, pady=1)
        btnImpTxtWhile.config(width=25, height=1)

        btnImpTxtFor = Button(self, text="Importar Texto For", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impTxtFor)
        btnImpTxtFor.grid(row=5, column=0, pady=1)
        btnImpTxtFor.config(width=25, height=1)

        btnImpTxtForEach = Button(self, text="Importar Texto ForEach", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                  font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impTxtForEach)
        btnImpTxtForEach.grid(row=6, column=0, pady=1)
        btnImpTxtForEach.config(width=25, height=1)

        btnImpBdConect = Button(self, text="Importar Banco Conectado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impBdConect)
        btnImpBdConect.grid(row=7, column=0, pady=1)
        btnImpBdConect.config(width=25, height=1)

        btnImpBdDesconect = Button(self, text="Importar Banco Desconectado", relief=RAISED, overrelief=RIDGE,
                                   anchor=CENTER,
                                   font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impBdDesconect)
        btnImpBdDesconect.grid(row=8, column=0, pady=1)
        btnImpBdDesconect.config(width=25, height=1)

        btnLimpaTxt = Button(self, text="Limpa Texto", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.limpaTxt)
        btnLimpaTxt.grid(row=9, column=0, pady=1)
        btnLimpaTxt.config(width=25, height=1)

    def mensagem(self):
        messagebox.showinfo(title="Mensagem", message="Bem vindo ao meu programa Python")

    def desvCond(self):
        if messagebox.askokcancel("Desvio Condicional", "ESCOLHA UMA OPÇÃO"):
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU OK")
        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")

    def desvEncad(self):
        resultadoDosBotoes = messagebox.askyesnocancel("Desvio Condicional", "ESCOLHA UMA OPÇÃO")
        if resultadoDosBotoes == True:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
        elif resultadoDosBotoes == False:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")

    def matchCase(self):
        resultado = messagebox.askyesnocancel("Desvio Condicional", "ESCOLHA UMA OPÇÃO")
        match resultado:
            case True:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
            case False:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
            case None:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")
            case _:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU OUTRA OPÇÃO")

    def impTxtWhile(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtWhile():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impTxtFor(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtFor():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impTxtForEach(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtForEach():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impBdConect(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impBdConect():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impBdDesconect(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impBdDesconect():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def limpaTxt(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()


class FrmLstbxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.lstbxPreferencias = Listbox(self, relief=GROOVE, selectmode=MULTIPLE, font="Roboto 8 bold",
                                         bg=corBranca, fg=corPreta, selectbackground=corVerde,
                                         selectforeground=corPreta, activestyle="none",
                                         height=23, width=23)
        self.lstbxPreferencias.place(x=5, y=1, width=200, height=270)

        barraRolagem = Scrollbar(self, orient=VERTICAL, command=self.lstbxPreferencias.yview)
        barraRolagem.place(x=205, y=1, width=15, height=270)
        self.lstbxPreferencias.config(yscrollcommand=barraRolagem.set)

    def limpaTxtPreferencias(self):
        self.lstbxPreferencias.delete(0, END)

    def atualizarLista(self, preferencias):
        self.lstbxPreferencias.delete(0, END)
        for item in preferencias:
            self.lstbxPreferencias.insert(END, item)


class FrmBotoesGrid(tk.Frame):
    def __init__(self, master, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        btnConsultarBd = Button(self, text="Consultar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                                command=self.objFrmDtgvwPreferencias.consultarBd)
        btnConsultarBd.grid(row=0, column=0, pady=1, padx=5)
        btnConsultarBd.config(width=25, height=1)

        btnInserirBd = Button(self, text="Inserir", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                              command=self.objFrmDtgvwPreferencias.inserirBd)
        btnInserirBd.grid(row=1, column=0, pady=1)
        btnInserirBd.config(width=25, height=1)

        btnDeletarBd = Button(self, text="Deletar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                              command=self.objFrmDtgvwPreferencias.excluirBd)
        btnDeletarBd.grid(row=2, column=0, pady=1)
        btnDeletarBd.config(width=25, height=1)

        btnAlterarBd = Button(self, text="Alterar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                              command=self.objFrmDtgvwPreferencias.alterarBd)
        btnAlterarBd.grid(row=3, column=0, pady=1)
        btnAlterarBd.config(width=25, height=1)

        btnLimparBd = Button(self, text="Limpar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                             command=self.objFrmDtgvwPreferencias.limpaGrid)
        btnLimparBd.grid(row=4, column=0, pady=1)
        btnLimparBd.config(width=25, height=1)


class FrmDtgvwPreferencias(tk.Frame):
    def __init__(self, master, Preferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.Preferencias = Preferencias

        self.colunas = ["ID", "Descricao"]
        self.tamanhosColunas = [10, 90]
        self.ancoramentoColunas = [tk.W, tk.W, ]

        self.colunas = ["ID", "Descricao"]
        self.dtgvwPreferencias = tk.ttk.Treeview(self, columns=self.colunas, show="headings")
        self.dtgvwPreferencias.place(x=5, y=1, width=200, height=135)

        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i], text=self.colunas[i], anchor=self.ancoramentoColunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhosColunas[i],
                                          anchor=self.ancoramentoColunas[i])

        # Criando estilo da grid

        estiloGrid = ttk.Style()
        estiloGrid.theme_use("clam")
        estiloGrid.configure("Treeview.Heading", font="Roboto 8 bold", background=corCinza, foreground=corBranca,
                             anchor=tk.W)
        estiloGrid.configure("Treeview", font="Roboto 8 bold", background=corBranca, foreground=corPreta)

        barraRolagem = Scrollbar(self, orient=VERTICAL, command=self.dtgvwPreferencias.yview)
        barraRolagem.place(x=205, y=1, width=15, height=135)
        self.dtgvwPreferencias.config(yscrollcommand=barraRolagem.set)

        self.refreshGrid()

    def limpaGrid(self):
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())



    def consultBd(self, parPreferenciasDescricao=None):
        try:
            objPreferencias = Preferencias()
            self.limpaGrid()
            return objPreferencias.consultBd(parPreferenciasDescricao)
        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def consultarBd(self):
        try:
            objFrmConsultarPreferencias = FrmConsultarPreferencias(self)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def inserirBd(self):
        try:
            objFrmInserirPreferencias = FrmInserirPreferencias(self)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def excluirBd(self):
        try:
            objFrmDeletarPreferencias = FrmDeletarPreferencias(self)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def alterarBd(self):
        try:
            objFrmAlterarPreferencias = FrmAlterarPreferencias(self)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def refreshGrid(self, registro=None):
        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhosColunas[i],
                                          anchor=self.ancoramentoColunas[i])

        if registro == None:
            linhas = self.consultBd()
        else:
            linhas = registro
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

        for linhaBd in linhas:
            self.dtgvwPreferencias.insert("", END, values=list(linhaBd))


class FrmConsultarPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        self.title("CONSULTAR PREFERENCIAS")

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=X)

        self.btnConsultar = tk.Button(self, text="Consultar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                      font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.consultarBd)
        self.btnConsultar.pack(side=TOP, pady=5)

    def consultarBd(self):
        descricao = self.entPreferencias.get()

        if messagebox.askokcancel("Confirmação", "Deseja realmente consultar as preferencias?"):
            try:
                self.objFrmDtgvwPreferencias.refreshGrid(self.objFrmDtgvwPreferencias.consultBd(descricao))

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
        self.destroy()


class FrmInserirPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        self.title("INSERIR PREFERENCIAS")

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=NONE, padx=5, pady=5)

        self.btnInserir = tk.Button(self, text="INSERIR", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                    font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.inserirBd)
        self.btnInserir.pack(side=TOP, pady=5)

    def inserirBd(self):

        if messagebox.askokcancel("Confirmação", f"Deseja realmente inserir a preferencia"
                                                 f" {self.entPreferencias.get()}?") == True:
            try:
                descricao = self.entPreferencias.get()
                objPreferencias = Preferencias()

                if objPreferencias.inserirBd(descricao):
                    messagebox.showinfo("SUCESSO", f"A preferencia {descricao} foi inserida com sucesso!")
                    self.objFrmDtgvwPreferencias.limpaGrid()
                    self.objFrmDtgvwPreferencias.refreshGrid()

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
        self.destroy()

class FrmDeletarPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        self.title("DELETAR PREFERENCIAS")
        self.configure(bg=corBranca, bd=1, relief=SUNKEN, padx=50, pady=30)

        self.indiceLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.focus()
        self.itemDaLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.item(self.indiceLinhaSelecionada)
        self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
        self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][1]

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=NONE)

        self.btnExcluir = tk.Button(self, text="DELETAR", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                    font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.deletarBd)
        self.btnExcluir.pack(side=TOP, pady=5)

        self.mainloop()

    def deletarBd(self):

        if (messagebox.askokcancel("EXCLUIR PREFERENCIAS", f"Deseja realmente excluir a preferencia"
                                                           f" {self.entPreferencias.get()}?") == True):

            try:
                objPreferencias = Preferencias()
                idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]

                if objPreferencias.excluirBd(idItemDaLinhaSelecionada):
                    messagebox.showinfo("SUCESSO", "A preferencia foi deletada com sucesso!")
                    self.objFrmDtgvwPreferencias.limpaGrid()
                    self.objFrmDtgvwPreferencias.refreshGrid()

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
        self.destroy()


class FrmAlterarPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        self.title("ALTERAR PREFERENCIAS")
        self.configure(bg=corBranca, bd=1, relief=SUNKEN, padx=50, pady=30)

        self.indiceLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.focus()
        self.itemDaLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.item(self.indiceLinhaSelecionada)
        self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
        self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][1]

        self.lblDescricao = FrmLabel(self, self.descricaoItemDaLinhaSelecionada)
        self.lblDescricao.pack(side=TOP, padx=5, pady=5)

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=NONE, padx=5, pady=5)

        self.btnAlterar = tk.Button(self, text="ALTERAR", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                    font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.alterarBd)
        self.btnAlterar.pack(side=TOP, pady=5)

        self.mainloop()

    def alterarBd(self):

        if (messagebox.askokcancel("ALTERAR PREFERENCIAS", f"Deseja realmente alterar a preferencia"
                                                           f" {self.lblDescricao.get()}?" f"pela a Preferencia"
                                                           f" {self.entPreferencias.get()}?") == True):

            try:
                objPreferencias = Preferencias()
                descricao = self.entPreferencias.get()
                idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]

                if objPreferencias.alterarBd(descricao, idItemDaLinhaSelecionada):
                    messagebox.showinfo("SUCESSO", "A preferencia foi Alterada com sucesso!")
                    self.objFrmDtgvwPreferencias.limpaGrid()
                    self.objFrmDtgvwPreferencias.refreshGrid()

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
        self.destroy()


class FrmEntry(tk.Frame):
    def __init__(self, master, descricao, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType

        self.lblDescricao = tk.Label(self, text=descricao, font="Roboto 8 bold", bg=corBranca, fg=corPreta,
                                     anchor=CENTER, relief=FLAT)

        self.lblDescricao.pack(side=TOP, fill=NONE)

        self.entDescricao = tk.Entry(self, font="Roboto 8 bold", bg=corBranca, fg=corPreta, relief=GROOVE,
                                     textvariable=tk.StringVar())
        self.entDescricao.pack(side=BOTTOM, anchor=CENTER)

    def get(self):
        valor = self.entDescricao.get()

        try:
            return self.varType(valor)
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.entDescricao.delete(0, tk.END)
        self.entDescricao.insert(0, valor)


class FrmLabel(tk.Frame):
    def __init__(self, master, labelTxt, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType
        self.labelTxt = labelTxt

        self.lblDescricao = tk.Label(self, text=self.labelTxt, font="Roboto 8 bold", bg=corBranca, fg=corPreta,
                                     anchor=CENTER, relief=FLAT)
        self.lblDescricao.pack(side=TOP, fill=NONE)

    def get(self):
        valor = self.labelTxt

        try:
            return self.varType(valor)
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.labelTxt = valor
