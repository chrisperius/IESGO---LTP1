class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "Livre"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livro_emprestado = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livro[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membro[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros[titulo_livro].status == "disponível":
            self.livros[titulo_livro].staus = "emprestado"
            self.membros[nome_membro].livros_emprestados.append(titulo_livro)

    def retornar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.membros[nome_membro].livros_emprestados:
            self.membros[nome_membro].livros_emprestados.remove[titulo_livro] = titulo_livro
            self.livros[titulo_livro].status = "disponível"

    def remover_livros(self, titulo_livro):
        if titulo_livro in self.livros:
            del self.livros[titulo_livro]

    def remover_membro(self, nome_membro):
        if nome_membro in self.membros:
            del self.membros[nome_membro]

    def buscar_pelo_nome(self, nome):
        if nome in self.livros:
            return f"Livro: {self.livros[nome].titulo}, Autor: {self.livros[nome].autor}, Status: {self.livros[nome].status}"
        elif nome in self.membros:
            return f"Membro: {self.membros[nome].nome}, Livros emprestados: {', '.join(self.membros[nome].livros_emprestados)}"
        else:
            return "Não encontrado!"
        
def main():
    biblioteca = Biblioteca()

    while True:

        print("\nOpções")
        print("1. Adicionar novo livro")
        print("2. Registrar membro")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Remover livro")
        print("6. Remover membro")
        print("7. Buscar por nome")
        print("8. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            titulo = input("Digite o nome do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = Livro(titulo, autor)
            biblioteca.adicionar_livro(livro)
            print("Livro adcionado!")

        elif opcao == "2":
            nome = input("Digite o nome do membro: ")
            membro = Membro(nome)
            biblioteca.registrar_membro(membro)
            print("Membro registrado!")

        elif opcao == "3":
            titulo_livro = input("Digite o titulo do livro a ser emprestado: ")
            nome_membro = input("Digite o nome do membro: ")
            biblioteca.emprestar_livro(titulo_livro, nome_membro)

        elif opcao == "4":
            titulo_livro = input("Digite o titulo do livro a ser retornado: ")
            nome_membro = input("Digite o nome do membro: ")
            biblioteca.retornar_livro(titulo_livro, nome_membro)

        elif opcao == "5":
            titulo_livro = input("Digite o nome do livro a ser removido: ")
            biblioteca.remover_livros(titulo_livro)

        elif opcao == "6":
            nome_membro = input("Digite o nome do membro a ser removido: ")
            biblioteca.remover_membro(nome_membro)

        elif opcao == "7":
            nome = input("Digite o nome do livro ou membro a ser buscado: ")
            biblioteca.buscar_pelo_nome(nome)

        elif opcao == "8":
            break

        else:
            print("Opção inválida, tente novamente: ")

if __name__ == "__main__":
    main()