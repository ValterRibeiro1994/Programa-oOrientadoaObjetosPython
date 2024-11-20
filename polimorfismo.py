"""Polimorfismo em POO"""

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        return 'Se move em Terra Firme' 

class Aviao(Veiculo):
    
    def mover(self):
        return 'Voa pelo Ar'

class Barco(Veiculo):

    def mover(self):
        return 'Navega pelo Mar'

class Carro(Veiculo):
    pass

if __name__ == "__main__":
    aviao1 = Aviao('Boeing', '747')
    barco1 = Barco('Titanic', 'qualquer coisa')
    carro1 = Carro('renault', 'sandero')
    for x in (aviao1, barco1, carro1):
        print('\nVeiculo')
        print(f'Marca: {x.marca}')
        print(f'Modelo: {x.modelo}')
        print(f'Movimento: {x.mover()}')