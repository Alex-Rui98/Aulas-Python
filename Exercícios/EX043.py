num_a = int(input("Introduza por favor o primeiro número: "))
num_b = int(input("Introduza por favor o segundo número: "))
num_c = int(input("Introduza por favor o terceiro número: "))
num_d = int(input("Introduza por favor o quarto número: "))
num_e = int(input("Introduza por favor o último número: "))

lista = [num_a, num_b, num_c, num_d, num_e]

maior = 0
menor = 0

for v in range(0,5):
    if lista[v] > maior:
        maior = lista[v]
    if menor == 0:
        menor = lista[0]
    if lista[v] < menor:
        menor = lista[v]

print(f"O maior número foi o {maior} que está na posição {lista.index(maior)+1}")
print(f"O menor número foi o {menor} que está na posição {lista.index(menor)+1}")
