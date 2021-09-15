
class Carro:
    def __init__(self, marca, velocidade_max=0, quilometragem=0):
        self.marca = marca
        self.quilometragem = quilometragem
        self.velocidade_max = velocidade_max

    def __str__(self):
        return f'Carro {self.marca}'

    def ligar(self):
        print(f'{self} ligado.')

    def acelerar(self):
        print(f'{self} acelerando...')
        print(f'{self} a {self.velocidade_max} km/h')

    def desligar(self):
        print(f'{self} desligando...')

carro1 = Carro('fusca', 99, 60000)
carro2 = Carro(quilometragem=500, marca='porsche')
carro3 = Carro('ford_ka')
carro3.velocidade_max = 150
carro3.ligar()
carro3.acelerar()
carro3.desligar()

carro1 = carro2
carro1 = carro1
carro2 = carro1
carro1 = carro2

print(f'1:{carro1}')
print(f'2:{carro2}')
print(f'3:{carro3}')
print(f'4:{carro4}')
