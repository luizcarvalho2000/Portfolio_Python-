from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, filedialog
import tkinter as tk
from tkinter import messagebox, Frame, Label

import numpy as np
from PIL import ImageTk, Image

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import pandas as pd
from view import *

# Cores
corPreto = "#2e2d2b"
corBranco = "#feffff"
corCinza = "#e5e5e5"
corVerde = "#666464"
corDaLetra = "#403d3d"
corAzul = "#003452"
corVermelho = "#ef5350"
cor1 = ['#fa5555', '#99bb55', '#5588bb']
cor2 = ['#5588bb', '#99bb55']

# Criando Janela Principal
janela = Tk()
janela.title("Sistema de Controle de Estoque")
janela.geometry("1052x600")
janela.configure(background=corBranco)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('contabilidade.ico')

style = ttk.Style(janela)
style.theme_use("clam")

# Criando Frames
frmLogo = Frame(janela, width=950, height=52, bg=corVermelho, relief=FLAT)
frmLogo.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=2, ipadx=680)

frmMeio = Frame(janela, width=950, height=270, bg=corVerde, relief=FLAT)
frmMeio.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

# Dividindo Frames
frmDados = Frame(frmMeio, width=425, height=280, bg=corBranco, relief=FLAT)
frmDados.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

frmResultado = Frame(frmMeio, width=250, height=270, bg=corBranco, relief=FLAT)
frmResultado.grid(row=0, column=1, padx=0, pady=0, sticky=NSEW)

frmChart = Frame(frmMeio, width=377, height=270, bg=corBranco, relief=FLAT)
frmChart.grid(row=0, column=2, padx=0, pady=0, sticky=NSEW)

# Criando Frame da Tabela
frmTabela = Frame(janela, width=650, height=150, relief=FLAT)
frmTabela.grid(row=3, column=0, padx=0, pady=10, sticky=NSEW)

# Frame do Logo

imgLg = Image.open("despesas.ico")
imgLg = imgLg.resize((50, 50))
imgLg = ImageTk.PhotoImage(imgLg)
lblLogo = Label(frmLogo, image=imgLg, text=" Calculadora de lucro", width=1050, compound=LEFT, relief=RAISED,
                anchor=NW, font='Roboto 15 bold', bg=corBranco, fg=corDaLetra)
lblLogo.place(x=0, y=0)


# Frame meio
def lucro():
    global imgSalvar, imgCalcular, imgDeletar, imgExportar, imgLg, imgResetar, imgSair


# Função para calcular
def calcular():
    nome = entryNome.get()
    compra = entryCompra.get()
    venda = entryVenda.get()
    quantidade = entryQuantidade.get()
    adicionais = entryAdicionais.get()
    frete = entryFrete.get()

    lista = [nome, compra, venda, quantidade, adicionais, frete]

    # Verificando caso tenha campos vazios

    for item in lista:
        if item == '':
            messagebox.showerror("ERRO", "Preencha todos os campos")
            return

    # Calculando o Lucro e aplicando na label
    def calcularLucro(nomeProduto, precoDeCompra, precoDeVenda, quantidade, custosAdicionais, custoFrete):

        # Perguntando ao usuário pelos dados
        nomeProduto = nomeProduto
        precoDeCompra = float(precoDeCompra)
        precoDeVenda = float(precoDeVenda)
        quantidade = int(quantidade)
        custosAdicionais = float(custosAdicionais)
        custoFrete = float(custoFrete)

        # Calculando o lucro
        custoTotal = (precoDeCompra + custosAdicionais + custoFrete) * quantidade
        lucro = (precoDeVenda - precoDeCompra - custosAdicionais - custoFrete) * quantidade
        margemDeLucro = lucro / (precoDeVenda * quantidade) * 100

        # Imprimindo os resultados

        lblNomeLucro['text'] = "O lucro do produto {} é de R${:.2f} e a margem de lucro é de {:.2f}%.".format(
            nomeProduto, margemDeLucro, custoTotal)
        lblLucro['text'] = "R${:.2f}".format(lucro)
        lblCusto['text'] = "R${:.2f}".format(margemDeLucro)

    # Fazendo calculo
    calcularLucro(nome, compra, venda, quantidade, adicionais, frete)


