from tkinter import *
from tkinter import messagebox, PhotoImage, Frame

# Variável global para armazenar a expressão
expressao = ""

# Função para atualizar o valor na tela
def atualizarDisplay(valor):
    global expressao
    # Verifica se o valor é vírgula ou ponto
    if valor in {',', '.'}:
        # Verifica se já existe um ponto ou vírgula na expressão
        if '.' not in expressao and ',' not in expressao:
            expressao += str(valor)
    else:
        ultimo_caractere = expressao[-1] if expressao else None
        # Verifica se o último caractere é um operador
        if ultimo_caractere in {'+', '-', '*', '/'} and valor in {'+', '-', '*', '/'}:
            expressao = expressao[:-1]
        expressao += str(valor)
    valorTxt.set(expressao)

# Função para calcular a expressão
def calcularResultado():
    global expressao
    try:
        expressao = expressao.replace('x²', '**2').replace('¹x', '**1').replace('%', '/100').replace('√²', '**0.5')
        resultado = str(eval(expressao))
        valorTxt.set(resultado)
        expressao = resultado
    except Exception as e:
        valorTxt.set('')
        messagebox.showinfo("ERRO!", "DIGITE UM NUMERO!")

# Função para limpar o display
def limparDisplay():
    global expressao
    expressao = ""
    valorTxt.set("")

# Função para limpar o último caractere
def limparUltimo():
    global expressao
    expressao = expressao[:-1]
    valorTxt.set(expressao)

# Função para executar operações matemáticas
def executarOperacao(operador):
    global expressao
    expressao += operador
    atualizarDisplay(operador)

# Cores
co0 = "#3b3b3b"  # Preto
co1 = "#feffff"  # Branco
co2 = "#38576b"  # Azul
co3 = "#ECEFF1"  # Cinza
co4 = "#FFAB40"  # Laranja
co5 = "#708090"  # Cinza Claro
co6 = "#c9c9c9"  # Prata

# Janela Principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("285x325")
janela.configure(background=co0)

# Frame Display
frameDisplay = Frame(janela, width=285, height=50, bd=2, relief=GROOVE)
frameDisplay.grid(row=0, column=0)
frameDisplay.configure(background=co2)

# Frame Botões
frameBotões: Frame = Frame(janela, width=285, height=322, bd=2, relief=GROOVE)
frameBotões.grid(row=1, column=0)

# Label
valorTxt = StringVar()
lblDisplay = Label(frameDisplay, textvariable=valorTxt, width=16, height=2, padx=7, relief=FLAT, anchor="e",
                   justify=RIGHT, font=('Robolt 20 bold'), bg=co2, fg=co1)
lblDisplay.place(x=0, y=0)

# Botões
imgBotaos: PhotoImage = PhotoImage(file="C:\Projetos pessoais\Python\Calculadora\Imagens\setinha.png")
btnBackspace = Button(frameBotões, image=imgBotaos, width=60, height=35, font=('Robolt 8 bold'), relief=RAISED,
                      overrelief=RIDGE, bg=co6, command=limparUltimo)
btnBackspace.place(x=210, y=0)

btnCE = Button(frameBotões, text="CE", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
               overrelief=RIDGE, bg=co6, fg=co0, command=limparDisplay)
btnCE.place(x=70, y=0)

btnC = Button(frameBotões, text="C", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
              overrelief=RIDGE, bg=co6, fg=co0, command=limparUltimo)
btnC.place(x=140, y=0)

btnDivisao = Button(frameBotões, text="/", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
                    overrelief=RIDGE, bg=co5, fg=co0, command=lambda: executarOperacao('/'))
btnDivisao.place(x=210, y=45)

btnSomar = Button(frameBotões, text="+", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
                  overrelief=RIDGE, bg=co5, fg=co0, command=lambda: executarOperacao('+'))
btnSomar.place(x=210, y=180)

btnVirgula = Button(frameBotões, text=",", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
                    overrelief=RIDGE, bg=co5, fg=co0, command=lambda: executarOperacao(','))
btnVirgula.place(x=0, y=225)

btnSubtracao = Button(frameBotões, text="-", width=8, font=('Robolt 8 bold'), relief=RAISED,
                      overrelief=RIDGE, height=2, bg=co5, fg=co0, command=lambda: executarOperacao('-'))
btnSubtracao.place(x=210, y=135)

btnMultiplicacao = Button(frameBotões, text="*", width=8, font=('Robolt 8 bold'), relief=RAISED,
                          overrelief=RIDGE, height=2, bg=co5, fg=co0, command=lambda: executarOperacao('*'))
btnMultiplicacao.place(x=210, y=90)

btnPonto = Button(frameBotões, text=".", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
                  overrelief=RIDGE, bg=co5, fg=co0, command=lambda: executarOperacao('.'))
btnPonto.place(x=140, y=225)

btnIgual = Button(frameBotões, text="=", width=8, height=2, font=('Robolt 8 bold'), relief=RAISED,
                  overrelief=RIDGE, bg=co5, fg=co0, command=calcularResultado)
btnIgual.place(x=210, y=225)

botoes = [
    ("%", 0, 0),
    ("¹x", 0, 45), ("x²", 70, 45), ("√²", 140, 45),
    ("7", 0, 90), ("8", 70, 90), ("9", 140, 90),
    ("4", 0, 135), ("5", 70, 135), ("6", 140, 135),
    ("1", 0, 180), ("2", 70, 180), ("3", 140, 180),
    ("0", 70, 225)
]

for texto, x, y in botoes:
    btn = Button(frameBotões, text=texto, width=8, height=2, font=('Robolt 8 bold'),
                 relief=RAISED, overrelief=RIDGE, bg=co6, fg=co0,
                 command=lambda t=texto: atualizarDisplay(t) if t != "=" else calcularResultado())
    btn.place(x=x, y=y)

janela.mainloop()