lista = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(0, 3):
    for c in range(0, 3):
        lista[i][c] = int(input(f"Introduza um número para {i}{c}: "))

for i in range(0, 3):
    for c in range(0, 3):
        print(f"[ {lista[i][c]} ]", end=" ")
    print()