# Função para salvar dados no Excel
def salvarDados():
    nome = entryNome.get()
    compra = entryCompra.get()
    venda = entryVenda.get()
    quantidade = entryQuantidade.get()
    adicionais = entryAdicionais.get()
    frete = entryFrete.get()

    lista = [nome, compra, venda, quantidade, adicionais, frete]

    # Verificando caso tenha campos vazios

    for item in lista:
        if item == '':
            messagebox.showerror("ERRO", "Preencha todos os campos")
            return

    # Salvando os dados no excel
    salvarProdutos(nome, compra, venda, quantidade, adicionais, frete)
    messagebox.showinfo("SUCESSO", "Dados salvos com sucesso")

    # Limpando os campos
    entryNome.delete(0, END)
    entryCompra.delete(0, END)
    entryVenda.delete(0, END)
    entryQuantidade.delete(0, END)
    entryAdicionais.delete(0, END)
    entryFrete.delete(0, END)

    # Mostrando os dados salvos no grafico

    mostrar()
    graficoBar()


def obterEstatisticasAtualizadas():
    # Obtém os dados atualizados da função estatistica()
    return estatistica()


def exportarExcel():
    try:
        # Obtém os dados dos produtos
        dadosProdutos = obterDadosExcel("dados.xlsx")

        # Obtém os dados atualizados da função estatistica()
        dadosEstatisticas = obterEstatisticasAtualizadas()

        # Abre o diálogo para salvar o arquivo
        caminhoArquivo = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )

        if caminhoArquivo:
            # Cria um arquivo Excel e salva os dados em abas separadas
            with pd.ExcelWriter(caminhoArquivo) as writer:
                # Aba "Produtos"
                pd.DataFrame(dadosProdutos, columns=[
                    'Produto', 'Preço de Compra', 'Preço de Venda', 'Quantidade', 'Custos Adicionais',
                    'Custo de Frete', 'Custo Total', 'Lucro Líquido', 'Margem de Lucro em %'
                ]).to_excel(writer, sheet_name="Produtos", index=False)

                # Aba "Estatísticas"
                pd.DataFrame(
                    {"Valor Total de Custo": [dadosEstatisticas[0]],
                     "Lucro Líquido Total": [dadosEstatisticas[1]],
                     "Margem de Lucro Total": [dadosEstatisticas[2]]}
                ).to_excel(writer, sheet_name="Estatísticas", index=False)

            messagebox.showinfo("Sucesso", "Dados exportados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar os dados: {e}")


def limparExcel():
    # Pergunta ao usuário se ele realmente deseja excluir o projeto
    confirmacao = messagebox.askyesno("AVISO!", "Deseja excluir o seu projeto?\nEle será excluído e não"
                                                " será possível restaurá-lo, Exporte os dados antes de apagar"
                                                " se desejar")
    match confirmacao:
        case True:
            try:
                wb = openpyxl.Workbook()
                wb.save("dados.xlsx")

                for item in tree.get_children():
                    tree.delete(item)

                messagebox.showinfo("Sucesso", "Dados apagados e Excel limpo com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao limpar os dados: {e}")
        case False:
            pass


def sair():
    confirmarSair = messagebox.askyesno("Deseja sair?", "Você deseja fechar o programa?")

    match confirmarSair:
        case True:
            janela.destroy()

        case False:
            pass

def deletar():
    try:
        treevDados = tree.focus()
        treevDicionario = tree.item(treevDados)
        treevLista = treevDicionario['values']
        valor = treevLista[0]
        valor = str(valor)

        confirmar = messagebox.askyesno(
            "AVISO!",
            f"Deseja realmente deletar o produto '{valor}'?\n\nEsta ação não poderá ser desfeita."
        )

        match confirmar:
            case True:
                deletarLinhaPorNome(valor, 'dados.xlsx')
                messagebox.showinfo("SUCESSO", "Produto deletado com sucesso")
                graficoBar()
                mostrar()
            case False:
                pass

    except IndexError:
        messagebox.showerror("ERRO", "Selecione um produto para deletar")

