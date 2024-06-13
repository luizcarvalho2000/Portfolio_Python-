from tkinter import *
from tkinter import ttk, messagebox, Scrollbar
import tkinter as tk
from Business import Preferencias

# Criando Cores

corPreta = "#000000"
corBranca = "#feffff"
corPrata = "#c9c9c9"
corCinza = "#708090"
corVerde = "#00b812"


class FrmBancoConectado(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        master.title('Banco Conectado')

        objFrmLstbxPreferencias = FrmLstbxPreferencias(self)
        objFrmLstbxPreferencias.place(x=180, y=5, width=200, height=255)
        objFrmLstbxPreferencias.config(bg=corPrata)

        objFrmBotoesLstbx = FrmBotoesLstbx(self, objFrmLstbxPreferencias, Preferencias)
        objFrmBotoesLstbx.place(x=0, y=5, width=180, height=255)
        objFrmBotoesLstbx.config(bg=corPrata)

        objFrmDataGrid = FrmDataGrid(self, Preferencias)
        objFrmDataGrid.place(x=180, y=260, width=200, height=170)
        objFrmDataGrid.config(bg=corPrata)

        objFrmBotoesDataGrid = FrmBotoesDataGrid(self, objFrmDataGrid )
        objFrmBotoesDataGrid.place(x=0, y=260, width=180, height=170)
        objFrmBotoesDataGrid.config(bg=corPrata)


class FrmBotoesLstbx(tk.Frame):
    def __init__(self, master, objFrmLstbxPreferencias, Preferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmLstbxPreferencias = objFrmLstbxPreferencias
        self.Preferencias = Preferencias

        # Criando Botões

        btnMensagem = Button(self, text="Mensagem", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.mensagem)
        btnMensagem.place(x=5, y=5, width=170, height=20)

        btnDesvCond = Button(self, text="Desvio Condicional", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.desvCond)
        btnDesvCond.place(x=5, y=30, width=170, height=20)

        btnDesvEncad = Button(self, text="Desvio Encadeado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.desvEncad)
        btnDesvEncad.place(x=5, y=55, width=170, height=20)

        btnMatchCase = Button(self, text="Match Case", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.matchCase)
        btnMatchCase.place(x=5, y=80, width=170, height=20)

        btnImpTxtWhile = Button(self, text="Importa Texto While", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impTxtWhile)
        btnImpTxtWhile.place(x=5, y=105, width=170, height=20)

        btnImpTxtFor = Button(self, text="Importa Texto For", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impTxtFor)
        btnImpTxtFor.place(x=5, y=130, width=170, height=20)

        btnImpTxtForEach = Button(self, text="Importa Texto ForEach", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                  font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impTxtForEach)
        btnImpTxtForEach.place(x=5, y=155, width=170, height=20)

        btnImpBdConect = Button(self, text="Importa Banco Conectado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impBdConect)
        btnImpBdConect.place(x=5, y=180, width=170, height=20)

        btnImpBdDesconect = Button(self, text="Importa Banco Desconectado", relief=RAISED, overrelief=RIDGE,
                                   anchor=CENTER,
                                   font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.impBdDesconect)
        btnImpBdDesconect.place(x=5, y=205, width=170, height=20)

        btnLimpTxt = Button(self, text="Limpa Texto", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                            font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.limpTxt)
        btnLimpTxt.place(x=5, y=230, width=170, height=20)

    def mensagem(self):
        messagebox.showinfo("Mensagem", "Bem Vindo ao meu Programa Python!")

    def desvCond(self):
        if messagebox.askokcancel("Desvio Condicional", "Escolha OK ou Cancelar"):
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU OK!")

        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR!")

    def desvEncad(self):
        resultadoDoBotoes = messagebox.askyesnocancel("DESVIO CONDICIONAL/ENCADEADO", "Escolha Sim, Não ou CANCELAR")
        if resultadoDoBotoes == True:
            messagebox.showinfo("RESULTADO", "Você escolheu SIM")
        elif resultadoDoBotoes == False:
            messagebox.showinfo("RESULTADO", "Você escolheu NÃO")
        else:
            messagebox.showinfo("RESULTADO", "Você escolheu CANCELAR")

    def matchCase(self):
        resultado = messagebox.askyesnocancel("ESTRUTURA DE ESCOLHA", "Escolha Sim, Não ou CANCELAR")
        match resultado:
            case True:
                messagebox.showinfo("RESULTADO", "Você escolheu SIM")
            case False:
                messagebox.showinfo("RESULTADO", "Você escolheu NÃO")
            case None:
                messagebox.showinfo("RESULTADO", "Você escolheu CANCELAR")
            case _:
                messagebox.showinfo("RESULTADO", "Você não escolheu nada")

    def impTxtWhile(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtWhile():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao ler arquivo: " + str(e))

    def impTxtFor(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtFor():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao ler arquivo: " + str(e))

    def impTxtForEach(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impTxtForEach():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao ler arquivo: " + str(e))

    def impBdConect(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impBdConect():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Conectar ao Banco: " + str(e))

    def impBdDesconect(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()
        try:
            objPreferencias = Preferencias()
            for item in objPreferencias.impBdDesconect():
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Conectar ao Banco: " + str(e))

    def limpTxt(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()


class FrmLstbxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Criando listBox

        self.lstbxPreferencias = Listbox(self, relief=GROOVE, selectmode="multiple", font="Roboto 8 bold", bg=corBranca,
                                         fg=corPreta, selectbackground=corVerde, selectforeground=corPreta,
                                         activestyle="none", height=23, width=23)
        self.lstbxPreferencias.place(x=0, y=5, width=190, height=245)

        barraRolagem = Scrollbar(self, orient="vertical", command=self.lstbxPreferencias.yview)
        barraRolagem.place(x=180, y=5, width=15, height=245)
        self.lstbxPreferencias.config(yscrollcommand=barraRolagem.set)

    def limpaTxtPreferencias(self):
        self.lstbxPreferencias.delete(0, END)

    def atualizarLista(self, preferencias):
        self.lstbxPreferencias.delete(0, END)
        for item in preferencias:
            self.lstbxPreferencias.insert(END, item)


class FrmBotoesDataGrid(tk.Frame):
    def __init__(self, master, objFrmDataGrid, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmDataGrid = objFrmDataGrid

        # Criando Botoes

        btnConsultarBd = Button(self, text="ConsultarBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.objFrmDataGrid.consultarBd)
        btnConsultarBd.place(x=5, y=15, width=170, height=20)

        btnInserirBd = Button(self, text="InserirBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.objFrmDataGrid.inserirBd)
        btnInserirBd.place(x=5, y=40, width=170, height=20)

        btnExcluirBd = Button(self, text="ExcluirBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.objFrmDataGrid.excluirBd)
        btnExcluirBd.place(x=5, y=65, width=170, height=20)

        btnAlterarBd = Button(self, text="AlterarBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.objFrmDataGrid.alterarBd)
        btnAlterarBd.place(x=5, y=90, width=170, height=20)

        btnLimpaGrid = Button(self, text="Limpa Grid", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.limpaGrid)
        btnLimpaGrid.place(x=5, y=115, width=170, height=20)

    def limpaGrid(self):
        self.objFrmDataGrid.limpaDtgvw()


class FrmDataGrid(tk.Frame):
    def __init__(self, master, Preferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Criando DataGrid

        self.colunas = ["ID", "Descricao"]
        self.tamanhoColunas = [10, 90]
        self.ancoramentoColunas = [tk.W, tk.W, ]

        self.colunas = ["ID", "Descricao"]
        self.dtgvwPreferencias = tk.ttk.Treeview(self, columns=self.colunas, show="headings")
        self.dtgvwPreferencias.place(x=0, y=15, width=190, height=120)

        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i], text=self.colunas[i], anchor=self.ancoramentoColunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhoColunas[i],
                                          anchor=self.ancoramentoColunas[i])

        # Criando estilo da grid

        estiloDtgvw = ttk.Style()
        estiloDtgvw.theme_use("clam")
        estiloDtgvw.configure("Treeview.Heading", font="Roboto 8 bold", background=corCinza, foreground=corBranca,
                              anchor=tk.W)
        estiloDtgvw.configure("Treeview", font="Roboto 8 bold", background=corBranca, foreground=corPreta)

        # Barra de rolagem da grid

        barraRolagem = Scrollbar(self, orient="vertical", command=self.dtgvwPreferencias.yview)
        barraRolagem.place(x=170, y=42, width=17, height=90)
        self.dtgvwPreferencias.config(yscrollcommand=barraRolagem.set)

        self.refresh()

    def limpaDtgvw(self):
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

    def consultBd(self, parPreferenciasDescricao=None):
        try:
            objPreferencias = Preferencias()
            self.limpaDtgvw()
            return objPreferencias.consultBd(parPreferenciasDescricao)
        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Conectar ao Banco: " + str(e))

    def consultarBd(self):
        try:
            objFrmConPreferencias = FrmConPreferencias(self)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Abrir a janela de consulta de preferencias: " + str(e))

    def inserirBd(self):
        try:
            objFrmAddPreferencias = FrmAddPreferencias(self)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Abrir a janela de inserção de preferencias: " + str(e))

    def excluirBd(self):
        try:
            objFrmDelPreferencias = FrmDelPreferencias(self)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Abrir a janela de exclusão de preferencias: " + str(e))

    def alterarBd(self):
        try:
            objFrmAltPreferencias = FrmAltPreferencias(self)

        except Exception as e:
            messagebox.showinfo("ERRO", "Erro ao Abrir a janela de alteração de preferencias: " + str(e))

    def refresh(self, registro=None):
        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhoColunas[i],
                                          anchor=self.ancoramentoColunas[i])

        if registro == None:
            linhas = self.consultBd()
        else:
            linhas = registro

        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

        for linhaBd in linhas:
            self.dtgvwPreferencias.insert("", "end", values=list(linhaBd))


class FrmConPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDataGrid = objFrmDataGrid

        self.title("Consultar Preferencias")

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=X)

        self.btnConsultar = tk.Button(self, text="Consultar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                      font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.consultarBd)
        self.btnConsultar.pack(side=TOP, padx=5, pady=5)

    def consultarBd(self):
        descricao = self.entPreferencias.get()

        if messagebox.askokcancel("Confirmação", "Deseja realmente consultar as preferencias?"):
            try:
                self.objFrmDataGrid.refresh(self.objFrmDataGrid.consultBd(descricao))

            except Exception as e:
                messagebox.showinfo("ERRO", "Erro ao consultar as preferencias: " + str(e))
        self.destroy()


class FrmAddPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDataGrid = objFrmDataGrid

        self.title("Inserir Preferencias")

        self.entPreferencias = FrmEntry(self, "Descricao")
        self.entPreferencias.pack(side=TOP, fill=X)

        self.btnInserir = tk.Button(self, text="Inserir", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                    font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.inserirBd)
        self.btnInserir.pack(side=TOP, padx=5, pady=5)

    def inserirBd(self):
        if messagebox.askokcancel("Confirmação", f'Deseja realmente inserir a preferencia {self.entPreferencias.get()}?') == True:
            try:
                descricao = self.entPreferencias.get()
                objPreferencias = Preferencias()

                if objPreferencias.inserirBd(descricao):
                    messagebox.showinfo("SUCESSO", "Preferencia inserida com sucesso!")
                    self.objFrmDataGrid.limpaDtgvw()
                    self.objFrmDataGrid.refresh()

            except Exception as e:
                messagebox.showinfo("ERRO", "Erro ao Inserir as preferencias: " + str(e))

        self.destroy()


class FrmDelPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)

            self.objFrmDataGrid = objFrmDataGrid

            self.title("Excluir Preferencias")

            self.indiceLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.focus()
            self.itemDaLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.item(self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada['values'][1]

            self.entPreferencias = FrmEntry(self, "Descricao")
            self.entPreferencias.pack(side=TOP, fill=X)

            self.btnExcluir = tk.Button(self, text="Excluir", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                        font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.excluirBd)
            self.btnExcluir.pack(side=TOP, padx=5, pady=5)

            self.mainloop()

        except Exception as e:
            self.destroy()
            messagebox.showinfo("ERRO", "Selecione uma linha para EXCLUIR! " + str(e))

    def excluirBd(self):

        if (messagebox.askokcancel("Excluir Preferencias",
                                  f"Confirmar exclusão da Preferencia {self.entPreferencias.get()}?") == True):
            try:
                objPreferencias = Preferencias()
                idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
                if objPreferencias.excluirBd(self.idItemDaLinhaSelecionada):
                    messagebox.showinfo("SUCESSO", "Preferencias excluidas com sucesso!")
                    self.objFrmDataGrid.limpaDtgvw()
                    self.objFrmDataGrid.refresh()

            except Exception as e:
                messagebox.showinfo("ERRO", "Erro ao Excluir as preferencias: " + str(e))

        self.destroy()


class FrmAltPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)

            self.objFrmDataGrid = objFrmDataGrid

            self.title("Alterar Preferencias")

            self.indiceLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.focus()
            self.itemDaLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.item(self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada['values'][1]

            self.lblDescricao = FrmLabel(self, self.descricaoItemDaLinhaSelecionada)
            self.lblDescricao.pack(side=TOP, padx=5, pady=5)

            self.entPreferencias = FrmEntry(self, "Descricao")
            self.entPreferencias.pack(side=TOP, fill=X)

            self.btnAlterar = tk.Button(self, text="Alterar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                        font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=self.alterarBd)
            self.btnAlterar.pack(side=TOP, padx=5, pady=5)

            self.mainloop()

        except Exception as e:
            self.destroy()
            messagebox.showinfo("ERRO", "Selecione uma linha para Alterar! " + str(e))

    def alterarBd(self):
        if (messagebox.askokcancel("Alterar Preferencias",
                                   f"Confirmar a alteração da Preferencia {self.lblDescricao.get()}?"
                                   f"pela Preferencia {self.entPreferencias.get()}?") == True):
            try:
                objPreferencias = Preferencias()
                descricao = self.entPreferencias.get()
                idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada["values"][0]
                if objPreferencias.alterarBd(descricao, idItemDaLinhaSelecionada):
                    messagebox.showinfo("SUCESSO", "Preferencias alteradas com sucesso!")
                    self.objFrmDataGrid.limpaDtgvw()
                    self.objFrmDataGrid.refresh()

            except Exception as e:
                messagebox.showinfo("ERRO", "VOCÊ DEVE INSERIR UMA DESCRIÇÃO ANTES DE ATUALIZAR " + str(e))

        self.destroy()


class FrmEntry(tk.Frame):
    def __init__(self, master, descricao, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType

        # Criando Label

        self.lblDescricao = tk.Label(self, text=descricao, font="Roboto 8 bold", bg=corBranca, fg=corPreta,
                                     anchor=CENTER, relief=FLAT, width=30)
        self.lblDescricao.pack(side=TOP, fill=X)

        # Criando Entry

        self.entPreferencias = tk.Entry(self, relief=GROOVE, textvariable=tk.StringVar(), width=20,
                                        font="Roboto 8 bold", bg=corBranca, fg=corPreta)
        self.entPreferencias.pack(side=BOTTOM, anchor=CENTER)

    def get(self):
        valor = self.entPreferencias.get()

        try:
            return self.varType(valor)
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.entPreferencias.delete(0, tk.END)
        self.entPreferencias.insert(0, valor)


class FrmLabel(tk.Frame):
    def __init__(self, master, lableText, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Atributos

        self.labelText = lableText
        self.varType = varType

        # Criando Label

        self.lblDescricao = tk.Label(self, text=self.labelText, font="Roboto 8 bold", bg=corPrata, fg=corPreta,
                                     anchor=CENTER, relief=FLAT)
        self.lblDescricao.pack(side=TOP, fill=X)

    def get(self):
        valor = self.labelText

        try:
            return self.varType(valor)
        except (ValueError, TypeError):
            return None

    def set(self, valor):
        self.labelText = valor
