from tkinter import *
from tkinter import messagebox, ttk, Scrollbar
import tkinter as tk
import pyodbc
import pandas as pdPreferencias
import os


# ---- Criando Funções ---- #

def mensagem():
    messagebox.showinfo("Mensagem", "Bem vindo ao meu programa Python!")


def matchCase():
    resultado = messagebox.askyesnocancel("ESTRUTURA DE ESCOLHA", "ESCOLHA SIM, NÃO OU CANCELAR!")
    match resultado:
        case True:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
        case False:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
        case None:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")
        case _:
            messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SAIR")


def desvCond():
    if messagebox.askokcancel("DESVIO CONDICIONAL", "ESCOLHA OK OU CANCELAR!"):
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
    else:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR!")


def desvEncad():
    resultadoDoBotoes = messagebox.askyesnocancel("DESVIO CONDICIONAL ENCADEADO/ANINHADO",
                                                  "ESCOLHA SIM, NÃO OU CANCELAR!")
    if resultadoDoBotoes == True:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
    elif resultadoDoBotoes == False:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
    elif resultadoDoBotoes == None:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")
    else:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SAIR")


def impTxtWhile():
    lstbxPreferencias.delete(0, END)
    try:

        arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
        strLinhaLida = arqPreferencias.readline()

        while strLinhaLida != "":
            lstbxPreferencias.insert(END, strLinhaLida)
            strLinhaLida = arqPreferencias.readline()

        arqPreferencias.close()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")


def impTxtFor():
    lstbxPreferencias.delete(0, END)
    try:
        arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
        arrStrLinhas = arqPreferencias.readlines()

        arqPreferencias.close()
        for item in range(len(arrStrLinhas)):
            item = arrStrLinhas[item]
            lstbxPreferencias.insert(END, item)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")


def impTxtForEach():
    lstbxPreferencias.delete(0, END)
    try:
        with open("Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:
            for linha in arqPreferencias:
                lstbxPreferencias.insert(END, linha)
        arqPreferencias.close()


    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")


def impBdConect():
    lstbxPreferencias.delete(0, END)
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
        srtSQL = "SELECT * FROM Preferencias_2"
        objLeitorBd.execute(srtSQL)

        preferencias = []
        registro = objLeitorBd.fetchone()

        while registro != None:
            preferencias.append(registro.Descricao)
            registro = objLeitorBd.fetchone()

        objLeitorBd.close()
        objConexao.close()

        atualizarLista(preferencias)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")


def atualizarLista(preferencias):
    lstbxPreferencias.delete(0, END)

    for item in preferencias:
        lstbxPreferencias.insert(END, item)


def impBdDesconect():
    lstbxPreferencias.delete(0, END)
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

        dfPreferencias = pdPreferencias.DataFrame(registro, columns=["Descricao"])

        objLeitorBd.close()
        objConexao.close()

        for linha in dfPreferencias["Descricao"]:
            lstbxPreferencias.insert(END, linha[0])

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")


def limpTxt():
    lstbxPreferencias.delete(0, END)


# ---- Criando Cores ---- #

corPreta = "#000000"
corBranca = "#feffff"
corPrata = "#c9c9c9"
corCinza = "#708090"
corVerde = "#00b812"

# ---- criando janela principal ---- #

janela = Tk()
janela.title("Importar Banco de Dados")
janela.geometry("350x300")
janela.configure(bg=corPreta)

# ---- Criando Frames ---- #

frmCima = Frame(janela, relief=GROOVE)
frmCima.pack(fill=BOTH, expand=True)
frmCima.configure(bg=corPrata)

# ---- Criando Botões ---- #

btnMensagem = Button(frmCima, text="Mensagem", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                     font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=mensagem)
btnMensagem.place(x=5, y=5, width=170, height=20)

btnDesvCond = Button(frmCima, text="Desvio Condicional", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                     font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=desvCond)
btnDesvCond.place(x=5, y=30, width=170, height=20)

btnDesvEncad = Button(frmCima, text="Desvio Encadeado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                      font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=desvEncad)
btnDesvEncad.place(x=5, y=55, width=170, height=20)

btnMatchCase = Button(frmCima, text="Match Case", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                      font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=matchCase)
btnMatchCase.place(x=5, y=80, width=170, height=20)

btnImpTxtWhile = Button(frmCima, text="Importa Texto While", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                        font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=impTxtWhile)
btnImpTxtWhile.place(x=5, y=105, width=170, height=20)

btnImpTxtFor = Button(frmCima, text="Importa Texto For", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                      font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=impTxtFor)
btnImpTxtFor.place(x=5, y=130, width=170, height=20)

btnImpTxtForEach = Button(frmCima, text="Importa Texto ForEach", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                          font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=impTxtForEach)
btnImpTxtForEach.place(x=5, y=155, width=170, height=20)

btnImpBdConect = Button(frmCima, text="Importa Banco Conectado", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                        font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=impBdConect)
btnImpBdConect.place(x=5, y=180, width=170, height=20)

btnImpBdDesconect = Button(frmCima, text="Importa Banco Desconectado", relief=RAISED, overrelief=RIDGE,
                           anchor=CENTER,
                           font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=impBdDesconect)
btnImpBdDesconect.place(x=5, y=205, width=170, height=20)

btnLimpTxt = Button(frmCima, text="Limpa Texto", relief=RAISED, overrelief=RIDGE, anchor=CENTER,
                    font="Roboto 8 bold", bg=corCinza, fg=corBranca, command=limpTxt)
btnLimpTxt.place(x=5, y=230, width=170, height=20)

# ---- Criando ListBox---- #

lstbxPreferencias = Listbox(frmCima, relief=GROOVE, selectmode="multiple", font="Roboto 8 bold", bg=corBranca,
                            fg=corPreta, selectbackground=corVerde, selectforeground=corPreta,
                            activestyle="none", height=23, width=23)
lstbxPreferencias.place(x=180, y=5, width=160, height=245)

# ---- Criando Barra de rolagem ---- #

BarraRolagem = Scrollbar(frmCima, orient=VERTICAL, command=lstbxPreferencias.yview)
BarraRolagem.place(x=322, y=5, height=245)
lstbxPreferencias.config(yscrollcommand=BarraRolagem.set)

janela.mainloop()
