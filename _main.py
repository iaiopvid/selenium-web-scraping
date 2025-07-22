from services.pesquisa_service import PesquisaService

def executar_por_filtros():
    for filtro in range(4):
        print(f"\n🔄 Executando filtro {filtro}...")
        service = PesquisaService(filtro)
        service.processar()

if __name__ == "__main__":
    executar_por_filtros()
