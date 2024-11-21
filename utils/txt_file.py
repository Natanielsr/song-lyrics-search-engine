import os 
import re

class TXTFile:

    def __init__(self):
        self.path = 'musics/'


    def save(self, file_name, lyrics_text):
        # Salvar o texto em um arquivo .txt
        file_path = f'{self.path}{self.sanitize_filename(file_name)}.txt'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(lyrics_text)

        print(f"Arquivo {file_path} gerado com sucesso!")

    def apagar_txt_da_pasta(self):
        for arquivo in os.listdir(self.path):
            caminho_completo = os.path.join(self.path, arquivo)
            if arquivo.endswith('.txt') and os.path.isfile(caminho_completo):
                os.remove(caminho_completo)
                print(f'{arquivo} foi removido.')

    def sanitize_filename(self, file_name):
        # Remove ou substitui caracteres inválidos no nome do arquivo
        return re.sub(r'[<>:"/\\|?*]', '_', file_name)