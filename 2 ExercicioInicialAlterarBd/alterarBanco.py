from tkinter import *
from builtins import Exception
from tkinter import messagebox, ttk, Scrollbar
import tkinter as tk
import pyodbc
import pandas as pdPreferencias
import os

# Criando Cores

corPreto = "#000000"
corBranco = "#feffff"
corPrata = "#c9c9c9"
corCinza = "#708090"
corVerde = "#00b812"


# Criando classes

class FrmBancoConectado(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        master.title("Banco de dados conectado")

        objFrmLstbxPreferencias = FrmLstbxPreferencias(self)
        objFrmLstbxPreferencias.place(x=180, y=5, width=200, height=250)
        objFrmLstbxPreferencias.config(bg=corPrata)

        objFrmBotoesLstbx = FrmBotoesLstbx(self, objFrmLstbxPreferencias)
        objFrmBotoesLstbx.place(x=0, y=5, width=180, height=250)
        objFrmBotoesLstbx.config(bg=corPrata)

        objFrmDataGrid = FrmDataGrid(self)
        objFrmDataGrid.place(x=180, y=255, width=200, height=170)
        objFrmDataGrid.config(bg=corPrata)

        objFrmBotoesDataGrid = FrmBotoesDataGrid(self, objFrmDataGrid)
        objFrmBotoesDataGrid.place(x=0, y=255, width=180, height=170)
        objFrmBotoesDataGrid.config(bg=corPrata)


class FrmBotoesLstbx(tk.Frame):
    def __init__(self, master, objFrmLstbxPreferencias, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.objFrmLstbxPreferencias = objFrmLstbxPreferencias

        # criando botões

        btnMensagem = Button(self, text="Mensagem", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.mensagem)
        btnMensagem.place(x=5, y=5, width=170, height=20)

        btnDesvCond = Button(self, text="Desvio Condicional", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.desvCond)
        btnDesvCond.place(x=5, y=30, width=170, height=20)

        btnDesvEncad = Button(self, text="Desvio Encadeado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.desvEncad)
        btnDesvEncad.place(x=5, y=55, width=170, height=20)

        btnMatchCase = Button(self, text="Match case", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.matchCase)
        btnMatchCase.place(x=5, y=80, width=170, height=20)

        btnImpTxtWhile = Button(self, text="Importa Texto While", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.impTxtWhile)
        btnImpTxtWhile.place(x=5, y=105, width=170, height=20)

        btnImpTxtFor = Button(self, text="Importa Texto For", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.impTxtFor)
        btnImpTxtFor.place(x=5, y=130, width=170, height=20)

        btnImpTxtForEach = Button(self, text="Importa Texto For Each", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                  font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.impTxtForEach)
        btnImpTxtForEach.place(x=5, y=155, width=170, height=20)

        btnImpBdConect = Button(self, text="Importa Banco Conectado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.impBdConect)
        btnImpBdConect.place(x=5, y=180, width=170, height=20)

        btnImpBdDesconect = Button(self, text="Importa Banco Desconectado", relief=RAISED, overrelief=RIDGE,
                                   anchor=CENTER,
                                   font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.impBdDesconect)
        btnImpBdDesconect.place(x=5, y=205, width=170, height=20)

        btnLimpaTxt = Button(self, text="Limpa Texto", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.limpaTxt)
        btnLimpaTxt.place(x=5, y=230, width=170, height=20)

    def mensagem(self):
        messagebox.showinfo("Mensagem", "Bem vindo o meu programa Python!")

    def desvCond(self):
        if messagebox.askokcancel("Desvio Condicional", "ESCOLHA OK OU CANCELAR"):
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU OK")
        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")

    def desvEncad(self):
        resultadoDosBotoes = messagebox.askyesnocancel("Desvio Encadeado", "ESCOLHA SIM, NÃO OU CANCELAR")
        if resultadoDosBotoes == True:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
        elif resultadoDosBotoes == False:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
        else:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")

    def matchCase(self):
        resultado = messagebox.askyesnocancel("MATCH CASE", "ESCOLHA SIM, NÃO OU CANCELAR")
        match resultado:
            case True:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
            case False:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
            case None:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")
            case _:
                messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SAIR")

    def impTxtWhile(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()

        try:
            arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
            strLinhaLida = arqPreferencias.readline()

            while strLinhaLida != "":
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, strLinhaLida)
                strLinhaLida = arqPreferencias.readline()
            arqPreferencias.close()
        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO LER ARQUIVO DE PREFERENCIAS" + str(e))

    def impTxtFor(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()

        try:
            arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
            arrStrLinhas = arqPreferencias.readlines()
            arqPreferencias.close()

            for item in range(len(arrStrLinhas)):
                item = arrStrLinhas[item]
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)

        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO LER ARQUIVO DE PREFERENCIAS" + str(e))

    def impTxtForEach(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()

        try:
            with open("Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:

                for item in arqPreferencias:
                    self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, item)
                arqPreferencias.close()

        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO LER ARQUIVO DE PREFERENCIAS" + str(e))

    def impBdConect(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()

        try:
            databaseName = 'Preferencias_3_09022024.accdb'
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            databasePath = os.path.join(projectDirectory, databaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + databasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()
            strSQL = "SELECT Descricao FROM Preferencias_3 ORDER BY ID"
            objLeitorBd.execute(strSQL)

            preferecias = []
            registro = objLeitorBd.fetchone()

            while registro != None:
                preferecias.append(registro.Descricao)
                registro = objLeitorBd.fetchone()

            objLeitorBd.close()
            objConexao.close()

            self.objFrmLstbxPreferencias.atualizarLista(preferecias)


        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO LER O BANCO DE DADOS" + str(e))

    def impBdDesconect(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()

        try:
            databaseName = 'Preferencias_3_09022024.accdb'
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            databasePath = os.path.join(projectDirectory, databaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + databasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()
            strSQL = "SELECT Descricao FROM Preferencias_3 ORDER BY ID"
            objLeitorBd.execute(strSQL)

            registro = objLeitorBd.fetchall()

            dfPreferecias = pdPreferencias.DataFrame(registro, columns=["Descricao"])

            objLeitorBd.close()
            objConexao.close()

            for linha in registro:
                self.objFrmLstbxPreferencias.lstbxPreferencias.insert(END, linha.Descricao)

        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO LER O BANCO DE DADOS" + str(e))

    def limpaTxt(self):
        self.objFrmLstbxPreferencias.limpaTxtPreferencias()


class FrmLstbxPreferencias(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.lstbxPreferencias = Listbox(self, selectmode=MULTIPLE, font="Roboto 8 bold", relief=GROOVE, bg=corBranco,
                                         fg=corPreto,
                                         selectbackground=corVerde, selectforeground=corPreto, activestyle="none",
                                         height=23, width=23)
        self.lstbxPreferencias.place(x=5, y=5, width=190, height=245)

        barraDeRolagem = Scrollbar(self, orient=VERTICAL, command=self.lstbxPreferencias.yview)
        barraDeRolagem.place(x=180, y=5, width=15, height=245)
        self.lstbxPreferencias.config(yscrollcommand=barraDeRolagem.set)

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

        # Criando Botões

        btnConsultarBd = Button(self, text="ConsultarBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.objFrmDataGrid.consultBd)
        btnConsultarBd.place(x=5, y=15, width=170, height=20)

        btnInserirBd = Button(self, text="InserirBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.objFrmDataGrid.inserirBd)
        btnInserirBd.place(x=5, y=40, width=170, height=20)

        btnExcluirBd = Button(self, text="ExcluirBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                              font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.objFrmDataGrid.excluirBd)
        btnExcluirBd.place(x=5, y=65, width=170, height=20)

        btnAlteraBd = Button(self, text="AlteraBd", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                             font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.objFrmDataGrid.alterarBd)
        btnAlteraBd.place(x=5, y=90, width=170, height=20)

        btnLimparGrid = Button(self, text="LimparGrid", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                               font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.limpaGrid)
        btnLimparGrid.place(x=5, y=115, width=170, height=20)

    def limpaGrid(self):
        self.objFrmDataGrid.limpaDtgvw()


class FrmDataGrid(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Criando Datagrid

        self.colunas = ["ID", "Descricao"]
        self.tamanhoColunas = [10, 90]
        self.ancoramentoColunas = [tk.W, tk.W, ]

        self.colunas = ["ID", "Descricao"]
        self.dtgvwPreferencias = ttk.Treeview(self, columns=self.colunas, show="headings")
        self.dtgvwPreferencias.place(x=5, y=15, width=190, height=120)

        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i], text=self.colunas[i], anchor=self.ancoramentoColunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhoColunas[i],
                                          anchor=self.ancoramentoColunas[i])

        # Criando estilo

        estiloDtgvw = ttk.Style()
        estiloDtgvw.theme_use("clam")
        estiloDtgvw.configure("Treeview.Heading", font="Roboto 8 bold", background=corCinza, foreground=corBranco,
                              anchor=tk.W, fieldbackground=corPreto)
        estiloDtgvw.configure("Treeview", font="Roboto 8 bold", background=corBranco, foreground=corPreto)

        # Barra de rolagem

        barraDeRolagemDtgvw = Scrollbar(self, orient="vertical", command=self.dtgvwPreferencias.yview)
        barraDeRolagemDtgvw.place(x=178, y=40, width=15, height=90)
        self.dtgvwPreferencias.config(yscrollcommand=barraDeRolagemDtgvw.set)

        self.Refresh()

    def limpaDtgvw(self):
        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

    def consultarBd(self, parPreferenciasDescricao=None):
        try:
            databaseName = 'Preferencias_3_09022024.accdb'
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            databasePath = os.path.join(projectDirectory, databaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + databasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()

            if parPreferenciasDescricao is None or parPreferenciasDescricao.strip() == "":
                strSQL = "SELECT ID, Descricao FROM Preferencias_3 ORDER BY ID"
                objLeitorBd.execute(strSQL)
            else:
                strSQL = "SELECT ID, Descricao FROM Preferencias_3 WHERE Descricao = ? ORDER BY ID"
                objLeitorBd.execute(strSQL, parPreferenciasDescricao)

            registro = objLeitorBd.fetchall()

            objLeitorBd.close()
            objConexao.close()

            return registro
        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO LER O BANCO DE DADOS" + str(e))

    def consultBd(self):
        try:
            objFrmConsPreferencias = FrmConsPreferencias(self)
        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO ABRIR A JANELA DE CONSULTA" + str(e))

    def inserirBd(self):
        try:
            objFrmAddPreferencias = FrmAddPreferencias(self)
        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO ABRIR A JANELA DE INSERÇÃO" + str(e))

    def excluirBd(self):
        try:
            objFrmDelPreferencias = FrmDelPreferencias(self)
        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO ABRIR A JANELA DE EXCLUSÃO" + str(e))

    def alterarBd(self):
        try:
            objFrmAltPreferencias = FrmAltPreferencias(self)
        except Exception as e:
            messagebox.showinfo("ERRO", "ERRO AO ABRIR A JANELA DE ALTERAÇÃO" + str(e))

    def Refresh(self, registro=None):
        for i in range(len(self.colunas)):
            self.dtgvwPreferencias.heading(self.colunas[i])
            self.dtgvwPreferencias.column(self.colunas[i], width=self.tamanhoColunas[i],
                                          anchor=self.ancoramentoColunas[i])
        if registro == None:
            linhas = self.consultarBd()
        else:
            linhas = registro

        self.dtgvwPreferencias.delete(*self.dtgvwPreferencias.get_children())

        for linhaBd in linhas:
            self.dtgvwPreferencias.insert("", "end", values=list(linhaBd))


class FrmConsPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDataGrid = objFrmDataGrid

        self.title('Consultar Preferencias')

        self.entPreferencias = FrmEntry(self, 'Descricao')
        self.entPreferencias.pack(side=TOP, fill=X)

        btnConsular = tk.Button(self, text="Consultar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.consultarBd)
        btnConsular.pack(side=TOP, padx=5, pady=5)

    def consultarBd(self):
        descricao = self.entPreferencias.get()

        if messagebox.askokcancel("Consultar Preferencias", f"Confirmar consulta de preferencias {descricao}?"):
            try:
                return self.objFrmDataGrid.Refresh(self.objFrmDataGrid.consultarBd(descricao))

            except Exception as ex:
                messagebox.showinfo("ERRO", str(ex))
            self.destroy()


class FrmAddPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.objFrmDataGrid = objFrmDataGrid

        self.title('Alterar Preferencias')

        self.entPreferencias = FrmEntry(self, 'Descricao')
        self.entPreferencias.pack(side=TOP, fill=X)

        btnInserir = tk.Button(self, text="Inserir", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                               font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.inserirBd)
        btnInserir.pack(side=TOP, padx=5, pady=5)

    def inserirBd(self):
        global objConexao
        try:
            databaseName = 'Preferencias_3_09022024.accdb'
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            databasePath = os.path.join(projectDirectory, databaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + databasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()

            strSQL = f"INSERT INTO Preferencias_3 (Descricao) VALUES(?)"
            objLeitorBd.execute(strSQL, self.entPreferencias.get())

            objConexao.commit()

        except Exception as e:
            messagebox.showinfo("ERRO", "Você deve inserir uma descricao antes de adicioná-la")
        else:
            messagebox.showinfo("Sucesso", "Adicionado com sucesso")
            self.objFrmDataGrid.Refresh()
        finally:
            objConexao.close()
            self.destroy()


class FrmDelPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.objFrmDataGrid = objFrmDataGrid

            self.title('Excluir Preferencias')

            self.indiceLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.focus()
            self.itemDaLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.item(self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemDaLinhaSelecionada['values'][0]
            self.descricaoItemDaLinhaSelecionada = self.itemDaLinhaSelecionada['values'][1]

            self.entPreferencias = FrmEntry(self, 'Descricao')
            self.entPreferencias.pack(side=TOP, fill=X)

            self.btnConsultar = tk.Button(self, text="Excluir", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                          font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.excluirBd)
            self.btnConsultar.pack(side=TOP, pady=5, padx=5)

            self.mainloop()

        except Exception:
            messagebox.showinfo("ERRO", "Selecione uma linha para excluir")

    def excluirBd(self):
        global objConexao
        if (messagebox.askokcancel("Excluir Preferencias", f"Confirmar exclusão de preferencias"
                                                           f" {self.entPreferencias.get()}?") == True):
            try:
                databaseName = 'Preferencias_3_09022024.accdb'
                projectDirectory = os.path.dirname(os.path.abspath(__file__))
                databasePath = os.path.join(projectDirectory, databaseName)

                connectionString = (
                        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                        r'DBQ=' + databasePath + ';'
                )

                objConexao = pyodbc.connect(connectionString)
                objLeitorBd = objConexao.cursor()

                strSQL = f"DELETE FROM Preferencias_3 WHERE ID = ?;"
                objLeitorBd.execute(strSQL, self.idItemDaLinhaSelecionada)

                objConexao.commit()

            except Exception as e:
                messagebox.showinfo("ERRO", str(e))
            else:
                messagebox.showinfo("Sucesso", "Excluído com sucesso")
                self.objFrmDataGrid.Refresh()
            finally:
                objConexao.close()
            self.destroy()


class FrmAltPreferencias(tk.Tk):
    def __init__(self, objFrmDataGrid, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.objFrmDataGrid = objFrmDataGrid

            self.title('Alterar Preferencias')

            self.indiceLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.focus()
            self.itemLinhaSelecionada = self.objFrmDataGrid.dtgvwPreferencias.item(self.indiceLinhaSelecionada)
            self.idItemDaLinhaSelecionada = self.itemLinhaSelecionada['values'][0]
            self.descricaoItemDaLinhaSelecionada = self.itemLinhaSelecionada['values'][1]

            self.lblDescricao = FrmLabel(self, self.descricaoItemDaLinhaSelecionada)
            self.lblDescricao.pack(side=TOP, padx=5, pady=5)

            self.entPreferencias = FrmEntry(self, 'Descricao')
            self.entPreferencias.pack(side=TOP, fill=X)

            self.btnAlterar = tk.Button(self, text="Alterar", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                                        font="Roboto 8 bold", bg=corCinza, fg=corBranco, command=self.alterarBd)
            self.btnAlterar.pack(side=TOP, padx=5, pady=5)

            self.mainloop()

        except Exception:
            self.destroy()
            messagebox.showinfo("ERRO", "VOCÊ DEVE INSERIR UMA DESCRICAO ANTES DE ALTERAR")

    def alterarBd(self):
        global objConexao
        if messagebox.askokcancel("Alterar Preferencias",f"Confirmar alteração de preferencias {self.lblDescricao.get()}?" f" pela preferencia {self.entPreferencias.get()}?") == True:

            try:
                databaseName = 'Preferencias_3_09022024.accdb'
                projectDirectory = os.path.dirname(os.path.abspath(__file__))
                databasePath = os.path.join(projectDirectory, databaseName)

                connectionString = (
                        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                        r'DBQ=' + databasePath + ';'
                )

                objConexao = pyodbc.connect(connectionString)
                objLeitorBd = objConexao.cursor()

                strSQL = f"UPDATE Preferencias_3 SET Descricao = ? WHERE ID = ?;"
                objLeitorBd.execute(strSQL, (self.entPreferencias.get(), self.idItemDaLinhaSelecionada))

                objConexao.commit()

            except Exception:
                messagebox.showinfo("ERRO", "VOCÊ DEVE INSERIR UMA DESCRICAO ANTES DE ATUALIZAR")
            else:
                messagebox.showinfo("Sucesso", "Atualizado com sucesso")
                self.objFrmDataGrid.Refresh()
            finally:
                objConexao.close()
            self.destroy()


class FrmEntry(tk.Frame):
    def __init__(self, master, descricao, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType

        # criando label

        self.lblDescricao = tk.Label(self, text=descricao, font="Roboto 8 bold", bg=corBranco, fg=corPreto,
                                     anchor=CENTER, relief=FLAT, width=30)
        self.lblDescricao.pack(side=TOP, fill=X)

        # criando Entry

        self.entPreferencias = tk.Entry(self, relief=GROOVE, textvariable=tk.StringVar(), width=20,
                                        font="Roboto 8 bold", bg=corBranco, fg=corPreto)
        self.entPreferencias.pack(side=BOTTOM, anchor=CENTER)

    def get(self):
        valor = self.entPreferencias.get()

        try:
            return self.varType(valor)
        except (TypeError, ValueError):
            self.entPreferencias.delete(0, tk.END)
            self.entPreferencias.insert(0, valor)


class FrmLabel(tk.Frame):
    def __init__(self, master, lableText, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.varType = varType
        self.labelText = lableText

        # criando label

        self.lblDescricao = tk.Label(self, text=self.labelText, font="Roboto 8 bold", bg=corBranco, fg=corPreto,
                                     anchor=CENTER, relief=FLAT, width=30)
        self.lblDescricao.pack(side=TOP, fill=X)

    def get(self):
        valor = self.labelText

        try:
            return self.varType(valor)
        except (TypeError, ValueError):
            return None

    def set(self, valor):
        self.labelText = valor