lblDetalhes = Label(frmDados, text="Entre os detalhes do produtos", compound=LEFT, padx=5, relief=FLAT,
                    anchor=CENTER, font='Roboto 11 bold', bg=corBranco, fg=corDaLetra)
lblDetalhes.place(x=100, y=10)
lblLinhaDel1 = Label(frmDados, width=500, height=1, anchor=NW, font='Roboto 15', bg=corVerde, fg=corBranco)
lblLinhaDel1.place(x=0, y=47)
lblLinhaDel2 = Label(frmDados, width=500, height=1, anchor=NW, font='Roboto 15', bg=corBranco, fg=corBranco)
lblLinhaDel2.place(x=0, y=50)

lblLinhaVertical = tk.Label(frmDados, width=1, height=505, anchor=NW, font='Roboto 1',
                            bg=corVerde, fg=corBranco)
lblLinhaVertical.place(x=0, y=0)

lblLinhaVertical2 = tk.Label(frmDados, width=1, height=505, anchor=NW, font='Roboto 1',
                             bg=corBranco, fg=corBranco)
lblLinhaVertical2.place(x=5, y=50)

lblLinhaVertical2 = tk.Label(frmDados, width=1, height=20, anchor=NW, font='Roboto 1',
                             bg=corBranco, fg=corBranco)
lblLinhaVertical2.place(x=5, y=1)

lblNome = Label(frmDados, text="Nome do Produto *", height=1, anchor=NW, font='Ivy 10 bold',
                bg=corBranco, fg=corDaLetra)
lblNome.place(x=10, y=70)
entryNome = tk.Entry(frmDados, width=20, justify='left', font='Ivy 10 bold', relief=GROOVE, bg=corBranco,
                     fg=corDaLetra)
entryNome.place(x=10, y=100)

lblQuantidade = Label(frmDados, text="Qtd do Produto *", height=1, anchor=NW, font='Ivy 10 bold',
                      bg=corBranco, fg=corDaLetra)
lblQuantidade.place(x=170, y=70)
entryQuantidade = tk.Entry(frmDados, width=8, justify='center', font='Ivy 10', relief=GROOVE,
                           bg=corBranco, fg=corDaLetra)
entryQuantidade.place(x=173, y=100)

lblCompra = Label(frmDados, text="Preço de Compra *", height=1, anchor=NW, font='Ivy 10 bold',
                  bg=corBranco, fg=corDaLetra)
lblCompra.place(x=290, y=70)
entryCompra = tk.Entry(frmDados, width=8, justify='center', font='Ivy 10', relief=GROOVE, bg=corBranco,
                       fg=corDaLetra)
entryCompra.place(x=290, y=100)

lblFrete = Label(frmDados, text="Preço do frete *", height=1, anchor=NW, font='Ivy 10 bold',
                 bg=corBranco, fg=corDaLetra)
lblFrete.place(x=10, y=130)
entryFrete = tk.Entry(frmDados, width=8, justify='center', font='Ivy 10', relief=GROOVE, bg=corBranco,
                      fg=corDaLetra)
entryFrete.place(x=10, y=160)

lblVenda = Label(frmDados, text="Preço de Venda *", height=1, anchor=NW, font='Ivy 10 bold',
                 bg=corBranco, fg=corDaLetra)
lblVenda.place(x=170, y=130)
entryVenda = tk.Entry(frmDados, width=8, justify='center', font='Ivy 10', relief=GROOVE, bg=corBranco,
                      fg=corDaLetra)
entryVenda.place(x=173, y=160)

lblAdicionais = Label(frmDados, text="Custos adicionais *", height=1, anchor=NW, font='Ivy 10 bold',
                      bg=corBranco, fg=corDaLetra)
lblAdicionais.place(x=290, y=130)
entryAdicionais = tk.Entry(frmDados, width=8, justify='center', font='Ivy 10', relief=GROOVE, bg=corBranco,
                           fg=corDaLetra)
entryAdicionais.place(x=290, y=160)

lblLinhaVertical3 = tk.Label(frmDados, width=1, height=505, anchor=NW, font='Roboto 1',
                             bg=corVerde, fg=corBranco)
lblLinhaVertical3.place(x=422, y=0)

