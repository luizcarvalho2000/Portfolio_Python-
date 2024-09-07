from DAO import PreferenciasDAO as PreferenciasDAO
from MODEL.PreferenciasVO import PreferenciasVO


class Preferencias:
    def __init__(self):
        super().__init__()

    objPreferenciasDAO = PreferenciasDAO
    objPreferenciasVO = PreferenciasVO

    @staticmethod
    def impTxtWhile():
        try:
            lista = []

            with open("../Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:
                strLinhaLida = arqPreferencias.readline()

                while strLinhaLida != "":
                    lista.append(strLinhaLida)
                    strLinhaLida = arqPreferencias.readline()

            return lista

        except Exception as erro:
            raise Exception(f"Erro ao consultar preferencias: {erro}")

    @staticmethod
    def impTxtFor():
        try:
            lista = []

            with open("../Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:
                arrStrLinhaLida = arqPreferencias.readlines()

            for item in arrStrLinhaLida:
                lista.append(item)

            return lista

        except Exception as erro:
            raise Exception(f"Erro ao consultar preferencias: {erro}")

    @staticmethod
    def impTxtForEach():
        try:
            lista = []

            with open("../Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:
                for item in arqPreferencias:
                    lista.append(item)

            return lista

        except Exception as erro:
            return str(erro)

    # Para os métodos que interagem com a instância de PreferenciasDAO, é mantido o self
    def impBdConect(self):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()
            return objPreferenciasDAO.impBdConect()

        except Exception as erro:
            raise Exception(f"Erro ao consultar preferencias: {erro}")

    def impBdDesconect(self):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()
            return objPreferenciasDAO.impBdDesconect()

        except Exception as erro:
            raise Exception(f"Erro ao consultar preferencias: {erro}")

    def consultBd(self, objPreferenciasVO):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

            return objPreferenciasDAO.consultarBd(objPreferenciasVO)

        except Exception as erro:
            raise Exception(f" erro ao consultar preferencias: {erro}")

    def inserirBd(self, objPreferenciasVO):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

            return objPreferenciasDAO.inserirBd(objPreferenciasVO)

        except Exception as erro:
            raise Exception(f" erro ao consultar preferencias: {erro}")

    def excluirBd(self, objPreferenciasVO):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

            return objPreferenciasDAO.excluirBd(objPreferenciasVO)

        except Exception as erro:
            return str(erro)

    def alterarBd(self, objPreferenciasVO):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

            return objPreferenciasDAO.alterarBd(objPreferenciasVO)

        except Exception as erro:
            raise Exception(f" erro ao consultar preferencias: {erro}")
