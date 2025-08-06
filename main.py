import time
import os
from menuDeProdutos import menu_de_produtos
from menuDeVendas import menu_vendas  

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    opcaoM = "0"

    while opcaoM != "3":
        print("==== MENU PRINCIPAL ====")
        print("1 - Sistema de Produtos")
        print("2 - Sistema de Vendas")
        print("3 - Sair")
        print("========================")
        opcaoM = input("Digite a opção: ")

        if opcaoM == "1":
            menu_de_produtos()
        elif opcaoM == "2":
            menu_vendas()
        elif opcaoM == "3":
            print("Saindo...")
            time.sleep(1.5)
            limpar_tela()
        else:
            print("Opção inválida!")
            time.sleep(1.5)
            limpar_tela()

if __name__ == "__main__":
    menu_principal()
