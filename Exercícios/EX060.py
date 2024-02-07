def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} a {passo}")
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f"{cont}", end=" ")
            cont += passo
        print("Fim!")
    else:
        while cont >= fim:
            print(f"{cont}", end=" ")
            cont -= passo
        print("Fim!")


contador(1, 20, 2)
contador(10, 0, 1)

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

contador(i, f, p)