class PreferenciasVO:
    def __init__(self, iD=None, descricao=None):
        # Validação de tipo com exceção
        if iD is not None:
            if not isinstance(iD, int):
                raise ValueError('ID inválido')
        if descricao is not None:
            if not isinstance(descricao, str):
                raise ValueError('Descrição inválida')

        self._id = iD
        self._descricao = descricao

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError('ID deve ser um inteiro')
        self._id = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        if not isinstance(value, str):
            raise ValueError('Descrição deve ser uma string')
        self._descricao = value
