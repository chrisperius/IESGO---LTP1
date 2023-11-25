class Livro:

    def __init__(self, titulo, autor):

        self.titulo = titulo

        self.autor = autor

        self.status = "disponível"

 

class Membro:

    def __init__(self, nome):

        self.nome = nome

        self.livros_emprestados = []

 

class Biblioteca:

    def __init__(self):

        self.livros = {}

        self.membros = {}

 

    def adicionar_livro(self, livro):

        self.livros[livro.titulo] = livro

 

    def registrar_membro(self, membro):

        self.membros[membro.nome] = membro

 

    def emprestar_livro(self, titulo_livro, nome_membro):

        if titulo_livro in self.livros and nome_membro in self.membros:

            livro = self.livros[titulo_livro]

            if livro.status == "disponível":

                membro = self.membros[nome_membro]

                livro.status = "emprestado"

                membro.livros_emprestados.append(livro)

                return f"{titulo_livro} emprestado para {nome_membro}."

            else:

                return f"{titulo_livro} não está disponível para empréstimo."

        else:

            return "Livro ou membro não encontrados."

 

    def retornar_livro(self, titulo_livro, nome_membro):

        if titulo_livro in self.livros and nome_membro in self.membros:

            livro = self.livros[titulo_livro]

            membro = self.membros[nome_membro]

            if livro in membro.livros_emprestados:

                livro.status = "disponível"

                membro.livros_emprestados.remove(livro)

                return f"{titulo_livro} devolvido por {nome_membro}."

            else:

                return f"{titulo_livro} não foi emprestado para {nome_membro}."

        else:

            return "Livro ou membro não encontrados."

 

# Emprestar ou retornar um livro

def operacao_livro(biblioteca, operacao):

    while True:

        titulo_livro = input("Digite o título do livro: ")

        if titulo_livro in biblioteca.livros:

            nome_membro = input("Digite o nome do membro: ")

            if nome_membro in biblioteca.membros:

                if operacao == "emprestar":

                    print(biblioteca.emprestar_livro(titulo_livro, nome_membro))

                elif operacao == "devolver":

                    print(biblioteca.retornar_livro(titulo_livro, nome_membro))

                break

            else:

                print("Membro não encontrado.")

        else:

            print("Livro não encontrado.")

 

# Criar instâncias de livros

livro1 = Livro("Fortaleza Digital", "Dan Brown")

livro2 = Livro("O símbolo perdido", "Dan Brown")

livro3 = Livro("A estrada da noite", "Joe Hill")

 


# Criar instâncias de membros

membro1 = Membro(input(" digite o seu nome: "))

 

# Criar uma instância da biblioteca

biblioteca = Biblioteca()

 

# Adicionar livros à biblioteca

biblioteca.adicionar_livro(livro1)

biblioteca.adicionar_livro(livro2)

biblioteca.adicionar_livro(livro3)

 

# Registro de membros na biblioteca

biblioteca.registrar_membro(membro1)

 

# Solicitar pedido de empréstimo ou retorno de livros

while True:

    print("\nEscolha uma operação:")

    print("1. Pegar livro emprestado")

    print("2. Devolver livro")

    print("3. Sair")

    escolha = input("Digite o número da operação desejada: ")

 

    if escolha == "1":

        operacao_livro(biblioteca, "emprestar")

    elif escolha == "2":

        operacao_livro(biblioteca, "devolver")

    elif escolha == "3":
        print("Você saiu!")

        break

    else:

        print("Opção inválida. Digite 1, 2 ou 3.")