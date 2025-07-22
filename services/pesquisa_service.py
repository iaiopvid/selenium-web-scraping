from core.enums import Resultado
from web.navegador import Navegador
from repository.pesquisa_repo import PesquisaRepository

class PesquisaService:
    def __init__(self, filtro: int = 0):
        self.filtro = filtro
        self.repo = PesquisaRepository()
        self.nav = Navegador()

    def processar(self):
        pesquisas = self.repo.buscar_em_aberto(self.filtro)
        for pesquisa in pesquisas:
            valor = pesquisa.get_documento_por_filtro(self.filtro)
            site = self.nav.buscar_site(valor, self.filtro)
            resultado = Resultado.definir(site)
            self.repo.registrar_resultado(pesquisa.id, resultado, self.filtro)