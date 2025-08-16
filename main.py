print (" Lista de tarefas")


while True:
    escolha = input(
        """
Escolha as seguintes opções:

1. Adicionar tarefa
2. listar tarefa
3. Remover tarefa
4. Sair
Opção: """
    )

    if escolha == "4":
        break

print("Fim da execução, até uma outra hora!")

from datetime import datetime

class Tarefa:
    def __init__(self, nome: str, data_criacao:datetime, prazo:datetime , tag:str):
        self.nome = nome
        self.data_criacao = data_criacao
        self.prazo = prazo
        self.tag = tag