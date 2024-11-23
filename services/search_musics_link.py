from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import logging

class SearchMusicsLink:

    def search(self, searchText):
        
        # Desabilitar logs do Selenium
        logging.getLogger('selenium').setLevel(logging.ERROR)

        # Configurar o Chrome para rodar em modo headless
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # Necessário em alguns ambientes
        chrome_options.add_argument("--disable-dev-shm-usage")  # Necessário em alguns ambientes
        chrome_options.add_argument("--disable-gpu")  # Desabilitar GPU, se necessário
        chrome_options.add_argument("--log-level=3")  # Suprime logs informativos

        # Iniciar o driver com as opções headless
        driver = webdriver.Chrome(options=chrome_options)

        #searchText = 'noites traiçoeiras'
        # Acesse a página
        searchLink = 'https://www.letras.mus.br/?q='+searchText
        print(searchLink)
        driver.get(searchLink)

        # Aguarde o carregamento da div (opcional)
        driver.implicitly_wait(10)

        # Encontre a div com a classe cse-search-results
        div = driver.find_element(By.CLASS_NAME, 'gsc-expansionArea')

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

        # Feche o navegador
        driver.quit()

        return links_list
