import tkinter
from tkinter import *
from tkinter import ttk, messagebox

# ----- cores -----

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"  # azul / blue
co5 = "#fff873"  # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"  # vermelha / red
co8 = co4        # +verde
co10 ="#fcfbf7"  # Branco
fundo = "#3b3b3b" #black

# ----- Criando janela principal -----

janela = Tk()
janela.title("Jogo da Velha")
janela.geometry("260x370")
janela.configure(bg=fundo)

# ----- Criando Frames -----

frameCima = Frame(janela, width=240, height=100, bg=co1, relief=RAISED)
frameCima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frameBaixo = Frame(janela, width=240, height=300, bg=fundo, relief=FLAT)
frameBaixo.grid(row=1, column=0, sticky=NW)

# ----- Criando Labels para frames -----

labelX = Label(frameCima, text="X",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 40 bold'), bg=co1, fg=co7)
labelX.place(x=25, y=10)
labelX = Label(frameCima, text="Jogador 1",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 7 bold'), bg=co1, fg=co0)
labelX.place(x=17, y=70)
labelXPontos = Label(frameCima, text="0",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 30 bold'), bg=co1, fg=co0)
labelXPontos.place(x=80, y=20)

labelSeparador = Label(frameCima, text=":",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 30 bold'), bg=co1, fg=co0)
labelSeparador.place(x=110, y=15)

labelO = Label(frameCima, text="O",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 40 bold'), bg=co1, fg=co4)
labelO.place(x=170, y=10)
labelO = Label(frameCima, text="Jogador 2",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 7 bold'), bg=co1, fg=co0)
labelO.place(x=165, y=70)
labelOPontos = Label(frameCima, text="0",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 30 bold'), bg=co1, fg=co0)
labelOPontos.place(x=130, y=20)

# ----- Funções -----

player1 = "X"
player2 = "O"

score1 = 0
score2 = 0

tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

jogando = 'X'
jogar = ''
contador = 0
contadorDeRodadas = 0

# função para iniciar o jogo
def iniciarJogo():
    btnJogar.place(x=85, y=500)
    global contador
    contador = 0
    # função para controlar jogo
    def controlarJogo(i):
        global jogando
        global contador
        global jogar
        global cor

        # comparando valor recebido

        if i == str(1):
            #verifica se aquele botão esta vazio
            if btn0['text'] == '':
                #Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                #Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn0['fg'] = cor
                btn0['text'] = jogando
                tabela[0][0] = jogando

                #verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(2):
            #verifica se aquele botão esta vazio
            if btn1['text'] == '':
                #Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                #Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn1['fg'] = cor
                btn1['text'] = jogando
                tabela[0][1] = jogando

                #verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(3):
            # verifica se aquele botão esta vazio
            if btn2['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn2['fg'] = cor
                btn2['text'] = jogando
                tabela[0][2] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(4):
            # verifica se aquele botão esta vazio
            if btn3['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn3['fg'] = cor
                btn3['text'] = jogando
                tabela[1][0] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(5):
            # verifica se aquele botão esta vazio
            if btn4['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn4['fg'] = cor
                btn4['text'] = jogando
                tabela[1][1] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(6):
            # verifica se aquele botão esta vazio
            if btn5['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn5['fg'] = cor
                btn5['text'] = jogando
                tabela[1][2] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(7):
            # verifica se aquele botão esta vazio
            if btn6['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn6['fg'] = cor
                btn6['text'] = jogando
                tabela[2][0] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(8):
            # verifica se aquele botão esta vazio
            if btn7['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn7['fg'] = cor
                btn7['text'] = jogando
                tabela[2][1] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        if i == str(9):
            # verifica se aquele botão esta vazio
            if btn8['text'] == '':
                # Verificando quem está jogando
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8
                # Definindo a cor do texto do botão
                # e marcar aquela posição da tabela
                # com valor do jogador atual

                btn8['fg'] = cor
                btn8['text'] = jogando
                tabela[2][2] = jogando

                # verificando quem esta jogando
                # para poder trocar o player
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # contador para proxima rodada
                contador += 1

        # Após o contador ser maior ou igual a 5,
        # verifica se o ouve algum vencedor de acordo
        # com os padrões seguinte dentro da tabela

        if contador >= 5:
            # linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                vencedor(jogando)

            # Colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                vencedor(jogando)

            # Diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                vencedor(jogando)

            # Verificar empate
            if contador >= 9:
                vencedor('EMPATE')



    # função para decidir o vencedor
    def vencedor(i):

        global score1
        global score2
        global tabela
        global contadorDeRodadas
        global contador

        # bloqueando botoes
        btn0['state'] = 'disable'
        btn1['state'] = 'disable'
        btn2['state'] = 'disable'
        btn3['state'] = 'disable'
        btn4['state'] = 'disable'
        btn5['state'] = 'disable'
        btn6['state'] = 'disable'
        btn7['state'] = 'disable'
        btn8['state'] = 'disable'

        # Label de quem é o vencedor
        lblVencedor = Label(frameBaixo, text="", width=17, relief=FLAT, anchor=CENTER, font=('Ivy, 13 bold'), bg=co1, fg=co2)
        lblVencedor.place(x=40, y=180)

        def start():
            global tabela
            global contador

            contador = 0
            # Limpa o tabuleiro
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]



            btn0['text'] = ''
            btn1['text'] = ''
            btn2['text'] = ''
            btn3['text'] = ''
            btn4['text'] = ''
            btn5['text'] = ''
            btn6['text'] = ''
            btn7['text'] = ''
            btn8['text'] = ''

            btn0['state'] = 'normal'
            btn1['state'] = 'normal'
            btn2['state'] = 'normal'
            btn3['state'] = 'normal'
            btn4['state'] = 'normal'
            btn5['state'] = 'normal'
            btn6['state'] = 'normal'
            btn7['state'] = 'normal'
            btn8['state'] = 'normal'

            lblVencedor.destroy()
            btnJogar.destroy()

        if i == 'O':
            lblVencedor['text'] = "Jogador 1 venceu!"
            score1 += 1
            labelXPontos['text'] = score1

        if i == 'X':
            lblVencedor['text'] = "Jogador 2 venceu!"
            score2 += 1
            labelOPontos['text'] = score2

        if i == 'EMPATE':
            lblVencedor['text'] = "Deu Velha!"

        # Botão próxima rodada
        btnJogar = Button(frameBaixo, text="proxima rodada", width=15, height=1, relief=RAISED, font=('Ivy, 10 bold'), overrelief=RIDGE, bg=fundo, fg=co0, command=start)
        btnJogar.place(x=65, y=210)

        def gameOver():
            global tabela
            global contadorDeRodadas
            global contador
            global jogando

            # Limpa o tabuleiro
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0
            contadorDeRodadas = 0
            jogando = ''

            # Limpa os botões
            btn0['text'] = ''
            btn1['text'] = ''
            btn2['text'] = ''
            btn3['text'] = ''
            btn4['text'] = ''
            btn5['text'] = ''
            btn6['text'] = ''
            btn7['text'] = ''
            btn8['text'] = ''

            # Habilita os botões
            btn0['state'] = 'normal'
            btn1['state'] = 'normal'
            btn2['state'] = 'normal'
            btn3['state'] = 'normal'
            btn4['state'] = 'normal'
            btn5['state'] = 'normal'
            btn6['state'] = 'normal'
            btn7['state'] = 'normal'
            btn8['state'] = 'normal'

            btnJogar.destroy()
            lblVencedor.destroy()
            terminar()

        if contadorDeRodadas>=4:
            if score1 > score2:
                lblVencedor['text'] = "Jogador 1 venceu o jogo!"
            elif score2 > score1:
                lblVencedor['text'] = "Jogador 2 venceu o jogo!"
            else:
                lblVencedor['text'] = "O jogo terminou em empate!"
            gameOver()

        else:
            contadorDeRodadas += 1
            # Iniciando a tabela
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0


    # função para terminar o jogo
    def terminar():
        global tabela
        global contadorDeRodadas
        global score1
        global score2
        global contador


        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        contadorDeRodadas = 0
        score1 = 0
        score2 = 0
        contador = 0

        # bloqueando botoes
        btn0['state'] = 'disable'
        btn1['state'] = 'disable'
        btn2['state'] = 'disable'
        btn3['state'] = 'disable'
        btn4['state'] = 'disable'
        btn5['state'] = 'disable'
        btn6['state'] = 'disable'
        btn7['state'] = 'disable'
        btn8['state'] = 'disable'

        lblGameOver = Label(frameBaixo, text="Jogar de Novo", width=17, relief=FLAT, anchor=CENTER, font=('Ivy, 13 bold'), bg=co1, fg=co2)
        lblGameOver.place(x=65, y=180)

        # Jogar Nova Partida
        def jogarNovamente():
            labelXPontos['text'] = 0
            labelOPontos['text'] = 0
            lblGameOver.destroy()
            btnJogarNovamente.destroy()

            # chamando Funcao iniciar jogo

            iniciarJogo()

        btnJogarNovamente = Button(frameBaixo, text="Jogar Novamente", width=15, height=1, relief=RAISED, font=('Ivy, 10 bold'), overrelief=RIDGE, bg=fundo, fg=co0, command=jogarNovamente)
        btnJogarNovamente.place(x=75, y=210)


     # Linhas Verticais

    linha1 = Label(frameBaixo, text="",height=23, pady=5, relief=FLAT, anchor=CENTER, font=('Ivy, 5 bold'), bg=co0, fg=co7)
    linha1.place(x=90, y=15)

    linha2 = Label(frameBaixo, text="",height=23, pady=5, relief=FLAT, anchor=CENTER, font=('Ivy, 5 bold'), bg=co0, fg=co7)
    linha2.place(x=174, y=15)

    # Linhas Horizontais

    linha3 = Label(frameBaixo, text="", width=200, padx=2, relief=FLAT, anchor=CENTER, font=('Ivy, 5 bold'), bg=co0, fg=co7)
    linha3.place(x=30, y=63)

    linha4 = Label(frameBaixo, text="", width=200, padx=2, relief=FLAT, anchor=CENTER, font=('Ivy, 1 bold'), bg=co0, fg=co7)
    linha4.place(x=30, y=130)

    # ----- Criando Botões -----

    btn0 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('1'))
    btn0.place(x=30, y=15)

    btn1 = Button(frameBaixo, text="", width=4, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('2'))
    btn1.place(x=96, y=15)

    btn2 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('3'))
    btn2.place(x=180, y=15)

    # Linha 1

    btn3 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('4'))
    btn3.place(x=30, y=75)

    btn4 = Button(frameBaixo, text="", width=4, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('5'))
    btn4.place(x=96, y=75)

    btn5 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('6'))
    btn5.place(x=180, y=75)
    # Linha 2

    btn6 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('7'))
    btn6.place(x=30, y=135)

    btn7 = Button(frameBaixo, text="", width=4, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('8'))
    btn7.place(x=96, y=135)

    btn8 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7, command=lambda:controlarJogo('9'))
    btn8.place(x=180, y=135)


# ---- Botão jogar ----

btnJogar = Button(frameBaixo, text="Jogar", width=10, height=1, relief=RAISED, font=('Ivy, 10 bold'), overrelief=RIDGE, bg=fundo, fg=co0, command=iniciarJogo)
btnJogar.place(x=85, y=210)

janela.mainloop()