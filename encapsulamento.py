'''Encapsulamento em POO'''

class Carro:
    def __init__(self, modelo, marca, velocidade_maxima, cor):
        self.modelo = modelo
        self.marca = marca
        self._velocidade_maxima = velocidade_maxima # atributo privado
        self.cor = cor

    # criamos um getter para obter o valor de _velocidade_maxima
    def get_velocidade_maxima(self):
        return self._velocidade_maxima
    
    # criamos um setter para atualizar o atributo protegido
    def set_velocidade_maxima(self, aumento: float) -> None:
        # o aumento deve vir repesentado em porcentagem 0.1, 0.5 e etc...
        try:
            if isinstance(aumento, float):
                if aumento > 0:
                    print(f'Subindo a velocidade maxima em {abs(aumento) * 100}%')
                else:
                    print(f'Baixando a velocidade maxima em {abs(aumento) * 100}%')

                if aumento > -1 and aumento < 1:
                    self._velocidade_maxima += (self._velocidade_maxima * aumento)
                else:
                    print('Fora do intervalo permitido entre -1 e 1 ')
            else:
                print('Informe uma porcentagem valida:\n10% = 0.1\n62% = 0.62')
        except Exception as E:
            print(f'Erro: {E}')

fusca = Carro('volkswagen', 'fusca', 100, 'verde')
fusca.set_velocidade_maxima(0.5)
print(fusca.get_velocidade_maxima())
fusca.set_velocidade_maxima(-0.1)
print(fusca.get_velocidade_maxima())
