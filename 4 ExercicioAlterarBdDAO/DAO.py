import os
import pyodbc
import pandas as pdPreferencias

class PreferenciasDAO():
    def __init__(self):
        super().__init__()

    def impBdConect(self):
        try:
            lista = []

            dataBaseName = "Preferencias_3_09022024.accdb"
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            dataBasePath = os.path.join(projectDirectory, dataBaseName)

            connectionString = (
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=' + dataBasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()
            strSQL = "SELECT Descricao FROM Preferencias_3 ORDER BY ID"
            objLeitorBd.execute(strSQL)

            registro = objLeitorBd.fetchone()

            while registro != None:
                lista.append(registro.Descricao)
                registro = objLeitorBd.fetchone()

            objLeitorBd.close()
            objConexao.close()

            return lista

        except Exception as erro:
            return erro

    def impBdDesconect(self):
        try:
            lista = []

            dataBaseName = "Preferencias_3_09022024.accdb"
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            dataBasePath = os.path.join(projectDirectory, dataBaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + dataBasePath + ';'
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
                lista.append(linha.Descricao)
            return lista

        except Exception as erro:
            return erro

    def consultBd(self, parPreferenciasDescricao=None):

        try:
            dataBaseName = "Preferencias_3_09022024.accdb"
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            dataBasePath = os.path.join(projectDirectory, dataBaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + dataBasePath + ';'
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

        except Exception as erro:
            return erro

    def inserirBd(self, descricao):
        global objConexao

        try:
            dataBaseName = "Preferencias_3_09022024.accdb"
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            dataBasePath = os.path.join(projectDirectory, dataBaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + dataBasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()
            strSql = "INSERT INTO Preferencias_3 (Descricao) VALUES (?)"

            objLeitorBd.execute(strSql, descricao)

            objConexao.commit()

            return True

        except Exception as erro:
            return erro
        finally:
            objConexao.close()

    def excluirBd(self, idDaLinhaSelecionada):
        global objConexao

        try:
            dataBaseName = "Preferencias_3_09022024.accdb"
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            dataBasePath = os.path.join(projectDirectory, dataBaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + dataBasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()
            strSql = f"DELETE FROM Preferencias_3 WHERE ID =?"

            objLeitorBd.execute(strSql, idDaLinhaSelecionada)

            objConexao.commit()

            return True

        except Exception as erro:
            return erro
        finally:
            objConexao.close()

    def alterarBd(self, descricao, idDaLinhaSelecionada):
        global objConexao

        try:
            dataBaseName = "Preferencias_3_09022024.accdb"
            projectDirectory = os.path.dirname(os.path.abspath(__file__))
            dataBasePath = os.path.join(projectDirectory, dataBaseName)

            connectionString = (
                    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + dataBasePath + ';'
            )

            objConexao = pyodbc.connect(connectionString)
            objLeitorBd = objConexao.cursor()
            strSql = f"UPDATE Preferencias_3 SET Descricao =? WHERE ID =?"

            objLeitorBd.execute(strSql, descricao, idDaLinhaSelecionada)

            objConexao.commit()

            return True

        except Exception as erro:
            return erro
        finally:
            objConexao.close()
