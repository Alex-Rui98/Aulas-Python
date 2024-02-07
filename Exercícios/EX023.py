#EX023

num_util= int(input("Introduza um número, e saiba a sua tabuada: "))

f=0

for f in range (0,10):
    if(f<11):
        tab=num_util * (f+1)
        print(num_util,"x",f+1,"=",tab)