from biblioteca.livros import inserir_livro, remover_livro, atualizar_livro, receber_livros
from biblioteca.usuarios import inserir_usuario, remover_usuario, atualizar_usuario, receber_usuarios
from biblioteca.emprestimos import emprestar_livro, devolver_livro, atualizar_emprestimo, receber_emprestimos
from biblioteca.relatorios import gerar_relatorio

def exibir_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Módulo de Livros")
    print("2. Módulo de Usuários")
    print("3. Módulo de Empréstimos")
    print("4. Módulo de Relatórios")
    print("0. Sair")
    return input("Selecione uma opção: ")

def menu_livros():
    while True:
        print("\n--- Módulo de Livros ---")
        print("1. Inserir Livro")
        print("2. Remover Livro")
        print("3. Atualizar Livro")
        print("4. Listar Livros")
        print("0. Voltar")
        opcao = input("Selecione uma opção: ")
        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            inserir_livro(titulo, autor)
        elif opcao == '2':
            livro_id = int(input("ID do livro a remover: "))
            remover_livro(livro_id)
        elif opcao == '3':
            livro_id = int(input("ID do livro a atualizar: "))
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            atualizar_livro(livro_id, titulo, autor)
        elif opcao == '4':
            livros = receber_livros()
            for livro in livros:
                print(livro)
        elif opcao == '0':
            break

def menu_usuarios():
    while True:
        print("\n--- Módulo de Usuários ---")
        print("1. Inserir Usuário")
        print("2. Remover Usuário")
        print("3. Atualizar Usuário")
        print("4. Listar Usuários")
        print("0. Voltar")
        opcao = input("Selecione uma opção: ")
        if opcao == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            inserir_usuario(nome, email)
        elif opcao == '2':
            usuario_id = int(input("ID do usuário a remover: "))
            remover_usuario(usuario_id)
        elif opcao == '3':
            usuario_id = int(input("ID do usuário a atualizar: "))
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            atualizar_usuario(usuario_id, nome, email)
        elif opcao == '4':
            usuarios = receber_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif opcao == '0':
            break

def menu_emprestimos():
    while True:
        print("\n--- Módulo de Empréstimos ---")
        print("1. Emprestar Livro")
        print("2. Devolver Livro")
        print("3. Atualizar Empréstimo")
        print("4. Listar Empréstimos")
        print("0. Voltar")
        opcao = input("Selecione uma opção: ")
        if opcao == '1':
            usuario_id = int(input("ID do Usuário: "))
            livro_id = int(input("ID do Livro: "))
            if emprestar_livro(usuario_id, livro_id):
                print("Empréstimo realizado com sucesso.")
            else:
                print("Empréstimo falhou. Verifique a disponibilidade do livro ou o número de livros já emprestados pelo usuário.")
        elif opcao == '2':
            livro_id = int(input("ID do Livro: "))
            devolver_livro(livro_id)
            print("Livro devolvido com sucesso.")
        elif opcao == '3':
            emprestimo_id = int(input("ID do Empréstimo: "))
            novo_livro_id = int(input("Novo ID do Livro: "))
            atualizar_emprestimo(emprestimo_id, novo_livro_id)
            print("Empréstimo atualizado com sucesso.")
        elif opcao == '4':
            emprestimos = receber_emprestimos()
            for emprestimo in emprestimos:
                print(emprestimo)
        elif opcao == '0':
            break

def main():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            menu_livros()
        elif opcao == '2':
            menu_usuarios()
        elif opcao == '3':
            menu_emprestimos()
        elif opcao == '4':
            arquivo_relatorio = gerar_relatorio()
            print(f"Relatório gerado: {arquivo_relatorio}")
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


