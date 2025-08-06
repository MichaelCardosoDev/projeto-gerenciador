import time
import os
from bancoDeDados import (
    criar_tabela, salvar_produto, mostrar_produto,
    atualizar_preco, atualizar_quantidade, mudar_informacoes_do_produto
)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

criar_tabela()

class Produtos():
    def __init__(self, id, nome, descrição, quantidade_disponivel, preço):
        self.id = id
        self.nome = nome
        self.descrição = descrição
        self.quantidade_disponivel = quantidade_disponivel
        self.__preço = preço

    def preço(self):
        return self.__preço

    def aumentar_preço(self):
        self.__preço += self.__preço


def menu_de_produtos():
    opcao = "0"
    limpar_tela()
    while opcao != "6":
        print("==== MENU DE PRODUTOS ====")
        print("1 - Cadastrar produto")
        print("2 - Mostrar produtos")
        print("3 - Atualizar preço")
        print("4 - Atualizar quantidade")
        print("5 - Mudar informações do produto")
        print("6 - Voltar")
        print("==========================")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            limpar_tela()
            print("==== MENU DE Cadastro ====")
            id = int(input("Digite o ID do produto: "))
            nome = input("Digite o nome do produto: ")
            descrição = input("Digite a descrição do produto: ")
            quantidade_disponivel = int(input("Digite a quantidade do produto: "))
            preço = float(input("Digite o preço do produto: "))
            Sistema = Produtos(id, nome, descrição, quantidade_disponivel, preço)
            salvar_produto(id, nome, descrição, quantidade_disponivel, preço)
            print("Produto salvo no banco de dados com sucesso!")
            time.sleep(1.5)
            limpar_tela()

        elif opcao == "2":
            limpar_tela()
            print("==== MENU DE ESTOQUE ====")
            produtos = mostrar_produto()
            if not produtos:
                print("Nenhum produto encontrado.")
            else:
                for p in produtos:
                    print(f"ID: {p[0]}")
                    print(f"Nome: {p[1]}")
                    print(f"Descrição: {p[2]}")
                    print(f"Quantidade: {p[3]}")
                    print(f"Preço: R${p[4]:.2f}")
                    print("-------------------------")
            input("Pressione Enter para continuar...")
            limpar_tela()

        elif opcao == "3":
            limpar_tela()
            print("==== MENU DA ATUALIZAÇÕ DE PREÇO ====")
            id = int(input("Digite o ID do produto que deseja atualizar: "))
            novo_preco = float(input("Digite o novo preço: "))
            atualizar_preco(id, novo_preco)
            print("Preço atualizado com sucesso!")
            time.sleep(1.5)
            limpar_tela()

        elif opcao == "4":
            limpar_tela()
            print("==== MENU DA ATUALIZAÇÃO DE QUANTIDADE ====")
            id = int(input("Digite o ID do produto que deseja atualizar: "))
            nova_quantidade = float(input("Digite a nova quantidade: "))
            atualizar_quantidade(id, nova_quantidade)
            print("Quantidade atualizada com sucesso!")
            time.sleep(1.5)
            limpar_tela()

        elif opcao == "5":
            limpar_tela()
            print("==== MENU DA ATUALIZAÇÃO DE PRODUTOS ====")
            id = int(input("Digite o ID do produto que deseja atualizar: "))
            novo_nome = input("Digite o novo nome: ")
            nova_descicao = input("Digite a nova descrição: ")
            mudar_informacoes_do_produto(id, novo_nome, nova_descicao)
            print("Informações atualizadas com sucesso!")
            time.sleep(1.5)
            limpar_tela()

        elif opcao == "6":
            print("Voltando ao menu principal...")
            time.sleep(1.5)
            limpar_tela()

        else:
            print("Opção inválida!")
            time.sleep(1.5)
            limpar_tela()
