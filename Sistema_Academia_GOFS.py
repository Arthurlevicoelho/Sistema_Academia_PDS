# Padrão Observer
class Observable:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina


class Academia(Observable):
    def __init__(self):
        super().__init__()
        self.alunos = []
        self.professores = []
        self.aparelhos = []

    def cadastrar_aluno(self, aluno):
        self.alunos.append(aluno)
        self.notify_observers()

    def remover_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                self.notify_observers()
                print("Aluno removido com sucesso!")
                return
        print("Aluno não cadastrado.")

    def editar_aluno(self, matricula, novo_nome):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno.nome = novo_nome
                self.notify_observers()
                return
        print("Aluno não cadastrado.")

    def imprimir_alunos(self):
        print("Lista de alunos cadastrados:")
        for aluno in self.alunos:
            print(f"Matrícula: {aluno.matricula}, Nome: {aluno.nome} - Idade: {aluno.idade}")

    def consultar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                print(f"Matrícula: {aluno.matricula}, Nome: {aluno.nome} - Idade: {aluno.idade}")
                return
        print("Aluno não cadastrado.")

    def cadastrar_professor(self, professor):
        self.professores.append(professor)
        self.notify_observers()

    def remover_professor(self, nome):
        for professor in self.professores:
            if professor.nome == nome:
                self.professores.remove(professor)
                self.notify_observers()
                print("Professor removido com sucesso!")
                return
        print("Professor não cadastrado.")

    def editar_professor(self, nome, nova_disciplina):
        for professor in self.professores:
            if professor.nome == nome:
                professor.disciplina = nova_disciplina
                self.notify_observers()
                return
        print("Professor não cadastrado.")

    def imprimir_professores(self):
        print("Lista de professores cadastrados:")
        for professor in self.professores:
            print(f"Nome: {professor.nome}, Disciplina: {professor.disciplina}")

    def consultar_professor(self, nome):
        for professor in self.professores:
            if professor.nome == nome:
                print(f"Nome: {professor.nome}, Disciplina: {professor.disciplina}")
                return
        print("Professor não cadastrado.")

    def cadastrar_aparelho(self, aparelho):
        self.aparelhos.append(aparelho)

    def remover_aparelho(self, aparelho):
        if aparelho in self.aparelhos:
            self.aparelhos.remove(aparelho)
            print("Aparelho removido com sucesso!")
        else:
            print("Aparelho não cadastrado.")

    def imprimir_aparelhos(self):
        print("Lista de aparelhos cadastrados:")
        for aparelho in self.aparelhos:
            print(aparelho)


# Padrão Factory Method
class PessoaFactory:
    @staticmethod
    def criar_aluno(nome, idade, matricula):
        return Aluno(nome, idade, matricula)

    @staticmethod
    def criar_professor(nome, idade, disciplina):
        return Professor(nome, idade, disciplina)


# Função para manipular o CRUD de alunos
def manipular_crud_alunos(academia):
    while True:
        print("\n----- Menu do CRUD de Alunos -----")
        print("1. Cadastrar aluno")
        print("2. Remover aluno")
        print("3. Editar aluno")
        print("4. Imprimir lista de alunos")
        print("5. Consultar aluno")
        print("6. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            matricula = input("Digite a matrícula do aluno: ")
            aluno = PessoaFactory.criar_aluno(nome, idade, matricula)
            academia.cadastrar_aluno(aluno)
            print("Aluno cadastrado com sucesso!")
        elif opcao == "2":
            matricula = input("Digite a matrícula do aluno a ser removido: ")
            academia.remover_aluno(matricula)
        elif opcao == "3":
            matricula = input("Digite a matrícula do aluno a ser editado: ")
            novo_nome = input("Digite o novo nome do aluno: ")
            academia.editar_aluno(matricula, novo_nome)
        elif opcao == "4":
            academia.imprimir_alunos()
        elif opcao == "5":
            matricula = input("Digite a matrícula do aluno a ser consultado: ")
            academia.consultar_aluno(matricula)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


# Função para manipular o CRUD de professores
def manipular_crud_professores(academia):
    while True:
        print("\n----- Menu do CRUD de Professores -----")
        print("1. Cadastrar professor")
        print("2. Remover professor")
        print("3. Editar professor")
        print("4. Imprimir lista de professores")
        print("5. Consultar professor")
        print("6. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do professor: ")
            idade = int(input("Digite a idade do professor: "))
            disciplina = input("Digite a disciplina do professor: ")
            professor = PessoaFactory.criar_professor(nome, idade, disciplina)
            academia.cadastrar_professor(professor)
            print("Professor cadastrado com sucesso!")
        elif opcao == "2":
            nome = input("Digite o nome do professor a ser removido: ")
            academia.remover_professor(nome)
        elif opcao == "3":
            nome = input("Digite o nome do professor a ser editado: ")
            nova_disciplina = input("Digite a nova disciplina do professor: ")
            academia.editar_professor(nome, nova_disciplina)
        elif opcao == "4":
            academia.imprimir_professores()
        elif opcao == "5":
            nome = input("Digite o nome do professor a ser consultado: ")
            academia.consultar_professor(nome)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


# Função para manipular o CRUD de aparelhos
def manipular_crud_aparelhos(academia):
    while True:
        print("\n----- Menu do CRUD de Aparelhos -----")
        print("1. Cadastrar aparelho")
        print("2. Remover aparelho")
        print("3. Imprimir lista de aparelhos")
        print("4. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            aparelho = input("Digite o nome do aparelho: ")
            academia.cadastrar_aparelho(aparelho)
            print("Aparelho cadastrado com sucesso!")
        elif opcao == "2":
            aparelho = input("Digite o nome do aparelho a ser removido: ")
            academia.remover_aparelho(aparelho)
        elif opcao == "3":
            academia.imprimir_aparelhos()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


# Execução do programa
academia = Academia()

while True:
    print("\n----- Menu Principal -----")
    print("1. Manipular CRUD de Alunos")
    print("2. Manipular CRUD de Professores")
    print("3. Manipular CRUD de Aparelhos")
    print("4. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        manipular_crud_alunos(academia)
    elif opcao == "2":
        manipular_crud_professores(academia)
    elif opcao == "3":
        manipular_crud_aparelhos(academia)
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
