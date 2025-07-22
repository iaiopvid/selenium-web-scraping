# from services.pesquisa_service import PesquisaService

# def executar_por_filtros():
#     for filtro in range(4):
#         print(f"\n🔄 Executando filtro {filtro}...")
#         service = PesquisaService(filtro)
#         service.processar()

# if __name__ == "__main__":
#     executar_por_filtros()

import time
from services.pesquisa_service import PesquisaService

def rodar_em_loop():
    tentativas = 0
    while True:
        alguma_execucao = False
        for filtro in range(4):
            print(f"\n🔄 Executando filtro {filtro}...")
            service = PesquisaService(filtro)
            if service.processar():  # retorna True se executou algo
                alguma_execucao = True

        if alguma_execucao:
            tentativas = 0  # zera se teve trabalho
        else:
            tentativas += 1
            print("⏳ Nenhuma pesquisa. Aguardando...")
            time.sleep(60 if tentativas < 20 else 3600)

if __name__ == "__main__":
    rodar_em_loop()
