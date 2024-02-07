#EX029

import random

import time

print("Bem Vindo ao jogo da adivinha!")

num_util=int(input("Introduza um número de 0 a 10, e eu direi se estou a pensar nesse número: "))

time.sleep(1)

confirm=""

print("Tem a certeza que quer escolher este número? (Y/N)")
confirm=input("----->").strip().upper()
while confirm:
    if confirm=="N":
        print("Ok, pode escolher agora outro número.")
        confirm = input("----->").strip().upper()
        time.sleep(1)
    elif confirm=="Y":
        print("Ótimo, gosto de confiança!")
        time.sleep(1)
        break
    else:
        print("Uhhhhhhh...")
        time.sleep(3)
        print("Vamos lá, escolhe uma das opções... ")
        confirm = input("----->").strip().upper()
    time.sleep(1)
num_cpu=random.randrange(0,10)

while num_cpu:
    if (num_util==num_cpu):
        print("Parabéns, tem um cérebro de máquina ;)")
        break
    elif (num_util<num_cpu):
        print("Oh não, demasiado baixo, tente novamente.")
        num_util
    else:
        print("Oh não, demasiado alto, tente novamente.")
        num_util