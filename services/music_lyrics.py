from utils.html_fetcher import HtmlFetcher
from bs4 import BeautifulSoup

class MusicLyrics:
    
    def __init__(self, url):
        self.url = url

    def find(self):
        paragraphs = self.get_paragraphs()
        lyrics_text = ''
        if len(paragraphs) > 0:
            lyrics_text = self.extract_text(str(paragraphs[0]))

        return lyrics_text

    def get_paragraphs(self):
        fetcher = HtmlFetcher(self.url)
        fetcher.fetch()  # Faz a requisição e carrega o HTML

        # Obter o título da página
        print(fetcher.get_title())

        paragraphs = fetcher.find_by_class('lyric-original')

        return paragraphs
    
    def extract_text(self, paragraphs):
        # Usando o BeautifulSoup para processar o HTML
        soup = BeautifulSoup(paragraphs, 'html.parser')
        # Encontrar o conteúdo da div com a classe 'lyric-original'
        lyric_div = soup.find('div', class_='lyric-original')

        # Extrair todo o texto de dentro dos parágrafos <p>
        lyrics_text = ''
        if lyric_div:
            for p in lyric_div.find_all('p'):
                lyrics_text += p.get_text(separator='\n') + '\n\n'  # Separar quebras de linha dentro dos parágrafos e adicionar espaçamento entre eles

        return lyrics_text.strip() # Remover espaços e quebras de linha extras no início e no final