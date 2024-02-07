#EX008

print("Bem-Vindo ao Catch-a-ride!\n")

km_per= float(input("Introduza os kilometros percorridos pelo carro:\n""\n"))
dias_util= int(input("Introduza os número de dias que o carro foi utilizado:\n""\n"))

#variaveis de calculo

custo_dia= 60
custo_km= 0.456

preco= (km_per * custo_km) + (dias_util * custo_dia)

print("O preço total da utilização deste carro é:\n", preco)