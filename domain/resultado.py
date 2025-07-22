from core.config import NADA_CONSTA, CONSTA01, CONSTA02

class Resultado:
    @staticmethod
    def definir(site_html: str) -> int:
        if NADA_CONSTA in site_html:
            return 1
        if CONSTA01 in site_html or CONSTA02 in site_html:
            if 'criminal' in site_html.lower():
                return 2
            return 5
        return 7