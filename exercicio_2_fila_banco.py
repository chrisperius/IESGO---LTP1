class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

class FilaDeBanco:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome, prioridade):
        cliente = Cliente(nome, prioridade)
        if prioridade == 'S':
            self.fila.insert(0, cliente)
        else:
            self.fila.append(cliente)

    def atender_proximo_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo o cliente: {cliente_atendido.nome}")
        else:
            print("A fila está vazia. Nenhum cliente para atender.")

    def visualizar_fila(self):
        if self.fila:
            print("Fila de clientes:")
            for cliente in self.fila:
                print(f"Nome: {cliente.nome}, Prioridade: {cliente.prioridade}")
        else:
            print("A fila está vazia.")

def main():
    fila_banco = FilaDeBanco()

    while True:
        print("\nOpções:")
        print("1. Adicionar cliente à fila")
        print("2. Atender próximo cliente")
        print("3. Visualizar fila")
        print("4. Sair do programa")
        escolha = input("Escolha a opção (1/2/3/4): ")

        if escolha == '1':
            nome = input("Nome do cliente: ")
            prioridade = input("O cliente tem prioridade por lei? (S para Sim, N para Não): ")
            fila_banco.adicionar_cliente(nome, prioridade)
        elif escolha == '2':
            fila_banco.atender_proximo_cliente()
        elif escolha == '3':
            fila_banco.visualizar_fila()
        elif escolha == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()