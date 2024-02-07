#EX024

num= int(input("Introduza um número, e saiba se é primo:"))

tot = 0

for c in range (1, num+1):
    if num % c == 0:
        tot += 1 #isto quer dizer tot= tot+1

if tot==2:
    print(f'O número {num} é PRIMO, foi divísivel {tot} vezes.')
else:
    print(f'O número {num} NÃO É PRIMO, foi divisível {tot} vezes.')