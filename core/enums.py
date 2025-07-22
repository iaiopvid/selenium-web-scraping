class Resultado:
    @staticmethod
    def definir(site_html: str) -> int:
        if "Não existem informações disponíveis para os parâmetros informados." in site_html:
            return 1
        if "Processos encontrados" in site_html or "Audiências" in site_html:
            if 'criminal' in site_html.lower():
                return 2
            return 5
        return 7