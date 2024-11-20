"""Metodo Destruidor em POO"""

# Definindo a classe MetodoDestruidor
class MetodoDestruidor:
    # O método construtor __init__ é chamado quando o objeto é criado
    def __init__(self, x, y):
        self.x = x  # Atribui o valor de x à instância
        self.y = y  # Atribui o valor de y à instância

    # Método para somar x e y
    def somar(self):
        return self.x + self.y
    
    # O método destruidor __del__ é chamado quando o objeto é deletado
    def __del__(self):
        # O método __class__.__name__ retorna o nome da classe como uma string
        classe = self.__class__.__name__
        
        # Mensagens para exibir ao deletar o objeto
        msg1 = f'-> {type(classe)}'  # Exibe o tipo da classe
        msg = f'{classe} Deletada com sucesso'  # Mensagem indicando que a classe foi deletada
        print(msg1, '\n', msg)

# Quando o script for executado diretamente, o código abaixo será executado
if __name__ == "__main__":
    # Criando um objeto da classe MetodoDestruidor
    numero = MetodoDestruidor(5, 3)
    
    # Chamando o método somar e exibindo o resultado
    print(numero.somar())  # Saída esperada: 8
    
    # Deletando explicitamente o objeto 'numero' com o comando 'del'
    del numero

    # se chamar o objeto numero irá dar erro
    # numero.somar() --> NameError objeto não definido
