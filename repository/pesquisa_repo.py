# class Pesquisa:
#     def __init__(self, id, cpf, rg, nome):
#         self.id = id
#         self.cpf = cpf
#         self.rg = rg
#         self.nome = nome

#     def get_documento_por_filtro(self, filtro):
#         if filtro == 0:
#             return self.cpf
#         if filtro in (1, 3):
#             return self.rg
#         if filtro == 2:
#             return self.nome
#         return None

# class PesquisaRepository:
#     def buscar_em_aberto(self, filtro):
#         return [Pesquisa(1, "12345678901", "1234567", "João Silva")]

#     def registrar_resultado(self, cod_pesquisa, resultado, filtro):
#         print(f"Resultado {resultado} registrado para pesquisa {cod_pesquisa} com filtro {filtro}")

from core.database import Database
from domain.pesquisa import Pesquisa

class PesquisaRepository:
    def __init__(self):
        self.db = Database()

    def buscar_em_aberto(self, filtro):
        query = """
            SELECT p.cod_pesquisa, p.cpf, p.rg, COALESCE(p.nome_corrigido, p.nome)
            FROM pesquisa p
            LEFT JOIN pesquisa_spv r ON r.cod_pesquisa = p.cod_pesquisa AND r.filtro = ?
            WHERE p.data_conclusao IS NULL
              AND r.resultado IS NULL
              AND p.tipo = 0
              AND p.cpf != ""
            LIMIT 100
        """
        self.db.execute(query, (filtro,))
        resultados = self.db.fetchall()
        return [Pesquisa(*row) for row in resultados]

    def registrar_resultado(self, cod_pesquisa, resultado, filtro):
        query = """
            INSERT INTO pesquisa_spv (
                cod_pesquisa, resultado, cod_funcionario,
                filtro, website_id, cod_spv_computador
            ) VALUES (?, ?, -1, ?, 1, 36)
        """
        self.db.execute(query, (cod_pesquisa, resultado, filtro))
        
    # Se Postgres substituir os placeholders '?' por '%s'.
