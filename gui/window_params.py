class WindowParams:

    @staticmethod
    def set_defaults(window, width = 400, heigth = 300):

        # Obtém as dimensões da tela
        largura_tela = window.winfo_screenwidth()
        altura_tela = window.winfo_screenheight()

        # Calcula a posição central
        x = (largura_tela // 2) - (width // 2)
        y = (altura_tela // 2) - (heigth // 2)

        # Define a geometria da nova janela (largura x altura + posição x + posição y)
        window.geometry(f"{width}x{heigth}+{x}+{y}")