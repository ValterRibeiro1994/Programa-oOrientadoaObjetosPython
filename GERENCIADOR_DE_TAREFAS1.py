import os
import json

class GerenciarTarefas:
    """Classe que gerencia tarefas, salvando em um arquivo JSON.
    
    O gerenciador permite adicionar, exibir, remover e limpar tarefas.
    """

    ARQUIVO_JSON = 'TarefasRegistradas.json'  # Arquivo onde as tarefas são salvas.

    def __init__(self):
        """Inicializa o gerenciador de tarefas, carregando as tarefas do arquivo JSON."""
        self.tarefas = self._carregar_json()

    def _carregar_json(self):
        """Carrega as tarefas do arquivo JSON.
        
        Se o arquivo não existir ou houver um erro na leitura, retorna um dicionário vazio.
        """
        if os.path.exists(self.ARQUIVO_JSON):
            try:
                with open(self.ARQUIVO_JSON, 'r', encoding='utf-8') as documento:
                    return json.load(documento)
            except json.JSONDecodeError:
                return {}
        return {}

    def _salvar_tarefa(self):
        """Salva a lista de tarefas no arquivo JSON."""
        with open(self.ARQUIVO_JSON, 'w', encoding='utf-8') as documento:
            json.dump(self.tarefas, documento, indent=4, ensure_ascii=False)

    def adicionar_tarefa(self, nome, data_tarefa, hora_tarefa, descricao, prioridade):
        """Adiciona uma nova tarefa.
        
        Argumentos:
        nome (str): O nome da tarefa.
        data_tarefa (str): A data da tarefa no formato dd/mm/aaaa.
        hora_tarefa (str): A hora da tarefa no formato hh:mm.
        descricao (str): A descrição da tarefa.
        prioridade (str): A prioridade da tarefa (Alta, Média, Baixa).
        """
        if nome in self.tarefas:
            print(f'Essa Tarefa "{nome}" já existe.')
            return
        
        nova_tarefa = {
            'Data da tarefa': data_tarefa,
            'Hora da tarefa': hora_tarefa,
            'Descrição da tarefa': descricao,
            'Prioridade': prioridade
        }

        self.tarefas[nome] = nova_tarefa
        self._salvar_tarefa()
        print(f'Tarefa "{nome}" adicionada com sucesso.')

    def exibir_tarefas(self):
        """Exibe todas as tarefas salvas."""
        if not self.tarefas:
            print('Não há tarefas registradas.')
        else:
            for n, (nome, detalhes) in enumerate(self.tarefas.items(), start=1):
                print(f'\nTarefa {n}: {nome}')
                for chave, valor in detalhes.items():
                    print(f'{chave}: {valor}')

    def remover_tarefa(self, nome):
        """Remove uma tarefa pelo nome.
        
        Argumento:
        nome (str): O nome da tarefa a ser removida.
        """
        if nome in self.tarefas:
            del self.tarefas[nome]
            self._salvar_tarefa()
            print(f'Tarefa "{nome}" removida com sucesso.')
        else:
            print(f'Tarefa "{nome}" não encontrada.')

    def limpar_tarefas(self):
        """Remove todas as tarefas salvas."""
        self.tarefas = {}
        self._salvar_tarefa()
        print("Todas as tarefas foram removidas.")

if __name__ == "__main__":
    gerenciador = GerenciarTarefas()
    gerenciador._carregar_json()

    while True:
        print("\n=== Menu do Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Exibir Tarefas")
        print("4. Limpar Todas as Tarefas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da Tarefa: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")  # Hora da tarefa
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Alta, Média, Baixa): ")
            gerenciador.adicionar_tarefa(nome, data, hora, descricao, prioridade)

        elif opcao == "2":
            nome = input("Digite o nome da tarefa a remover: ")
            gerenciador.remover_tarefa(nome)

        elif opcao == "3":
            gerenciador.exibir_tarefas()

        elif opcao == "4":
            confirmar = input("Tem certeza que deseja limpar todas as tarefas? (s/n): ")
            if confirmar.lower() == "s":
                gerenciador.limpar_tarefas()

        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
