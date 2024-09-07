from tkinter import *
from tkinter import ttk, messagebox, Scrollbar
import tkinter as tk
from Business.Preferencias import *
from MODEL.PreferenciasVO import PreferenciasVO

# Criando Cores

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

        objFrmDtgvwPreferencias = FrmDtgvwPreferencias(self, Preferencias, PreferenciasVO)
        objFrmDtgvwPreferencias.place(x=190, y=280, width=225, height=170)
        objFrmDtgvwPreferencias.config(bg=corPrata)

        objFrmBotoesDtgvw = FrmBotoesDtgvw(self, objFrmDtgvwPreferencias)
        objFrmBotoesDtgvw.place(x=0, y=280, width=190, height=255)
        objFrmBotoesDtgvw.config(bg=corPrata)


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
                                   anchor=CENTER, font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                                   command=self.impBdDesconect)
        btnImpBdDesconect.grid(row=8, column=0, pady=1)
        btnImpBdDesconect.config(width=25, height=1)

        btnLimpTxt = Button(self, text="Limpar texto", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                            font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.limpaTxt)
        btnLimpTxt.grid(row=9, column=0, pady=1)
        btnLimpTxt.config(width=25, height=1)

    @staticmethod
    def mensagem():
        messagebox.showinfo(title="Mensagem", message="Bem vindo ao meu programa Python")

    @staticmethod
    def desvCond():
        if messagebox.askokcancel("Desvio Condicional", "ESCOLHA UMA OPÇÃO"):
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU OK")
        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")

    @staticmethod
    def desvEncad():
        resultadoDosBotoes = messagebox.askyesnocancel("Desvio Condicional", "ESCOLHA UMA OPÇÃO")
        if resultadoDosBotoes is True:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
        elif resultadoDosBotoes is False:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")

    @staticmethod
    def matchCase():
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
        self.objFrmLstbxPreferencias.limparTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtWhile():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impTxtFor(self):
        self.objFrmLstbxPreferencias.limparTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtFor():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impTxtForEach(self):
        self.objFrmLstbxPreferencias.limparTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtForEach():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impBdConect(self):
        self.objFrmLstbxPreferencias.limparTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impBdConect():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def impBdDesconect(self):
        self.objFrmLstbxPreferencias.limparTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impBdDesconect():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def limpaTxt(self):
        self.objFrmLstbxPreferencias.limparTxtPreferencias()


class FrmLstbxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.lstbxPreferencias = tk.Listbox(self, relief=GROOVE, selectmode=MULTIPLE, bg=corBranca, fg=corPreta,
                                            font="Roboto 8 bold", selectbackground=corVerde,
                                            activestyle="none", width=23, height=23)
        self.lstbxPreferencias.place(x=5, y=1, width=200, height=270)

        barraDeRolagem = Scrollbar(self, orient="vertical", command=self.lstbxPreferencias.yview)
        barraDeRolagem.place(x=205, y=1, width=15, height=270)
        self.lstbxPreferencias.config(yscrollcommand=barraDeRolagem.set)

    def limparTxtPreferencias(self):
        self.lstbxPreferencias.delete(0, tk.END)

    def atualizarLista(self, preferencias):
        self.limparTxtPreferencias()
        for item in preferencias:
            self.lstbxPreferencias.insert(tk.END, item)


