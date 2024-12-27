import tkinter as tk
from tkinter import messagebox
from services.search_musics_link import SearchMusicsLink
from gui.window_params import WindowParams
import global_vars
import time
class AddMusicGUI:
    def __init__(self, master, search_musics_link : SearchMusicsLink):
        self.master = master
        self.search_musics_link = search_musics_link

    def add_music(self, music):
        global_vars.music_data.append((music[0], music[1]))
        messagebox.showinfo("Música adicionada", f"Nome: {music[0]}")
        self.janela.destroy()

    def search_musics(self, texto):
        # Limpa os botões existentes
        for widget in self.frame_botoes.winfo_children():
            widget.destroy()

        result = self.search_musics_link.search(texto)
        
        start = time.time()

        buttons = []
        for name, link in result:
            button = tk.Button(self.frame_botoes, text=f'[+] {name}', command=lambda name=name, link=link: self.add_music([name, link]))
            buttons.append(button)

        # Adicione os botões em lote
        for button in buttons:
            button.pack(pady=5)

        end = time.time()
        execution_time_ms = (end - start) * 1000  # Converter para milissegundos
        print(f"Tempo gráficos: {execution_time_ms:.3f} ms")

    def open_new_window(self):
        # Cria a nova janela
        self.janela = tk.Toplevel(self.master)
        self.janela.title("Buscar Música")

        WindowParams.set_defaults(self.janela)

        # Cria um textbox de entrada (Entry)
        self.entrada = tk.Entry(self.janela, width=60)
        self.entrada.pack(pady=5)

        # Cria um botão que usa lambda para passar o valor do Entry
        botao = tk.Button(self.janela, text="Pesquisar", command=lambda: self.search_musics(self.entrada.get()))
        botao.pack(pady=10)

        # Cria um frame para os novos botões
        self.frame_botoes = tk.Frame(self.janela)
        self.frame_botoes.pack(pady=10)

        