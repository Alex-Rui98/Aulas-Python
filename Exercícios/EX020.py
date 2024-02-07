#EX020

import random

import time

print("Bem-Vindo ao jogo do pedra, papel, tesoura!\n\n")

time.sleep (2)

print("Escolha por favor a sua jogada, introduzindo o número da jogada:\n\n")

print("(1) Pedra \n(2) Papel \n(3) Tesoura \n")

num= int(input("Número: "))

time.sleep(1)

cpu= random.randrange (1,3)

bat= num-cpu

print("Pedra...")

time.sleep(1)

print ("Papel...")

time.sleep(1)

print ("TESOURA!")

if (bat==0):
    print ("Empate.")
elif (bat==1 or bat==-2):
    print ("Vitória!")
elif (bat==2 or bat== -1):
    print ("Derrota!")