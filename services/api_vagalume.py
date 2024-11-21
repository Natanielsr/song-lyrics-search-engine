import requests
from bs4 import BeautifulSoup

# Termo de pesquisa
termo_de_pesquisa = "eu seguirei"
url = f"https://www.vagalume.com.br/search?q={termo_de_pesquisa.replace(' ', '+')}"

# Faz a requisição para o site do Vagalume
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Faz o parsing do HTML com o BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra a seção de resultados de músicas
    resultados = soup.find_all('a', class_='gs-title')

    if resultados:
        print(f"Resultados da pesquisa para '{termo_de_pesquisa}':\n")
        # Itera sobre os resultados e imprime o título da música e o link
        for i, musica in enumerate(resultados, 1):
            titulo = musica.text.strip()
            link = "https://www.vagalume.com.br" + musica['href']
            print(f"{i}. {titulo}\n   Link: {link}")
    else:
        print("Nenhum resultado encontrado.")
else:
    print(f"Erro na requisição: Status {response.status_code}")
