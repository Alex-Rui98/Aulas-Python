#EX019

import random

import time

print("Bem Vindo ao jogo da adivinha!")

num_util=int(input("Introduza um número de 0 a 7, e eu direi se estou a pensar nesse número: "))

time.sleep(1)

confirm= input("Tem a certeza que quer escolher este número? (Y/N)").strip()

if (confirm=="N"):
    print("Azar, vamos com este número na mesma!")
    time.sleep(1)
elif (confirm=="Y"):
    print("Ótimo, gosto de confiança!")
    time.sleep(1)
else:
    print("Uhhhhhhh...")
    time.sleep(3)
    print("O que queres que isso queira dizer, mas vamos lá!")
    time.sleep(1)
num_cpu=random.randrange(0,7)

print(f"O número que você inseriu foi {num_util}")
time.sleep(1)
print(f"O número que eu pensei foi o {num_cpu}")
time.sleep(1)

if (num_util==num_cpu):
    print("Parabéns, tem um cérebro de máquina ;)")
elif (num_util!=num_cpu):
    print("Oh não, melhor sorte para a próxima!")