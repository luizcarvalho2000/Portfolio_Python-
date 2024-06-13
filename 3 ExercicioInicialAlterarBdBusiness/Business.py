import os
import pyodbc
import pandas as pdPreferencias

class Preferencias():
    def impTxtWhile(self):

        try:
            lista = []

            arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
            strLinhaLida = arqPreferencias.readline()

            while strLinhaLida != "":
                lista.append(strLinhaLida)
                strLinhaLida = arqPreferencias.readline()
            arqPreferencias.close()

            return lista
        except Exception as e:
            return e

    def impTxtFor(self):
        try:
            lista = []

            arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
            arrStrLinhaLida = arqPreferencias.readlines()
            arqPreferencias.close()

            for item in range(len(arrStrLinhaLida)):
                item = arrStrLinhaLida[item]
                lista.append(item)

            return lista

        except Exception as e:
            return e

    def impTxtForEach(self):

        try:
            lista = []

            with open("Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:

                for item in arqPreferencias:
                    lista.append(item)
                arqPreferencias.close()

                return lista

        except Exception as e:
            return e

    def impBdConect(self):

        try:
            lista = []

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

            registro = objLeitorBd.fetchone()

            while registro != None:
                lista.append(registro.Descricao)
                registro = objLeitorBd.fetchone()

            objLeitorBd.close()
            objConexao.close()

            return lista


        except Exception as e:
            return e

    def impBdDesconect(self):
        try:
            lista = []

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
                lista.append(linha.Descricao)
            return lista

        except Exception as e:
            return e

    def consultBd(self, parPreferenciasDescricao=None):
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
            return e

    def inserirBd(self, descricao):
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

            strSQL = "INSERT INTO Preferencias_3 (Descricao) VALUES (?)"

            objLeitorBd.execute(strSQL, descricao)

            objConexao.commit()

            return True

        except Exception as e:
            return e

        finally:
            objConexao.close()


    def excluirBd(self, idItemDaLinhaSelecionada):
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

            strSQL = f"DELETE FROM Preferencias_3 WHERE ID = ?;"

            objLeitorBd.execute(strSQL, idItemDaLinhaSelecionada)

            objConexao.commit()

            return True

        except Exception as e:
            return e

        finally:
            objConexao.close()



    def alterarBd(self, descricao, idItemDaLinhaSelecionada):
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

            strSQL = f"UPDATE Preferencias_3 SET Descricao = ? WHERE ID = ?;"

            objLeitorBd.execute(strSQL, (descricao, idItemDaLinhaSelecionada))

            objConexao.commit()
            return True

        except Exception as e:
            return e

        finally:
            objConexao.close()
