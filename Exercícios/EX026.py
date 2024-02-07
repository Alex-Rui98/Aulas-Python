#EX026

from datetime import date

nasc= input("Introduza as datas de nascimento, separadas por espaços:").strip()

datasS= nasc.split(" ")

ano_atual= int(date.today().year)

contagem= len(datasS)

tot_maior=0

tot_menor=0

tot_imp=0

for pessoa in range (0,contagem):
    if(ano_atual-int(datasS[pessoa])>=18):
        tot_maior+=1
    elif(0<=ano_atual-int(datasS[pessoa])<18):
        tot_menor+=1
    else:
        tot_imp+=1

print(f'Ao todo tivemos {tot_maior} pessoas maiores de idade.')
print(f'Ao todo tivemos {tot_menor} pessoas menores de idade.')
print(f'Acreditamos que errou na introdução de {tot_imp} valores.')