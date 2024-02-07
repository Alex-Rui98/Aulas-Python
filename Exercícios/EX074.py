class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Apocalipse Nau", "Rui Zink")
livro3 = Livro("O Processo", "Franz Kafka")

print(livro1.titulo, livro1.autor)
print(livro2.titulo, livro2.autor)
print(livro3.titulo, livro3.autor)