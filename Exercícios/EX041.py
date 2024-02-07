a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
d = int(input("Digite um último número: "))

tupla = (a, b, c, d)

cont_7 = 0
for num in tupla:
    if num == 7:
        cont_7+=1

if cont_7 == 0:
    print("O número 7 não aparece nenhuma vez.")
else:
    print(f"O número 7 apareceu {cont_7} vezes.")

cont_5 = 0
for num in tupla:
    if num == 5:
        cont_5+=1

if cont_5 == 0:
    print("O número 5 não aparece nenhuma vez.")
else:
    print(f"O número 5 apareceu {cont_5} vezes.")

controlo_pares = 0
for num in tupla:
    if num % 2 == 0:
        if num == tupla[0]:
            print("Os números pares são: ", end=" -> ")
        print(num, end=" -> ")
    else:
        controlo_pares += 1

    if controlo_pares == 4:
        print("Não há números pares disponíveis.")