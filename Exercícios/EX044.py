lista = list()
opt = "Y"
while opt == "Y":
    num = input("Introduza um número:")
    if num in lista:
        print("Este número já foi introduzido.")
    else:
        lista.append(num)
        print(f"O número {num} foi introduzido.")

    opt = input("Pretende continuar [Y/N]?")
    if opt == "N":
        lisort = lista.sort(reverse=True)
        print(lisort)
        print(lista)
        break