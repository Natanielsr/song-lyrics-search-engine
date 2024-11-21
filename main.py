import tkinter as tk
from gui.add_music_GUI import AddMusicGUI
from utils.txt_file import TXTFile
from gui.window_params import WindowParams
from tkinter import messagebox
import global_vars
from services.music_letter import MusicLetter

class MusicListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Músicas")
        WindowParams.set_defaults(self.master, 600, 400)

        add_music = AddMusicGUI(self.master)
        # Cria um botão que usa lambda para passar o valor do Entry
        botao = tk.Button(self.master, text="Adicionar Música", command=add_music.open_new_window)
        botao.pack(pady=20)

        # Cria uma Listbox para exibir as músicas
        self.listbox = tk.Listbox(master, width=100)
        self.listbox.pack(pady=10)

        # Criar um botão para excluir o item selecionado
        btn_excluir = tk.Button(self.master, text="Excluir Item", command=self.excluir_item)
        btn_excluir.pack()

        generate_button = tk.Button(self.master, text="Gerar", command=self.generate_letters)
        generate_button.pack(pady=20)

        # Bind do evento de foco na janela
        self.master.bind("<FocusIn>", self.update_list)

        # Inicializa a lista
        self.update_list()

    def update_list(self, event=None):
        # Limpa a Listbox
        self.listbox.delete(0, tk.END)

        # Adiciona as músicas da lista global à Listbox
        for music in global_vars.music_data:
            self.listbox.insert(tk.END, music[0])

    def excluir_item(self):
        # Obter o índice do item selecionado
        selecionado = self.listbox.curselection()
        if selecionado:  # Verifica se há um item selecionado
            indice = selecionado[0] # Pega o índice da seleção
            global_vars.music_data.pop(indice)
            self.listbox.delete(selecionado)  # Exclui o item pelo índice

    def generate_letters(self):

        txt = TXTFile()
        txt.apagar_txt_da_pasta()

        files_names = ''
        i = 1
        for name, link in global_vars.music_data:
            file_name = f'{i} - {name}'

            lyrics_text = self.generate_letter(link)
            txt.save(file_name,lyrics_text)

            files_names += f'{file_name}.txt, '
            i += 1

        messagebox.showinfo("Salvo", f"Arquivos Salvos em /musics \n {files_names}")

    def generate_letter(self, url):
        ml = MusicLetter(url)
        lyrics_text = ml.find()

        return lyrics_text

def main():
    root = tk.Tk()
    app = MusicListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()