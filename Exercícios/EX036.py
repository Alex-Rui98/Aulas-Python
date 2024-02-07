from random import randrange

print("Bem vindo ao par-impar!")

cont = 0

num = input("Por favor escolha se o numero sera par ou impar [P/I]: ")
cpu_num = randrange(1, 10) % 2
while num == "P":
    if cpu_num == 0:
        print("Parabens")
        cont += 1
        cpu_num = randrange(1, 10) % 2
    elif cpu_num != 0:
        print(f"Oh nao, perdeu, num total de {cont}")
        break

while num == "I":
    if cpu_num != 0:
        print("Parabe")
        cont += 1
        cpu_num = randrange(1, 10) % 2
    elif cpu_num == 0:
        print(f"Oh nao, perdeu, num total de {cont}")
        break
    else:
        print("Resposta invalida, tente de novo")