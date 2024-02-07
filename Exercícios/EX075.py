class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

        print(f"O livro com o título {self.titulo} foi escrito pelo autor {self.autor}")


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Apocalipse Nau", "Rui Zink")
livro3 = Livro("O Processo", "Franz Kafka")