class FrmBotoesDtgvw(tk.Frame):
    def __init__(self, master, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        btnConsultarBd = Button(self, text="ConsultarBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                                command=self.objFrmDtgvwPreferencias.consultarBd)
        btnConsultarBd.grid(row=0, column=0, pady=1, padx=5)
        btnConsultarBd.config(width=25, height=1)

        btnInserirBd = Button(self, text="InserirBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                              command=self.objFrmDtgvwPreferencias.inserirBd)
        btnInserirBd.grid(row=1, column=0, pady=1)
        btnInserirBd.config(width=25, height=1)

        btnExcluirBd = Button(self, text="ExcluirBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                              command=self.objFrmDtgvwPreferencias.excluirBd)
        btnExcluirBd.grid(row=2, column=0, pady=1)
        btnExcluirBd.config(width=25, height=1)

        btnAlterarBd = Button(self, text="AlterarBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                              command=self.objFrmDtgvwPreferencias.alterarBd)
        btnAlterarBd.grid(row=3, column=0, pady=1)
        btnAlterarBd.config(width=25, height=1)

        btnLimpGrid = Button(self, text="Limpar Banco", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca,
                             command=self.objFrmDtgvwPreferencias.limparGrid)
        btnLimpGrid.grid(row=4, column=0, pady=1)
        btnLimpGrid.config(width=25, height=1)


class FrmDtgvwPreferencias(tk.Frame):
    def __init__(self, master, Preferencias, objPreferenciasVO, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.Preferencias = Preferencias
        objPreferenciasVO = PreferenciasVO()

        self.colunas = ["ID", "Descricao"]
        self.tamanhaColunas = [10, 90]
        self.ancoramentoDasColunas = [tk.W, tk.W, ]

        self.colunas = ["ID", "Descricao"]
        self.dtgvwPreferencias = tk.ttk.Treeview(self, columns=self.colunas, show="headings")
        self.dtgvwPreferencias.place(x=5, y=1, width=200, height=135)

        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i], text=self.colunas[i], anchor=self.ancoramentoDasColunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhaColunas[i],
                                          anchor=self.ancoramentoDasColunas[i])

        linhas = self.consultBd(objPreferenciasVO)
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

        for linhasBd in linhas:
            values = [linhasBd.ID, linhasBd.Descricao]
            self.dtgvwPreferencias.insert('', 'end', values=values)

        # Criando estilo Grid

        estiloGrid = ttk.Style()
        estiloGrid.theme_use("clam")
        estiloGrid.configure("Treeview.Heading", font="Roboto 8 bold", background=corCinza, foregraund=corBranca,
                             anchor=tk.W)
        estiloGrid.configure("Treeview", font="Roboto 8", background=corBranca, foreground=corPreta)

        barraRolagem = Scrollbar(self, orient=VERTICAL, command=self.dtgvwPreferencias.yview)
        barraRolagem.place(x=205, y=1, width=15, height=135)
        self.dtgvwPreferencias.config(yscrollcommand=barraRolagem.set)

    def limparGrid(self):
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

    def consultBd(self, objPreferenciasVO):
        try:
            objPreferencias = Preferencias()
            self.limparGrid()
            return objPreferencias.consultBd(objPreferenciasVO)
        except Exception as e:
            messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))

    def consultarBd(self):
        try:
            objFrmConsPreferencias = FrmConsPreferencias(self)

        except Exception as ex:
            messagebox.showinfo("ERRO", "OCORREU UM ERRO" + str(ex))

    def inserirBd(self):
        try:
            objFrmAddPreferencias = FrmAddPreferencias(self)

        except Exception as ex:
            messagebox.showinfo("ERRO", "OCORREU UM ERRO" + str(ex))

    def excluirBd(self):
        try:
            objFrmDelPreferencias = FrmDelPreferencias(self)

        except Exception as ex:
            messagebox.showinfo("ERRO", "OCORREU UM ERRO" + str(ex))

    def alterarBd(self):
        try:
            objFrmAltPreferencias = FrmAltPreferencias(self)

        except Exception as ex:
            messagebox.showinfo("ERRO", "OCORREU UM ERRO" + str(ex))

    def refreshGrid(self, registro=None):
        objPreferenciasVO = PreferenciasVO()
        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhaColunas[i],
                                          anchor=self.ancoramentoDasColunas[i])

        if registro is None:
            linhas = self.consultBd(objPreferenciasVO)
        else:
            linhas = registro
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

        for linhaBd in linhas:
            self.dtgvwPreferencias.insert("", END, values=list(linhaBd))


class FrmConsPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

        self.title("CONSULTAR PREFERENCIAS")

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=NONE, padx=5, pady=5)

        self.btnConsultar = tk.Button(self, text="Consultar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                      font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.consultarBd)
        self.btnConsultar.pack(side=TOP, pady=5)

    def consultarBd(self):
        descricao = self.entPreferencias.get()

        if messagebox.askokcancel("Confirmação", f"Deseja realmente consultar a preferencia {descricao} ?"):
            try:
                objPreferenciasVO = PreferenciasVO(descricao=descricao)
                self.objFrmDtgvwPreferencias.refreshGrid(self.objFrmDtgvwPreferencias.consultBd(objPreferenciasVO))

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
        self.destroy()


class FrmAddPreferencias(tk.Tk):
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
        descricao = self.entPreferencias.get()

        if messagebox.askokcancel("Confirmação", f"Deseja realmente inserir a preferencia {descricao} ?"):

            try:
                objPreferenciasVO = PreferenciasVO(descricao=descricao)
                objPreferencias = Preferencias()

                if objPreferencias.inserirBd(objPreferenciasVO):
                    messagebox.showinfo("SUCESSO", f"A preferencia {descricao} foi inserida com sucesso!")
                    self.objFrmDtgvwPreferencias.limparGrid()
                    self.objFrmDtgvwPreferencias.refreshGrid()

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
            finally:
                self.destroy()
        else:
            self.destroy()


class FrmDelPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:

            self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

            self.title("DELETAR PREFERENCIAS")

            self.indiceLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.focus()
            self.itemDaLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.item(
                self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][1]

            self.entPreferencias = FrmEntry(self, "Descricao")
            self.entPreferencias.pack(side=TOP, fill=NONE, padx=5, pady=5)

            self.btnExcluir = tk.Button(self, text="DELETAR", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                        font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.deletarBd)
            self.btnExcluir.pack(side=TOP, pady=5)

            self.mainloop()
        except Exception as ex:
            self.destroy()
            messagebox.showinfo('Erro', 'Selecione uma linha para Excluí-la' + str(ex))

    def deletarBd(self):
        id = self.idItemDaLinhaSelecionada

        if (messagebox.askokcancel("EXCLUIR PREFERENCIAS", f"Deseja realmente excluir a preferencia"
                                                           f" {self.entPreferencias.get()}?") == True):
            try:
                objPreferencias = Preferencias()
                objPreferenciasVO = PreferenciasVO(iD=id)

                if objPreferencias.excluirBd(objPreferenciasVO):
                    messagebox.showinfo("SUCESSO", "A preferencia foi deletada com sucesso!")
                    self.objFrmDtgvwPreferencias.limparGrid()
                    self.objFrmDtgvwPreferencias.refreshGrid()

                else:
                    messagebox.showinfo("ERRO", "A preferencia não pode ser excluída!")

            except Exception as e:
                messagebox.showerror("ERRO", "Ocorreu um erro: " + str(e))
        self.destroy()


class FrmAltPreferencias(tk.Tk):
    def __init__(self, objFrmDtgvwPreferencias, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.objFrmDtgvwPreferencias = objFrmDtgvwPreferencias

            self.title("ALTERAR PREFERENCIAS")

            self.indiceLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.focus()
            self.itemDaLinhaSelecionada = self.objFrmDtgvwPreferencias.dtgvwPreferencias.item(
                self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][1]

            self.lblDescricao = FrmLabel(self, self.descricaoItemDaLinhaSelecionada)
            self.lblDescricao.pack(side=TOP, padx=5, pady=5)

            self.entPreferencias = FrmEntry(self, "Por:")
            self.entPreferencias.pack(side=TOP, fill=NONE, padx=5, pady=5)

            self.btnAlterar = tk.Button(self, text="ALTERAR", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                        font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.alterarBd)
            self.btnAlterar.pack(side=TOP, pady=5)

            self.mainloop()
        except Exception as ex:
            self.destroy()
            messagebox.showinfo('Erro', 'Selecione uma linha para Alterar' + str(ex))

    def alterarBd(self):
        id = self.idItemDaLinhaSelecionada

        if (messagebox.askokcancel("ALTERAR PREFERENCIAS", f"Deseja realmente alterar a preferencia"
                                                           f" {self.lblDescricao.get()}?" f"pela a Preferencia"
                                                           f" {self.entPreferencias.get()}?") == True):

            try:

                objPreferencias = Preferencias()
                novaDescricao = self.entPreferencias.get()
                objPreferenciasVO = PreferenciasVO(iD=id, descricao=novaDescricao)

                if objPreferencias.alterarBd(objPreferenciasVO):
                    messagebox.showinfo("SUCESSO", "A preferencia foi Alterada com sucesso!")
                    self.objFrmDtgvwPreferencias.limparGrid()
                    self.objFrmDtgvwPreferencias.refreshGrid()

                else:
                    messagebox.showerror("ERRO", "A preferencia não foi alterada!")

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
