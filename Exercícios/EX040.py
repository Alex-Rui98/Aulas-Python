from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os números selecionados foram: {tupla}")
maior = menor = tupla[0]

for num in tupla:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"O maior número gerado foi o: {maior}")
print(f"O menor número gerado foi o: {menor}")