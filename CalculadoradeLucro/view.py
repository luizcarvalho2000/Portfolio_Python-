import openpyxl


def estatistica():
    # Abre a planilha
    wb = openpyxl.load_workbook("dados.xlsx")
    sheet = wb["lucro"]

    # define as células iniciais e finais dos dados
    primeiraLinha = 2
    ultimaLinha = sheet.max_row

    # Inicializa as variáveis para os totais
    custoTotalTotal = 0
    lucroTotal = 0

    # Criando o total de custo total e lucro
    for linha in range(primeiraLinha, ultimaLinha + 1):
        custoTotalTotal += sheet.cell(row=linha, column=7).value
        lucroTotal += sheet.cell(row=linha, column=8).value

    # Calculando a margem de lucro total
    precoDeVendaTotal = sum(sheet.cell(row=linha, column=3).value for linha in range(primeiraLinha, ultimaLinha + 1))
    margemDeLucroTotal = lucroTotal / precoDeVendaTotal * 100

    custoTotalTotal = float("{:.2f}".format(custoTotalTotal))
    lucroLiquidoTotal = float("{:.2f}".format(lucroTotal))
    margemDeLucroTotal = float("{:.2f}".format(margemDeLucroTotal))

    listaDeDados = [custoTotalTotal, lucroLiquidoTotal, margemDeLucroTotal]

    return listaDeDados

def obterDadosExcel(nomeDoArquivo):
    wb = openpyxl.load_workbook(nomeDoArquivo)
    sheet = wb.active
    dados = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        dados.append(row)
    return dados

'''def calcularLucro(nomeProduto, precoDeCompra, precoDeVenda, quantidade, custosAdicionais, custoFrete):
    # Perguntado ao usuário pelos dados
    nomeProduto = nomeProduto
    precoDeCompra = float(precoDeCompra)
    precoDeVenda = float(precoDeVenda)
    quantidade = int(quantidade)
    custosAdicionais = float(custosAdicionais)
    custoFrete = float(custoFrete)

    # Calculando o lucro
    custoTotal = (precoDeCompra + custosAdicionais) + custoFrete * quantidade
    lucro = (precoDeVenda - precoDeCompra - custosAdicionais - custoFrete) * quantidade
    margemDeLucro = lucro / (precoDeVenda * quantidade) * 100

    # Imprimindo os resultados

    print("O lucro do produto {} é de R$ {:.2f} e a margem de lucro é de {:.2f}%.".format(nomeProduto, lucro, margemDeLucro))
    print("O cisto total do produto {} é de R$ {:.2f}.".format(nomeProduto, custoTotal))'''

def salvarProdutos(nomeProduto, precoDeCompra, precoDeVenda, quantidade, custosAdicionais, custoFrete):

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

    # Salvando os resultados em um arquivo.xlsx

    try:
        wb = openpyxl.load_workbook("dados.xlsx")
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        wb.active.title  = "Resultado da Calculadora de Lucro"
        wb.active.append(["Produto", "Preço de Compra", "Preço de Venda", "Quantidade", "Custos Adicionais", "Custo de Frete", "Custo Total", "Lucro liquido", "Margem de lucro"])

    sheet = wb["lucro"]
    lastRow = sheet.max_row + 1

    sheet.cell(row=lastRow, column=1).value = nomeProduto
    sheet.cell(row=lastRow, column=2).value = precoDeCompra
    sheet.cell(row=lastRow, column=3).value = precoDeVenda
    sheet.cell(row=lastRow, column=4).value = quantidade
    sheet.cell(row=lastRow, column=5).value = custosAdicionais
    sheet.cell(row=lastRow, column=6).value = custoFrete
    sheet.cell(row=lastRow, column=7).value = custoTotal
    sheet.cell(row=lastRow, column=8).value = lucro
    sheet.cell(row=lastRow, column=9).value = margemDeLucro

    wb.save("dados.xlsx")

def deletarLinhaPorNome(nomeProduto, nomePlanilha):
    # Carrega a planilha
    wb = openpyxl.load_workbook(nomePlanilha)
    sheet = wb.active
    contador = 2

    # Percorre a coluna de nomes procurando pelo nome do produto
    for row in sheet.iter_rows(min_row=2, min_col=1, max_col=1, values_only=True):
        if str(row[0]) == nomeProduto:
            # Obtém o número da linha e deleta a linha inteira
            linha = contador
            sheet.delete_rows(linha)
            break

        # Incrementado o contador
        contador += 1

    # Salva as mudanças na planilha
    wb.save(nomePlanilha)
