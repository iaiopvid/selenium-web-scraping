from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time
from core.config import EXECUTAVEL

class Navegador:
    def __init__(self):
        service = Service(executable_path=EXECUTAVEL+"msedgedriver.exe")
        options = Options()
        options.add_argument("-headless")
        options.add_argument("--disable-gpu")
        # self.driver = webdriver.Edge(options=options)
        self.driver = webdriver.Edge(service=service, options=options)

    def buscar_site(self, valor: str, filtro: int) -> str:
        self.driver.get("https://esaj.tjsp.jus.br/cpopg/open.do")
        try:
            select = Select(self.driver.find_element('xpath', '//*[@id="cbPesquisa"]'))
            if filtro in (0, 1, 3):
                select.select_by_value('DOCPARTE')
                self.driver.find_element('xpath', '//*[@id="campo_DOCPARTE"]').send_keys(valor)
            elif filtro == 2:
                select.select_by_value('NMPARTE')
                self.driver.find_element('xpath', '//*[@id="pesquisarPorNomeCompleto"]').click()
                self.driver.find_element('xpath', '//*[@id="campo_NMPARTE"]').send_keys(valor)
            self.driver.find_element('xpath', '//*[@id="botaoConsultarProcessos"]').click()
            return self.driver.page_source
        except Exception as e:
            print(f"Erro Selenium: {e}")
            time.sleep(5)
            return ""