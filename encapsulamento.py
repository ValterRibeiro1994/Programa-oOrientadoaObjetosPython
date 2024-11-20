"""Encapsulamento em POO"""

# Definimos uma classe chamada Carro
class Carro:
    # O construtor __init__ inicia os atributos do carro
    def __init__(self, modelo, marca, velocidade_maxima, cor):
        self.modelo = modelo                # Atributo público para armazenar o modelo do carro
        self.marca = marca                  # Atributo público para armazenar a marca do carro
        self._velocidade_maxima = velocidade_maxima  # Atributo privado, representado com o underscore (_) indicando que deve ser protegido
        self.cor = cor                      # Atributo público para armazenar a cor do carro

    # Método getter para acessar a velocidade máxima (atributo privado)
    def get_velocidade_maxima(self):
        return self._velocidade_maxima  # Retorna o valor de _velocidade_maxima para quem chamar esse método

    # Método setter para atualizar a velocidade máxima de forma controlada
    def set_velocidade_maxima(self, aumento: float) -> None:
        # O aumento deve ser informado como uma porcentagem (ex: 0.1 para 10%, -0.5 para -50%)
        try:
            # Verificamos se o aumento é um número de ponto flutuante (float)
            if isinstance(aumento, float):
                # Se o aumento for positivo, indicamos que estamos aumentando a velocidade
                if aumento > 0:
                    print(f'Subindo a velocidade máxima em {abs(aumento) * 100}%')
                # Se o aumento for negativo, indicamos que estamos diminuindo a velocidade
                else:
                    print(f'Baixando a velocidade máxima em {abs(aumento) * 100}%')

                # Verificamos se o aumento está dentro do intervalo permitido (-1 a 1)
                if aumento > -1 and aumento < 1:
                    # Calculamos o novo valor de _velocidade_maxima com o aumento percentual
                    self._velocidade_maxima += (self._velocidade_maxima * aumento)
                else:
                    # Caso o aumento não esteja dentro do intervalo esperado, mostramos uma mensagem de erro
                    print('Fora do intervalo permitido entre -1 e 1')
            else:
                # Se o aumento não for um número de ponto flutuante, mostramos uma mensagem de erro
                print('Informe uma porcentagem válida:\n10% = 0.1\n62% = 0.62')
        except Exception as E:
            # Captura e exibe qualquer erro que possa ocorrer durante a execução do código
            print(f'Erro: {E}')

if __name__ == "__main__":
    # Criamos um objeto da classe Carro com os dados do Fusca
    fusca = Carro('volkswagen', 'fusca', 100, 'verde')
    
    # Chamamos o método setter para aumentar a velocidade máxima em 50%
    fusca.set_velocidade_maxima(0.5)
    
    # Chamamos o método getter para obter o valor da velocidade máxima após o aumento
    print(fusca.get_velocidade_maxima())
    
    # Chamamos o método setter novamente para diminuir a velocidade máxima em 10%
    fusca.set_velocidade_maxima(-0.1)
    
    # Chamamos o método getter novamente para obter o valor da velocidade máxima após a redução
    print(fusca.get_velocidade_maxima())
