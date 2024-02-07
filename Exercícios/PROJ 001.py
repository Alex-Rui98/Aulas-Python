#partes de outros para adicionar
livros = [
    {
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'isbn': '978-85-7164-316-6',
        'ano_publicacao': 1899,
        'editora': 'Garnier',
        'categoria': 'Romance',
        'genero': 'Ficção',
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'isbn': '978-0-452-28423-4',
        'ano_publicacao': 1949,
        'editora': 'Secker & Warburg',
        'categoria': 'Ficção Científica',
        'genero': 'Distopia',
    },
    {
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
        'isbn': '978-0-618-15263-4',
        'ano_publicacao': 1954,
        'editora': 'Allen & Unwin',
        'categoria': 'Fantasia',
        'genero': 'Aventura',
    }
]
emprestimo={"Disponiblidade":[]}
#PARTE RUI

#LISTAR TODOS OS LIVROS - simples amostra de todos os livros apresentados
i = 0

#listar= print((dicio), end="\n")

while i < len(livros):
    print(i+1, "-", livros[i]['titulo'], ":", livros[i]['autor'], livros[i]['isbn'], ",", livros[i]['ano_publicacao'], livros[i]['editora'], livros[i]['categoria'], livros[i]['genero'])
    i += 1
#adicionar
resp = input("ola").strip().upper()
add_book = {}
while resp == "Y":
    titu = input("Introduza o título do livro: ")
    autor = input("Introduza o autor do livro: ")
    isbn = input("Introduza o ISBN do livro: ")
    ano_pub = input("Introduza o ano de publicação do livro: ")
    editora = input("Introduza a editora do livro: ")
    cat = input("Introduza a categoria do livro: ")
    gen = input("Introduza o género do livro: ")
    add_book = {f"'titulo': '{titu}', 'autor': '{autor}', 'isbn': '{isbn}', 'ano': '{ano_pub}', 'editora': '{editora}', 'categoria': '{cat}', 'genero': '{gen}'"}

    livros.append(add_book)

    print("O livro foi adicionado com sucesso.")

    resp = input("continuar")


# Remover
print("Escolha o livro que pretende remover: ")
while i < len(livros):
    print(i+1, "-", livros[i]['titulo'], ":", livros[i]['autor'], livros[i]['isbn'], ",", livros[i]['ano_publicacao'], livros[i]['editora'], livros[i]['categoria'], livros[i]['genero'])
    i += 1
resp_num = int(input("Introduza aqui o número do livro--> "))
rem_book = livros.pop(resp_num-1)
print(livros)
