class Pesquisa:
    def __init__(self, id, cpf=None, rg=None, nome=None):
        self.id = id
        self.cpf = cpf
        self.rg = rg
        self.nome = nome

    def get_documento_por_filtro(self, filtro):
        if filtro == 0:
            return self.cpf
        if filtro in (1, 3):
            return self.rg
        if filtro == 2:
            return self.nome
        return None