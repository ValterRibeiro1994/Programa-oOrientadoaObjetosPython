"""Atributos de classe em POO"""

class Funcionarios:
    # definimos um atributo para a CLASSE
    quantidade_funcionarios = 0 # ele conta a quantidade de objetos criados( quantos funcionarios tem)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        # para cada vez que um Funcionario for contratado(um objeto for instanciado)
        Funcionarios.quantidade_funcionarios += 1 # acrescente 1 no atributo da classe automaticamente

    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Total de Funcionarios: {self.quantidade_funcionarios}')


if __name__ == "__main__":
    
    # Instanciando os objetos - Criando os Funcionarios
    alex = Funcionarios('Alex', 25)
    alexandre = Funcionarios('Alexandre', 27)

    # acessando o atributo da classe diretamente
    print("Funcionarios Ativos: ", Funcionarios.quantidade_funcionarios)
    