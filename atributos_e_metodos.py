"""Introdução a POO"""

# Importando o módulo para manipular datas
import datetime

# Definindo a classe Pessoa, que vai representar o jogador
class Pessoa:
    
    # Método construtor (__init__) que inicia os atributos da pessoa
    def __init__(self, nome='NovoJogador', idade=18, saldo=0, vida=100):
        # Atributos do jogador: nome, idade, saldo, vida
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.vida = vida

    # Método para permitir que o jogador escolha um novo nome
    def novo_nome(self):
        # O nome será alterado conforme a entrada do usuário
        self.nome = input('Digite Seu novo Nome: ')
        return self.nome

    # Método para calcular a idade a partir da data de nascimento
    def data_de_nascimento(self):
        # Pedimos ao jogador para informar a data de nascimento
        print(f'{self.nome}, informe o dia, mês e ano de nascimento: ')
        print(f'Modelo: 13101994')
        data = input("Qual a data do seu nascimento: -> ")

        try:
            # Tentamos converter a data informada para o formato correto
            data_nascimento = datetime.datetime.strptime(data, '%d%m%Y')
            data_atual = datetime.datetime.now()

            # Calculamos a idade com base na diferença de anos
            idade = data_atual.year - data_nascimento.year

            # Verificamos se o aniversário já aconteceu este ano
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1  # Se não, subtrai um ano

            # Atribuímos a idade calculada ao atributo da pessoa
            self.idade = idade
            
            # Verificamos se a pessoa é maior de 18 anos
            if idade < 18:
                print(f'{self.nome}, você ainda não tem idade para abrir uma conta.')
                return False  # Retorna False se for menor de 18 anos
            else:
                print(f'{self.nome}, falta pouco para concluir sua conta...')
                return True  # Retorna True se for maior de 18 anos
        except Exception as Error:
            # Capturamos qualquer erro caso o formato da data esteja errado
            print(f'Houve um erro: {Error}')
            return None

    # Método para exibir os atributos do jogador
    def exibir_atributos(self):
        # Exibindo os dados do jogador de forma formatada
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Saldo: {self.saldo:,.2f}
Vida (HP): {self.vida}
''')

# Função para inicializar o jogador
def jogador_inicial():
    jogador = Pessoa()  # Criando o jogador com os atributos padrão
    print('\nEscolha se você quer criar um novo jogador ou jogar com os atributos padrão:')
    print('[ 1 ] Atributos padrão')
    print('ou')    
    print('[ 2 ] Personalizar atributos')
    
    # O jogador escolhe se quer personalizar os atributos ou usar os padrões
    escolha = int(input('[ 1 ] ou [ 2 ]: '))
    
    if escolha == 1:
        return jogador  # Retorna o jogador com os atributos padrão
    else:
        jogador.novo_nome()  # Permite ao jogador escolher um novo nome
        jogador.data_de_nascimento()  # Solicita a data de nascimento
        return jogador  # Retorna o jogador com atributos personalizados

if __name__ == '__main__':
    # Instanciando o jogador
    jogador1 = jogador_inicial()

    # Exibindo os atributos do jogador
    jogador1.exibir_atributos()
