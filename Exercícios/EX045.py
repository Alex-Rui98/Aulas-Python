lista = []

for c in range(0, 5):
    novo_num = int(input(f"Digite um número: "))
    if c == 0 or novo_num > lista[-1]:
        lista.append(novo_num)
        print(f"O número {novo_num} foi adicionado na última posição.")
    else:
        ind = 0
        while ind < len(lista):
            if novo_num <= lista[ind]:
                lista.insert(ind, novo_num)
                print(f"Novo número adicionado na posição {ind + 1}.")
                break
            ind += 1

print(lista)
