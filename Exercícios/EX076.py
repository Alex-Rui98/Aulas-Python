class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

        print(f"O produto {self.nome} tem {self.quantidade} em stock.")