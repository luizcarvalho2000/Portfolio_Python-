from tkinter import *
from tkinter import ttk
from dados import *

# Importando Pillow
from PIL import Image, ImageTk

# Cores

co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#6f9fbd"  # Azul
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#ef5350"  # Vermelho
co6 = "#f7ff08"  #amarelo

# Criando janelas

janela = Tk()
janela.title('Pokedex')
janela.geometry('905x510')
janela.configure(bg=co1)
janela.iconbitmap('images/pokeball.ico')

ttk.Separator(janela, orient=HORIZONTAL).place(x=10, y=305, relwidth=1)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Criando frame Pokemon
framePokemon = Frame(janela, width=885, height=304, relief='flat')
framePokemon.pack(fill='both', expand=True)

frameStatus = Frame(janela, width=350, height=204, relief='flat')
frameStatus.place(x=10, y=300)

def trocarPokemon(i):
    global imagemPokemon, pokeImagem

    # Trocando cor do frame
    framePokemon['bg'] = pokemon[i]['tipo'][3]

    # tipo de pokemon
    pokeNome['text'] = i
    pokeNome['bg'] = pokemon[i]['tipo'][3]
    pokeTipo['text'] = pokemon[i]['tipo'][1]
    pokeTipo['bg'] = pokemon[i]['tipo'][3]
    pokeId['text'] = pokemon[i]['tipo'][0]
    pokeId['bg'] = pokemon[i]['tipo'][3]

    imagemPokemon = pokemon[i]['tipo'][2]

    imagemPokemon = Image.open(imagemPokemon)
    imagemPokemon = imagemPokemon.resize((238, 238))
    imagemPokemon = ImageTk.PhotoImage(imagemPokemon)

    pokeImagem = Label(framePokemon, image=imagemPokemon, relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pokeImagem.place(x=50, y=75)

    pokeTipo.lift()

    # pokeStatus
    pokeHp['text'] = pokemon[i]['status'][0]
    pokeAtack['text'] = pokemon[i]['status'][1]
    pokeDef['text'] = pokemon[i]['status'][2]
    pokeVel['text'] = pokemon[i]['status'][3]
    pokeTotal['text'] = pokemon[i]['status'][4]

    # PokeHabilidade

    pokeHab1['text'] = pokemon[i]['habilidades'][0]
    pokeHab2['text'] = pokemon[i]['habilidades'][1]
    pokeHab3['text'] = pokemon[i]['habilidades'][2]
    pokeHab4['text'] = pokemon[i]['habilidades'][3]


# Criando label

# Nome
pokeNome = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pokeNome.place(x=12, y=15)


# Categoria
pokeTipo = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=co1)
pokeTipo.place(x=12, y=50)

# Id
pokeId = Label(framePokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=co1)
pokeId.place(x=12, y=75)

# Status

pokeStatus = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pokeStatus.place(x=15, y=310)

# Hp

pokeHp = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHp.place(x=15, y=360)

# Ataque
pokeAtack = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeAtack.place(x=15, y=385)

# Defesa
pokeDef = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeDef.place(x=15, y=410)

# Velocidade
pokeVel = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeVel.place(x=15, y=435)

# Total
pokeTotal = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeTotal.place(x=15, y=460)

# Habilidades

pokeHab = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pokeHab.place(x=180, y=310)

# Habilidade 1

pokeHab1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab1.place(x=195, y=360)

