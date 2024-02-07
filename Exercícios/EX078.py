class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14159

    def get_raio(self):
        return self.__raio

    def set_raio(self, raio):
        self.__raio = raio
        print(raio)

    def set_area(self, raio):
        area = self.__pi * (raio * raio)
        print(f'A área definida pelo raio é {area}')

    def set_per(self, radius):
        per = self.__pi * 2 * radius
        print(f'O perímetro do círculo definido pelo raio é {per}')



raio = 5

circ = Circulo(raio)
circ.set_raio(raio)
circ.set_area(raio)
circ.set_per(raio)

raio = int(input("Introduza aqui o novo raio:"))


circ.set_raio(raio)
circ.set_area(raio)
circ.set_per(raio)