# Botão calcular
imgCalcular = Image.open('calculadora2.ico')
imgCalcular = imgCalcular.resize((18, 18))
imgCalcular = ImageTk.PhotoImage(imgCalcular)
btnCalcular = tk.Button(frmDados, text="Calcular", image=imgCalcular, compound=LEFT, relief=GROOVE, overrelief=RIDGE,
                        width=100, font="Ivy 11", bg=corBranco, fg=corDaLetra, command=calcular)
btnCalcular.place(x=10, y=200)

# Botão Salvar
imgSalvar = Image.open('save.ico')
imgSalvar = imgSalvar.resize((18, 18))
imgSalvar = ImageTk.PhotoImage(imgSalvar)
btnSalvar = tk.Button(frmDados, text="Salvar", image=imgSalvar, compound=LEFT, relief=GROOVE, overrelief=RIDGE,
                      width=100, font="Ivy 11", bg=corBranco, fg=corDaLetra, command=salvarDados)
btnSalvar.place(x=10, y=230)

# Botao Deletar
imgDeletar = Image.open('delete.ico')
imgDeletar = imgDeletar.resize((18, 18))
imgDeletar = ImageTk.PhotoImage(imgDeletar)
btnDeletar = tk.Button(frmDados, text="Deletar", image=imgDeletar, compound=LEFT, relief=GROOVE, overrelief=RIDGE,
                       width=100, font="Ivy 11", bg=corBranco, fg=corDaLetra, command=deletar)
btnDeletar.place(x=130, y=200)

imgExportar = Image.open('xls.ico')
imgExportar = imgExportar.resize((18, 18))
imgExportar = ImageTk.PhotoImage(imgExportar)
btnExportar = tk.Button(frmDados, text="Exportar", image=imgExportar, compound=LEFT, relief=GROOVE,
                        overrelief=RIDGE,
                        width=100, font="Ivy 11", bg=corBranco, fg=corDaLetra, command=exportarExcel)
btnExportar.place(x=130, y=230)

# Botão Limpar
imgResetar = Image.open('reiniciar.ico')
imgResetar = imgResetar.resize((18, 18))
imgResetar = ImageTk.PhotoImage(imgResetar)
btnLimpar = tk.Button(frmDados, text="Limpar", image=imgResetar, compound=LEFT, relief=GROOVE, overrelief=RIDGE,
                      width=100, font="Ivy 11", bg=corBranco, fg=corDaLetra, command=limparExcel)
btnLimpar.place(x=250, y=200)

imgSair = Image.open('sair.ico')
imgSair = imgSair.resize((18, 18))
imgSair = ImageTk.PhotoImage(imgSair)
btnLimpar = tk.Button(frmDados, text="Fechar", image=imgSair, compound=LEFT, relief=GROOVE, overrelief=RIDGE,
                      width=100, font="Ivy 11", bg=corBranco, fg=corDaLetra, command=sair)
btnLimpar.place(x=250, y=230)

# --------------------- Resultado -------------------------------
lblResult = Label(frmResultado, text="Resultado da operação", compound=LEFT, padx=5, relief=FLAT, anchor=CENTER,
                  font='Roboto 11 bold', bg=corBranco, fg=corDaLetra)
lblResult.place(x=50, y=10)
lblLinha5 = Label(frmResultado, width=500, height=1, anchor=NW, font='Verdana 1 ', bg=corVerde, fg=corBranco)
lblLinha5.place(x=0, y=47)
lblLinha6 = Label(frmResultado, width=500, height=1, anchor=NW, font='Verdana 1 ', bg=corBranco, fg=corBranco)
lblLinha6.place(x=0, y=50)

lblLinhaVerti2 = tk.Label(frmResultado, width=1, height=505, anchor=NW, font='Roboto 10',
                          bg=corVerde, fg=corBranco)
lblLinhaVerti2.place(x=247, y=0)

lblNomeLucro = Label(frmResultado, text="", wraplength=220, justify=LEFT, pady=2, height=3, anchor=NW,
                     font=' Ivy 10', bg=corBranco, fg=corDaLetra)
lblNomeLucro.place(x=10, y=70)
lblLucro = Label(frmResultado, text="R$0,00", width=20, height=1, anchor=E, relief=RIDGE, font=' Ivy 15',
                 bg=corBranco, fg=corDaLetra)
