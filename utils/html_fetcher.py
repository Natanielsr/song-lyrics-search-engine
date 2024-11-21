import requests
from bs4 import BeautifulSoup

class HtmlFetcher:
    def __init__(self, url):
        self.url = url
        self.html_content = None
        self.soup = None

    def fetch(self):
        """Busca a página HTML e armazena o conteúdo."""
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.html_content = response.text
                self.soup = BeautifulSoup(self.html_content, 'html.parser')
                print(f"Página '{self.url}' carregada com sucesso.")
            else:
                print(f"Erro ao buscar a página: {response.status_code}")
        except Exception as e:
            print(f"Ocorreu um erro ao buscar a página: {e}")

    def get_title(self):
        """Retorna o título da página."""
        if self.soup:
            return self.soup.title.string if self.soup.title else "Título não encontrado"
        return "HTML não foi carregado"

    def find_by_tag(self, tag):
        """Retorna todos os elementos de uma determinada tag."""
        if self.soup:
            return self.soup.find_all(tag)
        return "HTML não foi carregado"

    def find_by_id(self, element_id):
        """Encontra um elemento específico pelo ID."""
        if self.soup:
            return self.soup.find(id=element_id)
        return "HTML não foi carregado"
        
    def find_by_class(self, class_name):
        """Encontra elementos por classe CSS."""
        if self.soup:
            return self.soup.find_all(class_=class_name)
        return "HTML não foi carregado"