import pyodbc
from io import StringIO

class Conexao:
    _conexao = None
    _pathBD = None

    def __init__(self):
        Conexao.getConexao()

    @staticmethod
    def getConexao():
        if Conexao._conexao is None:
            Conexao.setConexao()

        return Conexao._conexao

    @staticmethod
    def setConexao():
        try:
            with (open(".\\config.ini", "r") as arquivoIni):
                connectionString = StringIO()
                connectionString.write(arquivoIni.readline())
                connectionString.write(arquivoIni.readline())
                connectionString = connectionString.getvalue()

            lstConexao = connectionString.split('\n')
            tplConexao = (fr'{lstConexao[0]}' +
                            fr'{lstConexao[1]}')
            objConexao = pyodbc.connect(tplConexao)
            Conexao._conexao = objConexao
        except FileNotFoundError:
            raise Exception("Erro: Arquivo config.ini não encontrado.")

        except IOError as e:
            raise Exception(f"Erro ao ler o arquivo config.ini: {e}")

    @staticmethod
    def fecharConexao():
        if Conexao._conexao is not None:
            Conexao._conexao.close()
            Conexao._conexao = None

    @property
    def conexao(self):
        if Conexao._conexao is None:
            Conexao.setConexao()
        return Conexao._conexao

    def __enter__(self):
        return self.conexao

    def __exit__(self, exc_type, exc_val, exc_tb):
        Conexao.fecharConexao()
