#EX014

velo=int(input("Introduza a velocidade registada em km/h:"))

if(velo<=80):
    print("Obrigado por ser um condutor seguro")
else:
    print("Irá ser multado em", 100 + 7*(velo-80), "€")
