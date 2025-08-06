import random
import time
import os
from datetime import datetime
from bancoDeDados import mostrar_produto, salvar_venda, listar_vendas, calcular_total, remover_estoque, cancelar_venda

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Vendas:
    def __init__(self, id_venda, id_do_produto_vendido, quantidade_vendida, data_a_venda):
        self.id_venda = id_venda
        self.id_do_produto_vendido = id_do_produto_vendido
        self.quantidade_vendida = quantidade_vendida
        self.data_a_venda = data_a_venda

def menu_vendas():
    opcao = "0"
    limpar_tela()
    while opcao != "4":
        print("==== MENU DE VENDAS ====")
        print("1 - Realizar venda")
        print("2 - Histórico de vendas")
        print("3 - Cancelamento da compra")
        print("4 - Voltar")
        opcao = input("Digite a opção: ")

        if opcao == "1":
            limpar_tela()
            print("==== CAIXA ====")
            while True:
                id_produto = input("Digite o ID do produto: ")
                produtos = mostrar_produto()
                produto_encontrado = None

                for prod in produtos:
                    if str(prod[0]) == id_produto:
                        produto_encontrado = prod
                        break

                if produto_encontrado:
                    print(f"Produto encontrado: {produto_encontrado}")
                    quantidade_da_venda = int(input("Digite a quantidade vendida: "))
                    total = calcular_total(id_produto, quantidade_da_venda)
                    print(f"Total da venda: R$ {total:.2f}")
                    id_venda = random.randint(1000, 9999)
                    data_venda = datetime.now().strftime("%d/%m/%Y %H:%M")
                    salvar_venda(id_venda, id_produto, quantidade_da_venda, data_venda)
                    print("Venda realizada com sucesso!")
                    nova_quantidade = remover_estoque(id_produto, quantidade_da_venda)
                    if nova_quantidade is None:
                        print("Venda não registrada devido a erro no estoque.")
                    else:
                        print(f"Nova quantidade em estoque: {nova_quantidade}")
                        print("Produto não encontrado.")
                
                opcaoQuan = input("Deseja inserir mais um item (S/N)? ").lower()
                if opcaoQuan == "n":
                    break
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "2":
            limpar_tela()
            print("==== HISTÓRICO DE VENDAS ====")
            vendas = listar_vendas()
            if vendas:
                for venda in vendas:
                    print(f"ID da venda: {venda[0]}")
                    print(f"Produto: {venda[1]}")
                    print(f"Quantidade: {venda[2]}")
                    print(f"Data: {venda[3]}")
                    print("---------------------------")
            else:
                print("Nenhuma venda registrada.")
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "3":
            limpar_tela()
            print("==== CANCELAMENTO DE VENDAS ====")
            id_cancelamento = int(input("Digite o ID da venda a cancelar: "))
            cancelar_venda(id_cancelamento)
            input("Pressione Enter para voltar ao menu...")
            
            

        elif opcao == "4":
            print("Voltando ao menu principal...")
            time.sleep(1.5)
            limpar_tela()
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

