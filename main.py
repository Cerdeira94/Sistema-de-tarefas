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