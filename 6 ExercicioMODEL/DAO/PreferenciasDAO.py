import pandas as pdPreferencias
from io import StringIO
from DAO.DB_DAO import Conexao
from MODEL.PreferenciasVO import PreferenciasVO


class PreferenciasDAO(Conexao):
    def __init__(self):
        super().__init__()

        self.preferenciasVO = PreferenciasVO()

    def impBdConect(self):

        try:
            lista = []

            objConexao = self.conexao
            objLeitorBd = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" Descricao")
            strSQL.write(" FROM")
            strSQL.write(" Preferencias_3")
            strSQL.write(" ORDER BY ID")

            objLeitorBd.execute(strSQL.getvalue())

            registro = objLeitorBd.fetchone()

            while registro is not None:
                lista.append(registro.Descricao)
                registro = objLeitorBd.fetchone()

            objLeitorBd.close()
            return lista

        except Exception as erro:
            raise Exception(erro)
        finally:
            self.fecharConexao()

    def impBdDesconect(self):

        try:
            lista = []

            objConexao = self.conexao
            objLeitorBd = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" Descricao")
            strSQL.write(" FROM")
            strSQL.write(" Preferencias_3")
            strSQL.write(" ORDER BY ID")

            objLeitorBd.execute(strSQL.getvalue())

            registro = objLeitorBd.fetchall()

            dfPreferencias = pdPreferencias.DataFrame(registro, columns=["Descricao"])

            objLeitorBd.close()

            for linha in dfPreferencias["Descricao"]:
                lista.append(linha.Descricao)
            return lista

        except Exception as erro:
            raise Exception(erro)
        finally:
            self.fecharConexao()

    def consultarBd(self, objPreferenciasVO):

        try:
            objConexao = self.conexao
            objLeitorBd = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("SELECT")
            strSQL.write(" ID,")
            strSQL.write(" Descricao")
            strSQL.write(" FROM")
            strSQL.write(" Preferencias_3")

            if objPreferenciasVO.descricao is None or objPreferenciasVO.descricao == "":
                strSQL.write(" ORDER BY ID")
                objLeitorBd.execute(strSQL.getvalue())
            else:
                strSQL.write(" WHERE")
                strSQL.write(" Descricao = ?")
                strSQL.write(" ORDER BY ID")
                objLeitorBd.execute(strSQL.getvalue(), objPreferenciasVO.descricao)

            registro = objLeitorBd.fetchall()

            return registro

        except Exception as erro:
            raise Exception(erro)
        finally:
            self.fecharConexao()

    def inserirBd(self, objPreferenciasVO):
        try:
            objConexao = self.conexao
            objLeitorBd = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("INSERT INTO")
            strSQL.write(" Preferencias_3 (")
            strSQL.write(" Descricao")
            strSQL.write(" ) VALUES (")
            strSQL.write(" ?")
            strSQL.write(" )")

            objLeitorBd.execute(strSQL.getvalue(), objPreferenciasVO.descricao)

            objConexao.commit()

            return True

        except Exception as erro:
            raise Exception(erro)
        finally:
            self.fecharConexao()

    def excluirBd(self, objPreferenciasVO):

        try:
            objConexao = self.conexao
            objLeitorBd = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("DELETE")
            strSQL.write(" FROM")
            strSQL.write(" Preferencias_3")
            strSQL.write(" WHERE")
            strSQL.write(" ID = ?")

            objLeitorBd.execute(strSQL.getvalue(), objPreferenciasVO.id)

            objConexao.commit()

            return True

        except Exception as erro:
            raise Exception(erro)
        finally:
            self.fecharConexao()

    def alterarBd(self, objPreferenciasVO):

        try:
            objConexao = self.conexao
            objLeitorBd = objConexao.cursor()

            strSQL = StringIO()
            strSQL.write("UPDATE")
            strSQL.write(" Preferencias_3")
            strSQL.write(" SET")
            strSQL.write(" Descricao =?")
            strSQL.write(" WHERE")
            strSQL.write(" ID =?")

            objLeitorBd.execute(strSQL.getvalue(), objPreferenciasVO.descricao, objPreferenciasVO.id)

            objConexao.commit()

            return True

        except Exception as erro:
            raise Exception(erro)
        finally:
            self.fecharConexao()
