'''Programação Orientada a Objetos - breve introdução'''

import datetime

# vamos criar um objeto ( uma pessoa ) ou instanciar um objeto
class Pessoa: 

    # usamos o metodo construtor para definir os atributos do objeto
    def __init__(self, nome='NovoJogador', idade=18, saldo=0, vida=100):

        # definimos os atributos acima
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.vida = vida

    # agora criamos um metodo para que o NovoJogador possa escolher um novo nome
    def novo_nome(self):
        self.nome = input('Digite Seu novo Nome: ')
        return self.nome
    
    # agora criamos um metodo para garantir que o usuario seja maior de 18 anos
    ##### pedimos o ano de nascimento e o mês
    def data_de_nascimento(self):
        
        # exibimos uma mensagem ao usuario pedindo a data de nascimento
        print(f'{self.nome} informe o dia, o mês e o ano de nascimento: ')
        print(f'Modelo : 13101994')
        data = input("Qual a data do seu nascimento: -> ")

        # primeiro tentamos converter a entrada recebida
        try: # pode ter erros na entrada

            data_nascimento = datetime.datetime.strptime(data, '%d%m%Y')
            data_atual = datetime.datetime.now()

            # calculamos a diferença de anos
            idade = data_atual.year - data_nascimento.year

            # verifica se o aniversario não ocorreu ainda
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            self.idade = idade
            
            if idade < 18:
                print(f'{self.nome} Infelizmente você ainda não tem idade para abrir uma conta.')
                return False
            else:
                print(f'{self.nome} Falta pouco para concluir a sua conta ....')
                return True
        # capturamos possiveis erros     
        except Exception as Error:
            print(f'Houve um Erro: ', Error)
            return None
        
    def exibir_atributos(self):
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Saldo: {self.saldo:,.2f}
Vida (HP): {self.vida}
''')
        

# vamos usar essa clase (pessoa - objeto )
def jogador_inicial():
    jogador = Pessoa()
    print('\nInforme se voce quer criar um novo jogador, ou se prefere jogador como usuario padrão: ')
    print('[ 1 ] Atributos padrão se mantem')
    print('ou')    
    print('[ 2 ] Personalizamos os atributos')
    escolha = int(input('[ 1 ] ou [ 2 ]: '))
    if escolha == 1:
        return jogador
    else:
        jogador.novo_nome()
        jogador.data_de_nascimento()
        return jogador

# vamos instanciar o objeto
jogador1 = jogador_inicial()
jogador1.exibir_atributos()