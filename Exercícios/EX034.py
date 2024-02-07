"""nota = float(input("Por favor introduza uma nota (Insira -1 para obter a média): "))
cont = 0
soma = 0
maior = menor = 0
media = 0
while nota != -1:
    if cont == 0:
        maior = menor = nota
    cont += 1
    soma += nota
    nota = float(input("Por favor introduza uma nota (Insira -1 para obter a média): "))
    if nota < menor:
        menor = nota
    elif nota > maior:
            maior = nota
    elif nota == -1:
            break

media = soma/cont

print(f"Das {cont} notas introduzidas, a média apresentada é de {media}, sendo {maior} a nota mais alta e {menor} a nota mais baixa.")"""

nota = float(input("Por favor introduza uma nota (Insira -1 para obter a média): "))
cont = 0
soma = 0
maior = menor = None

while nota != -1:
    if cont == 0 or nota < menor:
        menor = nota
    if cont == 0 or nota > maior:
        maior = nota

    cont += 1
    soma += nota
    nota = float(input("Por favor introduza uma nota (Insira -1 para obter a média): "))

if cont > 0:
    media = soma / cont
    print(f"Das {cont} notas introduzidas, a média apresentada é de {media}, sendo {maior} a nota mais alta e {menor} a nota mais baixa.")
else:
    print("Nenhuma nota foi introduzida.")