# Habilidade 2
pokeHab2 = Label(janela, text='Calda de Ferro', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab2.place(x=195, y=385)

# Habilidade 3
pokeHab3 = Label(janela, text='Bola Eletrica', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab3.place(x=195, y=410)

# Habilidade 4
pokeHab4 = Label(janela, text='Ataque Rapido', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab4.place(x=195, y=435)

# Criando botões de navegação

# Imagem do pokemon

imagemPokemon1 = Image.open("images/cabeça-bulbasaur.png")
imagemPokemon1 = imagemPokemon1.resize((40, 40))
imagemPokemon1 = ImageTk.PhotoImage(imagemPokemon1)

btnPokeImagem1 = Button(janela, image=imagemPokemon1, text="Bulbasaur",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Bulbasaur"))
btnPokeImagem1.place(x=375, y=5)

imagemPokemon2 = Image.open("images/cabeça-Ivysaur.png")
imagemPokemon2 = imagemPokemon2.resize((40, 40))
imagemPokemon2 = ImageTk.PhotoImage(imagemPokemon2)

btnPokeImagem2 = Button(janela, image=imagemPokemon2, text="Ivysaur",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Ivysaur"))
btnPokeImagem2.place(x=375, y=60)

imagemPokemon3 = Image.open("images/cabeça-Venusaur.png")
imagemPokemon3 = imagemPokemon3.resize((40, 40))
imagemPokemon3 = ImageTk.PhotoImage(imagemPokemon3)

btnPokeImagem3 = Button(janela, image=imagemPokemon3, text="Venusaur",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Venusaur"))
btnPokeImagem3.place(x=375, y=115)

imagemPokemon4 = Image.open("images/cabeça-charmander.png")
imagemPokemon4 = imagemPokemon4.resize((40, 40))
imagemPokemon4 = ImageTk.PhotoImage(imagemPokemon4)

btnPokeImagem4 = Button(janela, image=imagemPokemon4, text="Charmander",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Charmander"))
btnPokeImagem4.place(x=375, y=170)

imagemPokemon5 = Image.open("images/cabeça-Charmeleon.png")
imagemPokemon5 = imagemPokemon5.resize((40, 40))
imagemPokemon5 = ImageTk.PhotoImage(imagemPokemon5)

btnPokeImagem5 = Button(janela, image=imagemPokemon5, text="Charmeleon",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Charmeleon"))
btnPokeImagem5.place(x=375, y=225)

imagemPokemon6 = Image.open("images/cabeça-Charizard.png")
imagemPokemon6 = imagemPokemon6.resize((40, 40))
imagemPokemon6 = ImageTk.PhotoImage(imagemPokemon6)

btnPokeImagem6 = Button(janela, image=imagemPokemon6, text="Charizard",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Charizard"))
btnPokeImagem6.place(x=375, y=280)

imagemPokemon7 = Image.open("images/cabeça-Squirtle.png")
imagemPokemon7 = imagemPokemon7.resize((40, 40))
imagemPokemon7 = ImageTk.PhotoImage(imagemPokemon7)

btnPokeImagem7 = Button(janela, image=imagemPokemon7, text="Squirtle",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Squirtle"))
btnPokeImagem7.place(x=375, y=335)

imagemPokemon8 = Image.open("images/cabeça-Wartortle.png")
imagemPokemon8 = imagemPokemon8.resize((40, 40))
imagemPokemon8 = ImageTk.PhotoImage(imagemPokemon8)

btnPokeImagem8 = Button(janela, image=imagemPokemon8, text="Wartortle",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Wartortle"))
btnPokeImagem8.place(x=375, y=390)

imagemPokemon9 = Image.open("images/cabeça-Blastoise.png")
imagemPokemon9 = imagemPokemon9.resize((40, 40))
imagemPokemon9 = ImageTk.PhotoImage(imagemPokemon9)

btnPokeImagem9 = Button(janela, image=imagemPokemon9, text="Blastoise",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Blastoise"))
btnPokeImagem9.place(x=375, y=445)

imagemPokemon10 = Image.open("images/cabeça-Carterpie.png")
imagemPokemon10 = imagemPokemon10.resize((40, 40))
imagemPokemon10 = ImageTk.PhotoImage(imagemPokemon10)

btnPokeImagem10 = Button(janela, image=imagemPokemon10, text="Caterpie",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Caterpie"))
btnPokeImagem10.place(x=550, y=5)

imagemPokemon11 = Image.open("images/cabeça-Metapod.png")
imagemPokemon11 = imagemPokemon11.resize((40, 40))
imagemPokemon11 = ImageTk.PhotoImage(imagemPokemon11)

btnPokeImagem11 = Button(janela, image=imagemPokemon11, text="Metapod",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Metapod"))
btnPokeImagem11.place(x=550, y=60)

imagemPokemon12 = Image.open("images/cabeça-Butterfree.png")
imagemPokemon12 = imagemPokemon12.resize((40, 40))
imagemPokemon12 = ImageTk.PhotoImage(imagemPokemon12)

btnPokeImagem12 = Button(janela, image=imagemPokemon12, text="Butterfree",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Butterfree"))
btnPokeImagem12.place(x=550, y=115)

imagemPokemon13 = Image.open("images/cabeça-Pichu.png")
imagemPokemon13 = imagemPokemon13.resize((40, 40))
imagemPokemon13 = ImageTk.PhotoImage(imagemPokemon13)

btnPokeImagem13 = Button(janela, image=imagemPokemon13, text="Pichu",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("pichu"))
btnPokeImagem13.place(x=550, y=170)

imagemPokemon14 = Image.open("images/cabeça-pikachu.png")
imagemPokemon14 = imagemPokemon14.resize((40, 40))
imagemPokemon14 = ImageTk.PhotoImage(imagemPokemon14)

btnPokeImagem14 = Button(janela, image=imagemPokemon14, text="Pikachu",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Pikachu"))
btnPokeImagem14.place(x=550, y=225)

imagemPokemon15 = Image.open("images/cabeça-Raichu.png")
imagemPokemon15 = imagemPokemon15.resize((40, 40))
imagemPokemon15 = ImageTk.PhotoImage(imagemPokemon15)

btnPokeImagem15 = Button(janela, image=imagemPokemon15, text="Raichu",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Raichu"))
btnPokeImagem15.place(x=550, y=280)

imagemPokemon16 = Image.open("images/cabeça-Magikarp.png")
imagemPokemon16 = imagemPokemon16.resize((40, 40))
imagemPokemon16 = ImageTk.PhotoImage(imagemPokemon16)

btnPokeImagem16 = Button(janela, image=imagemPokemon16, text="Magikarp",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Magikarp"))
btnPokeImagem16.place(x=550, y=335)

imagemPokemon17 = Image.open("images/cabeça-gyarados.png")
imagemPokemon17 = imagemPokemon17.resize((40, 40))
imagemPokemon17 = ImageTk.PhotoImage(imagemPokemon17)

btnPokeImagem17 = Button(janela, image=imagemPokemon17, text="Gyarados",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Gyarados"))
btnPokeImagem17.place(x=550, y=390)

imagemPokemon18 = Image.open("images/cabeça-Gastly.png")
imagemPokemon18 = imagemPokemon18.resize((40, 40))
imagemPokemon18 = ImageTk.PhotoImage(imagemPokemon18)

btnPokeImagem18 = Button(janela, image=imagemPokemon18, text="Gastly",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Gastly"))
btnPokeImagem18.place(x=550, y=445)

imagemPokemon19 = Image.open("images/cabeça-Haunter.png")
imagemPokemon19 = imagemPokemon19.resize((40, 40))
imagemPokemon19 = ImageTk.PhotoImage(imagemPokemon19)

btnPokeImagem19 = Button(janela, image=imagemPokemon19, text="Haunter",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Haunter"))
btnPokeImagem19.place(x=725, y=5)

imagemPokemon20 = Image.open("images/cabeça-gengar.png")
imagemPokemon20 = imagemPokemon20.resize((40, 40))
imagemPokemon20 = ImageTk.PhotoImage(imagemPokemon20)

btnPokeImagem20 = Button(janela, image=imagemPokemon20, text="Gengar",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Gengar"))
btnPokeImagem20.place(x=725, y=60)

imagemPokemon21 = Image.open("images/cabeça-Snorlax.png")
imagemPokemon21 = imagemPokemon21.resize((40, 40))
imagemPokemon21 = ImageTk.PhotoImage(imagemPokemon21)

btnPokeImagem21 = Button(janela, image=imagemPokemon21, text="Snorlax",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Snorlax"))
btnPokeImagem21.place(x=725, y=115)

imagemPokemon22 = Image.open("images/cabeça-Articuno.png")
imagemPokemon22 = imagemPokemon22.resize((40, 40))
imagemPokemon22 = ImageTk.PhotoImage(imagemPokemon22)

btnPokeImagem22 = Button(janela, image=imagemPokemon22, text="Articuno",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Articuno"))
btnPokeImagem22.place(x=725, y=170)

imagemPokemon23 = Image.open("images/cabeça-Zapdos.png")
imagemPokemon23 = imagemPokemon23.resize((40, 40))
imagemPokemon23 = ImageTk.PhotoImage(imagemPokemon23)

btnPokeImagem23 = Button(janela, image=imagemPokemon23, text="Zapdos",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Zapdos"))
btnPokeImagem23.place(x=725, y=225)

imagemPokemon24 = Image.open("images/cabeça-Moltres.png")
imagemPokemon24 = imagemPokemon24.resize((40, 40))
imagemPokemon24 = ImageTk.PhotoImage(imagemPokemon24)

btnPokeImagem24 = Button(janela, image=imagemPokemon24, text="Moltres",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Moltres"))
btnPokeImagem24.place(x=725, y=280)

imagemPokemon25 = Image.open("images/cabeça-Dragonite.png")
imagemPokemon25 = imagemPokemon25.resize((40, 40))
imagemPokemon25 = ImageTk.PhotoImage(imagemPokemon25)

btnPokeImagem25 = Button(janela, image=imagemPokemon25, text="Dragonite",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Dragonite"))
btnPokeImagem25.place(x=725, y=335)

imagemPokemon26 = Image.open("images/cabeça-Mewtwo.png")
imagemPokemon26 = imagemPokemon26.resize((40, 40))
imagemPokemon26 = ImageTk.PhotoImage(imagemPokemon26)

btnPokeImagem26 = Button(janela, image=imagemPokemon26, text="Mewtwo",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Mewtwo"))
btnPokeImagem26.place(x=725, y=390)

imagemPokemon27 = Image.open("images/cabeça-Mew.png")
imagemPokemon27 = imagemPokemon27.resize((40, 40))
imagemPokemon27 = ImageTk.PhotoImage(imagemPokemon27)

btnPokeImagem27 = Button(janela, image=imagemPokemon27, text="Mew",width=150, relief=RAISED, overrelief=RIDGE,
                        compound=LEFT, anchor=NW,  padx=5, font=('Verdana 12 bold'), bg=co1, fg=co0, command=lambda:trocarPokemon("Mew"))
btnPokeImagem27.place(x=725, y=445)

# Inicializando com o primeiro pokemon
trocarPokemon("Bulbasaur")

janela.mainloop()
