lista = [[], [], []], [[], [], []], [[], [], []]
pares = 0
soma2 = 0
maior = 0
for i in range(0, 3):
    for c in range(0, 3):
        lista[i][c] = int(input(f"Introduza um número para {i}{c}: "))
        num = lista[i][c]
        if num % 2 == 0:
            pares += num
        if c == 1:
            soma2 += num
        if i == 2:
            if num > maior:
                maior = num


for i in range(0, 3):
    for c in range(0, 3):
        print(f"[ {lista[i][c]} ]", end=" ")
    print()
print(pares, soma2, maior)