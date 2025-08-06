import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao VARCHAR(100) NOT NULL,
            quantidade INT CHECK (quantidade > 0),
            preco DECIMAL(9,2)
        )
    """)

    conexao.commit()
    conexao.close()

def salvar_produto(id, nome, descricao, quantidade, preco):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO Produtos (id, nome, descricao, quantidade, preco) VALUES (?, ?, ?, ?, ?)",
        (id, nome, descricao, quantidade, preco)
    )

    conexao.commit()
    conexao.close()

def mostrar_produto():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, descricao, quantidade, preco FROM Produtos")
    produtos = cursor.fetchall()

    conexao.close()
    return produtos

def atualizar_preco(id, novo_preco):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE Produtos SET preco = ? WHERE id = ?",
        (novo_preco, id)
    )

    conexao.commit()
    conexao.close()

def atualizar_quantidade(id, nova_quantidade):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE Produtos SET quantidade = ? WHERE id = ?",
        (nova_quantidade, id)
    )

    conexao.commit()
    conexao.close()

def mudar_informacoes_do_produto(id, novo_nome, nova_descricao):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE Produtos SET nome = ?, descricao = ? WHERE id = ?",
        (novo_nome, nova_descricao, id)
    )

    conexao.commit()
    conexao.close()

def criar_tabela_vendas():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vendas (
            id_vendas INT PRIMARY KEY,
            id_produto INT,
            quantidade_da_vanda INT,
            data_da_venda DATE
        )
    """)

    conexao.commit()
    conexao.close()

def salvar_venda(id_venda, id_do_produto_vendido, quantidade_vendida, data_a_venda):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO Vendas (id_vendas, id_produto, quantidade_da_vanda, data_da_venda) VALUES (?, ?, ?, ?)",
        (id_venda, id_do_produto_vendido, quantidade_vendida, data_a_venda)
    )

    conexao.commit()
    conexao.close()

def listar_vendas():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT V.id_vendas, P.nome, V.quantidade_da_vanda, V.data_da_venda
        FROM Vendas V
        JOIN Produtos P ON V.id_produto = P.id
    """)

    vendas = cursor.fetchall()
    conexao.close()
    return vendas

def calcular_total(id_produto, quantidade):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT preco FROM Produtos WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        preco = resultado[0]
        total = preco * quantidade
        return total
    else:
        return None


def remover_estoque(id_produto, quantidade_da_venda):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    
    cursor.execute("SELECT quantidade FROM Produtos WHERE id = ?", (id_produto,))
    resultado = cursor.fetchone()

    if resultado:
        quantidade_atual = resultado[0]

        if quantidade_da_venda > quantidade_atual:
            print(" Estoque insuficiente! Venda cancelada.")
            conexao.close()
            return None

        nova_quantidade = quantidade_atual - quantidade_da_venda

        
        cursor.execute("UPDATE Produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))
        conexao.commit()
        conexao.close()

        return nova_quantidade
    else:
        conexao.close()
        print(" Produto não encontrado.")
        return None

def cancelar_venda(id_venda):
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()

    
    cursor.execute("SELECT id_produto, quantidade_da_vanda FROM Vendas WHERE id_vendas = ?", (id_venda,))
    resultado = cursor.fetchone()

    if resultado:
        id_produto, quantidade_vendida = resultado

        cursor.execute("DELETE FROM Vendas WHERE id_vendas = ?", (id_venda,))

        cursor.execute("UPDATE Produtos SET quantidade = quantidade + ? WHERE id = ?", (quantidade_vendida, id_produto))

        conexao.commit()
        conexao.close()
        print(f" Venda {id_venda} cancelada e estoque restaurado.")
        return True
    else:
        conexao.close()
        print(" Venda não encontrada.")
        return False
    