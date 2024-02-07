# EX027

idade = []

for c in range(0, 10):
    if (c < 10):
        idade.append(int(input(f'Coloque a idade da {c + 1}ª pessoa: ')))

print(f'A maior idade lida foi {max(idade)}.')

print(f'A menor idade lida foi {min(idade)}.')

# OU PODES FAZER ASSIM

maior = 0
menor = 0

for pessoa in range(0, 10):
    idad = int(input(f"{pessoa + 1} - Digite a sua idade:"))
    if pessoa == 0:
        maior = idad
        menor = idad
    else:
        if idade > maior:
            maior = idad
        elif idad < menor:
            menor = idad

print(f"A maior idade encontrada foi a {maior}")
print(f"A menor idade encontrada foi a {menor}")