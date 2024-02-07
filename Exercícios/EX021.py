#EX021

import time

dez=10

for contagem in range(0,11):
    if (dez>0):
        print(dez)
        time.sleep(1)
        dez = dez - 1
    elif (dez==0):
        print("Feliz Ano Novo!")