lblLucro.place(x=10, y=140)

lblCusto = Label(frmResultado, text="0,00%", width=20, height=1, anchor=E, relief=RIDGE, font=' Ivy 15',
                 bg=corBranco, fg=corDaLetra)
lblCusto.place(x=10, y=180)
lucro()


def graficoBar():
    lblGrafico = Label(frmChart, text="Estatísticas dos produtos salvos", compound=LEFT, padx=10, relief=FLAT,
                       anchor=NW, font='Verdana 11 bold', bg=corBranco, fg=corDaLetra)
    lblGrafico.place(x=60, y=10)
    lblLinha7 = Label(frmChart, width=500, height=1, anchor=NW, font='Verdana 1 ', bg=corVerde, fg=corBranco)
    lblLinha7.place(x=0, y=47)
    lblLinha8 = Label(frmChart, width=500, height=1, anchor=NW, font='Verdana 1 ', bg=corBranco, fg=corBranco)
    lblLinha8.place(x=0, y=50)

    lblLinhaVertical4 = tk.Label(frmChart, width=1, height=505, anchor=NW, font='Roboto 1',
                                 bg=corVerde, fg=corBranco)
    lblLinhaVertical4.place(x=372, y=0)


# obtendo valores
listaNomes = ['Valor total de custo', 'Lucro líquido total', 'Margem de lucro total']
listaValores = estatistica()
simbolos = ['R$', 'R$', '%']

# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(6.2, 3.5), dpi=60)
ax = figura.add_subplot(111)
# ax.autoscale(enable=True, axis='both', tight=None)
ax.bar(listaNomes, listaValores, color=cor1, width=0.5)

# crie uma lista para coletar os dados plt.patches
c = 0

# definir rótulos de barras individuais usando a lista acima
for i in ax.patches:
    if c == 2:
        # get_x puxa para a esquerda ou para a direita; get_height empurra para cima ou para baixo
        ax.text(i.get_x() - .001, i.get_height() + .5, str("{:,.0f}".format(listaValores[c]) + simbolos[c]),
                fontsize=17, fontstyle='italic', verticalalignment='bottom', color='dimgrey')
    else:
        # get_x puxa para a esquerda ou para a direita; get_height empurra para cima ou para baixo
        ax.text(i.get_x() - .001, i.get_height() + .5, str(simbolos[c] + "{:,.0f}".format(listaValores[c])),
                fontsize=17, fontstyle='italic', verticalalignment='bottom', color='dimgrey')

    c += 1

ax.set_xticks(np.arange(len(listaNomes)))
ax.set_xticklabels(listaNomes, fontsize=12)
ax.patch.set_facecolor('#ffffff')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

canva = FigureCanvasTkAgg(figura, frmChart)
canva.get_tk_widget().place(x=0, y=50)
graficoBar()



# função para mostrar
def mostrar():
    # criando uma visualização em árvore com barras de rolagem duplas
    listaDados = ['Nome do produto', 'Preço de Compra($)', 'Preço de Venda(R$)', 'Qtd', 'Custos Adicionais(R$)',
                  'Custo Médio de Frete(R$)', 'Custo total', 'Lucro Líquido(R$)', 'Margem de Lucro (%)']

    dfList = obterDadosExcel("dados.xlsx")

    global tree

    tree = ttk.Treeview(frmTabela, selectmode="extended", columns=listaDados, show="headings")
    # vertical scrollbar
    verticalScrBar = ttk.Scrollbar(frmTabela, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    horizontalScrBar = ttk.Scrollbar(frmTabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=verticalScrBar.set, xscrollcommand=horizontalScrBar.set)

    tree.grid(column=0, row=1, sticky='nsew')
    verticalScrBar.grid(column=1, row=1, sticky='ns')
    horizontalScrBar.grid(column=0, row=2, sticky='ew')
    frmTabela.grid_rowconfigure(0, weight=12)

    hd = ["nw", "center", "center", "center", "center", "center", "center", "center", "center"]
    h = [150, 120, 110, 40, 130, 150, 80, 110, 130]
    n = 0

    for col in listaDados:
        tree.heading(col, text=col.title(), anchor=NW)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in dfList:
        tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()
