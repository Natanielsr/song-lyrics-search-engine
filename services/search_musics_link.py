from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging
import time

class SearchMusicsLink:

    def __init__(self):
        start = time.time()
        print(f"Starting Driver...")
        # Desabilitar logs do Selenium
        logging.getLogger('selenium').setLevel(logging.ERROR)

        # Configurar o Chrome para rodar em modo headless
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # Necessário em alguns ambientes
        chrome_options.add_argument("--disable-dev-shm-usage")  # Necessário em alguns ambientes
        chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU, se necessário
        chrome_options.add_argument("--log-level=3")  # Suprime logs informativos

        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")

        # Iniciar o driver com as opções headless
        self.driver = webdriver.Chrome(options=chrome_options)

        end = time.time()
        execution_time_ms = (end - start) * 1000  # Converter para milissegundos
        print(f"Driver started at : {execution_time_ms:.3f} ms")

        start = time.time()

    def search(self, searchText):
        start = time.time()

        # Acesse a página
        searchLink = 'https://www.letras.mus.br/?q='+searchText
        print(searchLink)
       
        self.driver.get(searchLink)

        # Aguarde o carregamento da div (opcional)
        self.driver.implicitly_wait(1)

        end = time.time()
        execution_time_ms = (end - start) * 1000  # Converter para milissegundos
        print(f"Tempo de busca: {execution_time_ms:.3f} ms")

        start = time.time()

        # Encontre a div com a classe cse-search-results
        div = self.driver.find_element(By.CLASS_NAME, 'gsc-expansionArea')

        # Encontrar o primeiro link
        links = div.find_elements(By.TAG_NAME, "a")

        links_list= []
        # Processar todos os links encontrados
        for link in links:
            # Imprimir texto e URL de cada link
            if(link.text != ''):
                link_name = str(link.text)
                new_link_name = link_name[:-16]  # Remove os últimos 16 caracteres
                tuple = (new_link_name, str(link.get_attribute("href")))
                links_list.append(tuple)

        end = time.time()
        execution_time_ms = (end - start) * 1000  # Converter para milissegundos
        print(f"Tempo de conversão: {execution_time_ms:.3f} ms")

        start = time.time()

        #self.driver.close()
        # Feche o navegador
        #driver.quit()

        end = time.time()
        execution_time_ms = (end - start) * 1000  # Converter para milissegundos
        print(f"Tempo para fechar: {execution_time_ms:.3f} ms")

        
        return links_list
