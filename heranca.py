"""Herança em POO"""

# Classe Pai que define as informações de um pai
class Pai:
    def __init__(self, nome, sobrenome, esposa, filho1=None, filho2=None):
        # O construtor (__init__) recebe os parâmetros e os atribui como atributos da classe
        self.nome = nome         # Atributo para armazenar o nome do pai
        self.sobrenome = sobrenome # Atributo para armazenar o sobrenome do pai
        self.esposa = esposa     # Atributo para armazenar o nome da esposa (mãe dos filhos)
        self.filho1 = filho1     # Atributo para armazenar o primeiro filho
        self.filho2 = filho2     # Atributo para armazenar o segundo filho (opcional)

# Classe Filho que herda da classe Pai
class Filho(Pai):
    def __init__(self, nome, pai):
        # Aqui chamamos o construtor da classe Pai usando 'super()' para herdar seus atributos
        # Passamos os parâmetros necessários para iniciar a classe Pai
        super().__init__(nome, pai.sobrenome, pai.esposa, pai.filho1, pai.filho2)
        
        # O Filho herda os atributos da classe Pai diretamente
        self.mae = self.esposa      # Mae do Filho é a esposa do Pai
        self.irmao = self.filho1    # Irmão do Filho é o filho1 do Pai

if __name__ == '__main__':
    
    # Cria um objeto da classe Pai com os dados do pai
    papai = Pai('Valter', 'Tertuliano', 'Fernanda', 'Juan')

    # Cria um objeto da classe Filho e passa o objeto 'papai' para que o filho herde os dados do pai
    filho = Filho('Juan', papai)

    # Exibindo os dados do Filho
    print(f'Nome do Filho: {filho.nome}')        # Exibe o nome do filho (passado ao criar o objeto)
    print(f'Sobrenome do Filho: {filho.sobrenome}') # Exibe o sobrenome do filho (herdado do pai)
    print(f'Mãe do Filho: {filho.mae}')          # Exibe o nome da mãe (esposa do pai)
    print(f'Irmão do Filho: {filho.irmao}')       # Exibe o nome do irmão (filho1 do pai)

    # Exibindo os dados do Pai
    print(f'Nome do Pai: {papai.nome}')          # Exibe o nome do pai
    print(f'Sobrenome do papai: {papai.sobrenome}') # Exibe o sobrenome do pai
    print(f'Esposa do Pai: {papai.esposa}')      # Exibe o nome da esposa do pai
    print(f'Filho do Pai: {papai.filho1}')       # Exibe o nome do primeiro filho do pai
