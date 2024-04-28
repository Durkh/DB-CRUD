import psycopg2
import random
from tabulate import tabulate
from datetime import datetime


def conectar():
    try:
        conn = psycopg2.connect(
            "dbname='jhacogja' user='jhacogja' host='isabelle.db.elephantsql.com' password='kUGSLRalV0LsOp36SqromCEl3DwKYcsS'")
        print("Conexão ao banco de dados estabelecida.")
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


class Manga:
    def __init__(self, isbn, titulo, volume, autor, preco, quantidade, categoria, local_fabricacao):
        self.isbn = isbn
        self.titulo = titulo
        self.volume = volume
        self.autor = autor
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria
        self.local_fabricacao = local_fabricacao


class EstoqueMangas:
    def __init__(self, connection):
        self.conexao = connection

    def adicionar_manga(self, manga: Manga):
        try:
            self.conexao.cursor().execute("INSERT INTO estoque (ISBN, titulo, volume, autor, preco, quantidade, categoria, local_de_fab) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                                          (manga.isbn, manga.titulo, manga.volume, manga.autor, manga.preco, manga.quantidade, manga.categoria, manga.local_fabricacao))
            self.conexao.commit()
            print("Mangá inserido com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)

    def pesquisar_manga(self, titulo):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM estoque WHERE titulo ILIKE %s", (f"%{titulo}%",))
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar manga:", error)
            return None

    def alterar_manga(self, isbn, novo_manga: Manga):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("UPDATE estoque SET titulo = %s, volume = %s, autor = %s, preco = %s, quantidade = %s, categoria = %s, local_de_fab = %s WHERE ISBN = %s", (
                    novo_manga.titulo, novo_manga.volume, novo_manga.autor, novo_manga.preco, novo_manga.quantidade, novo_manga.categoria, novo_manga.local_fabricacao, isbn))
                self.conexao.commit()
                print("Título alterado com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao alterar título:", error)

    def remover_manga(self, isbn):
        print(isbn)
        try:
            self.conexao.cursor().execute(
                "DELETE FROM estoque WHERE ISBN = %s", (isbn,))
            self.conexao.commit()
            print("Título removido com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao remover funcionario:", error)

    def exibir_estoque(self):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM estoque")
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None

    def exibir_estoque_baixo(self):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM estoque WHERE quantidade < 5")
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None

    def exibir_estoque_Mari(self):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM estoque WHERE local_de_fab ILIKE 'Mari'")
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None

    def exibir_estoque_faixa_preco(self, p1, p2):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM estoque WHERE preco BETWEEN %s AND %s", (p1, p2))
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None


class Pessoa:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf


class Vendedor(Pessoa):
    def __init__(self, nome, email, cpf, matricula):
        super().__init__(nome, email, cpf)
        self.matricula = matricula


class Cliente(Pessoa):
    def __init__(self, nome, email, cpf, time, obra_favorita, cidade_natal):
        super().__init__(nome, email, cpf)
        self.time = time
        self.obra_favorita = obra_favorita
        self.cidade_natal = cidade_natal


class Relatorio:
    def __init__(self, conexao):
        self.conexao = conexao
        self.relatorio = []

    def vendas(self, vendedor, data_inicial, data_final):
        if vendedor:
            try:
                with self.conexao.cursor() as cursor:
                    cursor.execute(
                        "select view_funcionarios.nome, COUNT(view_vendas.quantidade) as total_vendas, CONCAT('R$ ', COALESCE(SUM(view_vendas.total), 0.00)) AS total_gasto from view_funcionarios left join view_vendas on view_vendas.cpf_funcionario=view_funcionarios.cpf join vendas on vendas.id_venda = view_vendas.id_venda where view_funcionarios.cpf = %s and vendas.data >= %s and vendas.data <= %s GROUP BY view_funcionarios.nome", (vendedor, data_inicial, data_final))
                    vendas = cursor.fetchall()
            except (Exception, psycopg2.Error) as error:
                print("Erro ao recuperar dados:", error)
                return None

            self.relatorio.append("Relatório de vendas:")
            header = ["Vendedor", "Quantidade de vendas", "Total vendido"]
            self.relatorio.append(tabulate(vendas, headers=header))

            return self.relatorio
        else:
            try:
                with self.conexao.cursor() as cursor:
                    cursor.execute(
                        "select view_funcionarios.nome, COUNT(view_vendas.quantidade) as total_vendas, CONCAT('R$ ', COALESCE(SUM(view_vendas.total), 0.00)) AS total_gasto from view_funcionarios left join view_vendas on view_vendas.cpf_funcionario=view_funcionarios.cpf GROUP BY view_funcionarios.nome")
                    vendas = cursor.fetchall()
            except (Exception, psycopg2.Error) as error:
                print("Erro ao recuperar dados:", error)
                return None

            self.relatorio.append("Relatório de vendas:")
            header = ["Vendedor", "Quantidade de vendas", "Total vendido"]
            self.relatorio.append(tabulate(vendas, headers=header))
            self.relatorio.append(
                f"\nTotal de vendas: {sum([venda[1] for venda in vendas])} | Total vendido: R${sum([float(venda[2].replace('R$ ', '')) for venda in vendas])}")

            return self.relatorio

    def estoque(self):
        estoque_baixo = []
        em_falta = []
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM estoque")
                estoque = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None
        self.relatorio.append("Relatório de estoque:")
        header = ["ISBN", "Título", "Autor", "Volume", "Preço",
                  "Quantidade", "Categoria", "Local de fabricação"]
        self.relatorio.append(tabulate(estoque, headers=header))
        self.relatorio.append(
            f"\nTotal de mangás em estoque: {len(estoque)} | Total de unidades mangás: {sum([manga[5] for manga in estoque])} | Valor total do estoque: R${sum([manga[4]*manga[5] for manga in estoque])}\n")
        for manga in estoque:
            if manga[5] < 5:
                estoque_baixo.append(manga)
        self.relatorio.append("\nMangás em estoque baixo:")
        self.relatorio.append(tabulate(estoque_baixo, headers=header))
        self.relatorio.append("\nMangás em falta:")
        for manga in estoque:
            if manga[5] == 0:
                em_falta.append(manga)
        self.relatorio.append(tabulate(em_falta, headers=header))

        return self.relatorio

    def clientes(self):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT view_clientes.nome, view_clientes.cpf, view_clientes.email, view_clientes.time_do_coracao, view_clientes.obra_favorita, view_clientes.cidade_natal, COUNT(view_vendas.total) as total_vendas, CONCAT('R$ ', COALESCE(SUM(view_vendas.total), 0.00)) AS total_gasto FROM view_clientes LEFT JOIN view_vendas ON view_vendas.cpf_cliente=view_clientes.cpf GROUP BY view_clientes.nome, view_clientes.cpf, view_clientes.email, view_clientes.time_do_coracao, view_clientes.obra_favorita, view_clientes.cidade_natal")
                clientes = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None
        self.relatorio.append("Relatório de clientes:")
        header = ["Nome", "CPF", "Email", "Time do coracao", "Obra favorita",
                  "Cidade natal", "Compras realizadas", "Total gasto"]
        self.relatorio.append(tabulate(clientes, headers=header))
        self.relatorio.append(
            f"\nTotal de clientes: {len(clientes)} || Total de compras realizadas: {sum([cliente[6] for cliente in clientes])} || Total gasto: R${sum([float(cliente[7].replace('R$ ', '')) for cliente in clientes])}")

        return self.relatorio


class GerenciadorPessoas:
    def __init__(self, conexao):
        self.conexao = conexao

    def adicionar_cliente(self, cliente):
        try:
            self.conexao.cursor().execute("INSERT INTO pessoas (nome, cpf, email) VALUES(%s, %s, %s)",
                                          (cliente.nome, cliente.cpf, cliente.email))
            self.conexao.cursor().execute("INSERT INTO clientes (cpf, time_do_coracao, obra_favorita, cidade_natal) VALUES(%s, %s, %s, %s)",
                                          (cliente.cpf, cliente.time, cliente.obra_favorita, cliente.cidade_natal))
            self.conexao.commit()
            print("Dados inseridos com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)

    def adicionar_vendedor(self, vendedor):
        try:
            self.conexao.cursor().execute("INSERT INTO pessoas (nome, cpf, email) VALUES(%s, %s, %s)",
                                          (vendedor.nome, vendedor.cpf, vendedor.email))
            self.conexao.cursor().execute("INSERT INTO funcionarios (cpf, matricula) VALUES(%s, %s)",
                                          (vendedor.cpf, vendedor.matricula))
            self.conexao.commit()
            print("Dados inseridos com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)

    def pesquisar_cliente(self, nome):
        try:
            with self.conexao.cursor() as cursor:
                if nome:
                    cursor.execute(
                        "SELECT * FROM view_clientes WHERE nome ILIKE %s", (f"%{nome}%",))
                else:
                    cursor.execute(
                        "SELECT * FROM view_clientes")
                clientes = cursor.fetchall()
                return clientes
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar clientes:", error)

    def pesquisar_vendedor(self, nome):
        try:
            with self.conexao.cursor() as cursor:
                if nome:
                    cursor.execute(
                        "SELECT * FROM view_funcionarios WHERE nome ILIKE %s", (f"%{nome}%",))
                else:
                    cursor.execute(
                        "SELECT * FROM view_funcionarios")
                funcionarios = cursor.fetchall()
                return funcionarios
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar funcionarios:", error)

    def remover_cliente(self, cpf):
        try:
            self.conexao.cursor().execute(
                "DELETE FROM pessoas WHERE cpf = %s", (cpf,))
            self.conexao.cursor().execute(
                "DELETE FROM clientes WHERE cpf = %s", (cpf,))
            self.conexao.commit()
            print("Cliente removido com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao remover cliente:", error)

    def remover_vendedor(self, cpf):
        try:
            self.conexao.cursor().execute(
                "DELETE FROM pessoas WHERE cpf = %s", (cpf,))
            self.conexao.cursor().execute(
                "DELETE FROM funcionarios WHERE cpf = %s", (cpf,))
            self.conexao.commit()
            print("Funcionario removido com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao remover funcionario:", error)

    def alterar_cliente(self, cpf, novo_nome, novo_email, novo_time, nova_obra_favorita, nova_cidade_natal):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "UPDATE pessoas SET nome = %s, email = %s WHERE cpf = %s", (novo_nome, novo_email, cpf))
                cursor.execute("UPDATE clientes SET time_do_coracao = %s, obra_favorita = %s, cidade_natal = %s WHERE cpf = %s", (
                    novo_time, nova_obra_favorita, nova_cidade_natal, cpf,))
                self.conexao.commit()
                print("Cliente alterado com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao alterar cliente:", error)

    def alterar_vendedor(self, cpf, novo_nome, novo_email, nova_matricula):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "UPDATE pessoas SET nome = %s, email = %s WHERE cpf = %s", (novo_nome, novo_email, cpf,))
                cursor.execute(
                    "UPDATE funcionarios SET matricula = %s WHERE cpf = %s", (nova_matricula, cpf,))
                self.conexao.commit()
                print("Funcionario alterado com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao alterar funcionario:", error)


class Venda:
    def __init__(self, cpf_vendedor, cpf_cliente, id_venda, quantidade, total, metodo_pagamento, status_pagamento, data):
        self.cpf_vendedor = cpf_vendedor
        self.cpf_cliente = cpf_cliente
        self.id_venda = id_venda
        self.quantidade = quantidade
        self.total = total
        self.metodo_pagamento = metodo_pagamento
        self.status_pagamento = status_pagamento
        self.data = data


class GerenciadorVendas:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_venda(self, venda):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("INSERT INTO vendas (vendedor, cliente, quantidade, total, metodo_pagamento, status_pagamento, data) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING id_venda",
                               (venda.cpf_vendedor, venda.cpf_cliente, venda.quantidade, venda.total, venda.metodo_pagamento, venda.status_pagamento, venda.data))
                id_venda = cursor.fetchone()[0]

                self.conexao.commit()
                print("Dados inseridos com sucesso.")
                return id_venda
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)

    def inserir_item_venda(self, id_venda, isbn, quantidade, preco, desconto):
        try:
            if (desconto):
                self.conexao.cursor().execute("INSERT INTO itens_vendidos (id_venda, isbn, quantidade, preco, desconto) VALUES(%s, %s, %s, %s, %s)",
                                              (id_venda, isbn, quantidade, preco, "s"))
            else:
                self.conexao.cursor().execute("INSERT INTO itens_vendidos (id_venda, isbn, quantidade, preco, desconto) VALUES(%s, %s, %s, %s, %s)",
                                              (id_venda, isbn, quantidade, preco, "n"))
            self.conexao.commit()
            print("Dados inseridos com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)

    def computa_venda_estoque(self, isbn, quantidade_estoque, quantidade_venda):
        try:
            self.conexao.cursor().execute("UPDATE estoque SET quantidade = %s WHERE isbn = %s",
                                          (quantidade_estoque - quantidade_venda, isbn))
            self.conexao.commit()
            print("Dados inseridos com sucesso.")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados:", error)

    def exibir_vendas(self):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM view_vendas")
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None

    def exibir_vendas_cliente(self, cpf_cliente):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM view_vendas WHERE cpf_cliente = %s", (cpf_cliente,))
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None

    def exibir_itens_vendidos(self, id_venda):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM view_itens_vendidos WHERE id_venda = %s", (id_venda,))
                return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Erro ao recuperar dados:", error)
            return None


# # Função para exibir o menu


def print_manga(mangas):
    if mangas == None:
        pass
    elif mangas == []:
        print("Sua pesquisa retornou uma lista vazia.")
    else:
        print("Títulos encontrados:")
        header = ["ISBN", "Título", "Autor", "Volume", "Preço",
                  "Quantidade", "Categoria", "Local de fabricação"]
        print(tabulate(mangas, headers=header))


def exibir_menu_estoque(conexao, admin):
    estoque = EstoqueMangas(conexao)

    while True:
        if admin:
            print("\nMenu Estoque:")
            print("1. Adicionar mangá")
            print("2. Alterar mangá")
            print("3. Pesquisar mangá")
            print("4. Remover mangá")
            print("5. Listar estoque")
            print("6. Exibir estoque baixo")
            print("7. Exibir títulos de Mari")
            print("8. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                isbn = input("ISBN: ")
                titulo = input("Título: ")
                volume = input("Volume: ")
                autor = input("Autor: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                categoria = input("Categoria: ")
                local_fab = input("Local de fabricação: ")

                manga = Manga(isbn, titulo, volume, autor, preco,
                              quantidade, categoria, local_fab)
                estoque.adicionar_manga(manga)
            elif opcao == "2":
                data_with_index = []
                print("Digite o título do mangá que deseja alterar.")
                nome = input("Título: ")
                if nome:
                    titulos = estoque.pesquisar_manga(nome)
                    if titulos == []:
                        print("Título não encontrado.")
                        continue

                    for i, titulo in enumerate(titulos, 1):
                        data_with_index.append(
                            (i,) + titulo)

                    print(tabulate(data_with_index, headers=["ID", "ISBN", "Título", "Autor", "Volume", "Preço",
                                                             "Quantidade", "Categoria", "Local de fabricação"]))

                    print("Digite o id do mangá que deseja alterar.")
                    id = input("ID: ")
                    if id:
                        id = int(id)
                    else:
                        print("ID inválido")
                        continue

                    if id > len(titulos) or id < 1:
                        print('Entrada inválida')
                        continue

                    print(
                        "Digite os novos dados do mangá. Deixe em branco para não alterar")
                    novo_titulo = input("titulo: ")
                    novo_autor = input("autor: ")
                    novo_volume = input("volume: ")
                    novo_preco = input("preco: ")
                    nova_quantidade = input("quantidade: ")
                    nova_categoria = input("categoria: ")
                    novo_local_fab = input("local de fabricação: ")

                    novo_titulo = novo_titulo if novo_titulo else titulos[id-1][1]
                    novo_autor = novo_autor if novo_autor else titulos[id-1][2]
                    novo_volume = novo_volume if novo_volume else titulos[id-1][3]
                    novo_preco = novo_preco if novo_preco else titulos[id-1][4]
                    nova_quantidade = nova_quantidade if nova_quantidade else titulos[id-1][5]
                    nova_categoria = nova_categoria if nova_categoria else titulos[id-1][6]
                    novo_local_fab = novo_local_fab if novo_local_fab else titulos[id-1][7]

                    estoque.alterar_manga(
                        titulos[id-1][0], Manga(titulos[id-1][0], novo_titulo, novo_volume, novo_autor, novo_preco, nova_quantidade, nova_categoria, novo_local_fab))
                else:
                    print("Título não informado.")
            elif opcao == "3":
                print("\nMenu de pesquisa:")
                print("1. Pesquisar por título")
                print("2. Pesquisar por preço")
                print("3. Voltar")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    titulo = input("Título: ")
                    print_manga(estoque.pesquisar_manga(titulo))
                elif opcao == "2":
                    p1 = float(input("limite inferior de preço: "))
                    if p1 < 0:
                        print("valor inválido")
                        continue

                    p2 = float(input("limite superior de preço: "))
                    if p2 < 0:
                        print("valor inválido")
                        continue

                    print_manga(estoque.exibir_estoque_faixa_preco(p1, p2))
                else:
                    continue
            elif opcao == "4":
                print("Digite o título do mangá que deseja remover.")
                nome = input("Título: ")
                if nome:
                    titulos = estoque.pesquisar_manga(nome)
                    if titulos == []:
                        print("Título não encontrado.")
                        continue

                    data_with_index = []
                    for i, titulo in enumerate(titulos, 1):
                        data_with_index.append(
                            (i,) + titulo)

                    print(tabulate(data_with_index, headers=["ID", "ISBN", "Título", "Autor", "Volume", "Preço",
                                                             "Quantidade", "Categoria", "Local de fabricação"]))

                    print("Digite o id do mangá que deseja remover.")
                    id = input("ID: ")
                    if id:
                        id = int(id)
                    else:
                        print("ID inválido")
                        continue

                    if id > len(titulos) or id < 1:
                        print('Entrada inválida')
                        continue

                    estoque.remover_manga(titulos[id-1][0])
                else:
                    print("Título não informado.")
            elif opcao == "5":
                print_manga(estoque.exibir_estoque())
            elif opcao == "6":
                print_manga(estoque.exibir_estoque_baixo())
            elif opcao == "7":
                print_manga(estoque.exibir_estoque_Mari())
            elif opcao == "8":
                break
        else:
            print("\nMenu Estoque:")
            print("1. Pesquisar mangá")
            print("2. Listar estoque")
            print("3. Exibir títulos de Mari")
            print("4. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("\nMenu de pesquisa:")
                print("1. Pesquisar por título")
                print("2. Pesquisar por preço")
                print("3. Voltar")

                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    titulo = input("Título: ")
                    print_manga(estoque.pesquisar_manga(titulo))
                elif opcao == "2":
                    p1 = float(input("limite inferior de preço: "))
                    if p1 < 0:
                        print("valor inválido")
                        continue

                    p2 = float(input("limite superior de preço: "))
                    if p2 < 0:
                        print("valor inválido")
                        continue

                    print_manga(estoque.exibir_estoque_faixa_preco(p1, p2))
                else:
                    continue
            elif opcao == "2":
                print_manga(estoque.exibir_estoque())
            elif opcao == "3":
                print_manga(estoque.exibir_estoque_Mari())
            elif opcao == "4":
                break


def exibir_menu_pessoas(conexao):
    gerenciador_pessoas = GerenciadorPessoas(conexao)
    while True:
        print("\nMenu de pessoas:")

        print("1. Adicionar cliente")
        print("2. Adcicionar funcionário")
        print("3. Pesquisar cliente")
        print("4. Pesquisar funcionário")
        print("5. Remover cliente")
        print("6. Remover funcionario")
        print("7. Alterar cliente")
        print("8. Alterar funcionario")
        print("9. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            time = input("Time do coração: ")
            obra_favorita = input("Obra favorita: ")
            cidade_natal = input("Cidade natal: ")
            cliente = Cliente(nome, email, cpf, time,
                              obra_favorita, cidade_natal)
            gerenciador_pessoas.adicionar_cliente(cliente)
        elif opcao == "2":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            matricula = input("Matrícula: ")
            vendedor = Vendedor(nome, email, cpf, matricula)
            gerenciador_pessoas.adicionar_vendedor(vendedor)
        elif opcao == "3":
            print("Para listar todos, basta não informar o nome.")
            nome = input("Nome: ")
            clientes = gerenciador_pessoas.pesquisar_cliente(nome)
            if clientes == []:
                print("Cliente não encontrado.")
                continue

            data_with_index = []
            for i, titulo in enumerate(clientes, 1):
                data_with_index.append(
                    (i,) + titulo)

            print(tabulate(data_with_index, headers=["ID", "Nome", "CPF", "Email", "Time", "Obra Favorita",
                                                     "Cidade Natal"]))
        elif opcao == "4":
            print("Para listar todos, basta não informar o nome.")
            nome = input("Nome: ")
            vendedores = gerenciador_pessoas.pesquisar_vendedor(nome)
            data_with_index = []
            for i, titulo in enumerate(vendedores, 1):
                data_with_index.append(
                    (i,) + titulo)

            print(tabulate(data_with_index, headers=[
                  "ID", "Nome", "CPF", "Email", "Matrícula"]))

        elif opcao == "5":
            print("Digite o nome do cliente que deseja remover.")
            nome = input("Nome: ")
            if nome:
                clientes = gerenciador_pessoas.pesquisar_cliente(nome)
                if clientes == []:
                    print("Cliente não encontrado.")
                    continue

                data_with_index = []
                for i, titulo in enumerate(clientes, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=["ID", "Nome", "CPF", "Email", "Time", "Obra Favorita",
                                                         "Cidade Natal"]))

                print("Digite o id do cliente que deseja remover.")
                id = input("ID: ")
                if id:
                    id = int(id)
                else:
                    print("ID inválido")
                    continue
                if clientes:
                    gerenciador_pessoas.remover_cliente(clientes[id-1][1])
                else:
                    print("Cliente não encontrado.")
            else:
                print("Nome não informado.")
        elif opcao == "6":
            print("Digite o nome do vendedor que deseja remover.")
            nome = input("Nome: ")
            if nome:
                vendedores = gerenciador_pessoas.pesquisar_vendedor(nome)
                if vendedores == []:
                    print("Vendedor não encontrado.")
                    continue
                data_with_index = []
                for i, titulo in enumerate(vendedores, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=[
                    "ID", "Nome", "CPF", "Email", "Matrícula"]))
                print("Digite o id do vendedor que deseja remover.")
                id = input("ID: ")
                if id:
                    id = int(id)
                else:
                    print("ID inválido")
                    continue
                if vendedores and vendedores[id-1][0] == nome:
                    gerenciador_pessoas.remover_vendedor(vendedores[id-1][1])
                else:
                    print("Vendedor não encontrado.")
            else:
                print("Nome não informado.")
        elif opcao == "7":
            print("Digite o nome do cliente que deseja alterar.")
            nome = input("Nome: ")
            if nome:
                clientes = gerenciador_pessoas.pesquisar_cliente(nome)
                if clientes == []:
                    print("Cliente não encontrado.")
                    continue

                data_with_index = []
                for i, titulo in enumerate(clientes, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=["ID", "Nome", "CPF", "Email", "Time", "Obra Favorita",
                                                         "Cidade Natal"]))
                print("Digite o id do cliente que deseja alterar.")
                id = input("ID: ")
                if id:
                    id = int(id)
                else:
                    print("ID inválido")
                    continue
                if id > len(clientes) or id < 1:
                    print('Entrada inválida')
                    continue

                print(
                    "Digite os novos dados do cliente. Deixe em branco para não alterar")
                novo_nome = input("Nome: ")
                novo_email = input("Email: ")
                novo_time = input("Time do coração: ")
                nova_obra_favorita = input("Obra favorita: ")
                nova_cidade_natal = input("Cidade natal: ")
                novo_nome = novo_nome if novo_nome else clientes[id-1][0]
                novo_email = novo_email if novo_email else clientes[id-1][2]
                novo_time = novo_time if novo_time else clientes[id-1][3]
                nova_obra_favorita = nova_obra_favorita if nova_obra_favorita else clientes[
                    id-1][4]
                nova_cidade_natal = nova_cidade_natal if nova_cidade_natal else clientes[
                    id-1][5]

                gerenciador_pessoas.alterar_cliente(
                    clientes[id-1][1], novo_nome, novo_email, novo_time, nova_obra_favorita, nova_cidade_natal)
            else:
                print("Nome não informado.")
        elif opcao == "8":
            print("Digite o nome do funcionario que deseja alterar.")
            nome = input("Nome: ")
            if nome:
                vendedores = gerenciador_pessoas.pesquisar_vendedor(nome)
                if vendedores == []:
                    print("Vendedor não encontrado.")
                    continue

                data_with_index = []
                for i, titulo in enumerate(vendedores, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=[
                    "ID", "Nome", "CPF", "Email", "Matrícula"]))
                print("Digite o id do vendedor que deseja alterar.")

                id = input("ID: ")
                if id:
                    id = int(id)
                else:
                    print("ID inválido")
                    continue
                if id > len(vendedores) or id < 1:
                    print('Entrada inválida')
                    continue

                print(
                    "Digite os novos dados do funcionario. Deixe em branco para não alterar")
                novo_nome = input("Nome: ")
                novo_email = input("Email: ")
                nova_matricula = input("Matrícula: ")
                novo_nome = novo_nome if novo_nome else vendedores[id-1][0]
                novo_email = novo_email if novo_email else vendedores[id-1][2]
                nova_matricula = nova_matricula if nova_matricula else vendedores[id-1][3]

                gerenciador_pessoas.alterar_vendedor(
                    vendedores[id-1][1], novo_nome, novo_email, nova_matricula)
            else:
                print("Nome não informado.")
        elif opcao == "9":
            break


def exibir_menu_vendas(conexao,  admin):
    gerenciador_pessoas = GerenciadorPessoas(conexao)
    gerenciador_estoque = EstoqueMangas(conexao)
    gerenciador_vendas = GerenciadorVendas(conexao)
    while True:
        if admin:
            print("\nMenu Vendas:")
            print("1. Realizar venda")
            print("2. Exibir vendas")
            print("3. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                mangas_vendidos = []

                print("Digite o nome do funcionario vai realizar a venda.")
                nome_funcionario = input("Nome do funcionario: ")
                vendedores = gerenciador_pessoas.pesquisar_vendedor(
                    nome_funcionario)

                if vendedores == []:
                    print("Vendedor não encontrado.")
                    continue

                data_with_index = []
                for i, titulo in enumerate(vendedores, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=[
                    "ID", "Nome", "CPF", "Email", "Matrícula"]))
                print("Digite o id do vendedor que irá vender.")
                id_funcionario = int(input("ID: "))-1
                print("Digite o nome do cliente que está comprando.")
                nome_cliente = input("Nome do cliente: ")
                clientes = gerenciador_pessoas.pesquisar_cliente(nome_cliente)
                if clientes == []:
                    print("Cliente não encontrado.")
                    continue

                data_with_index = []
                for i, titulo in enumerate(clientes, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=["ID", "Nome", "CPF", "Email", "Time", "Obra Favorita",
                                                         "Cidade Natal"]))
                print("Digite o id do cliente que deseja comprar.")

                id_cliente = input("ID: ")
                if id_cliente:
                    id_cliente = int(id_cliente)-1
                else:
                    print("ID inválido")
                    continue
                if (clientes[id_cliente][3] == 'Flamengo' or clientes[id_cliente][4] == 'One Piece' or clientes[id_cliente][5] == 'Sousa'):
                    desconto = True
                else:
                    desconto = False
                while True:
                    manga = input("Título do mangá: ")
                    mangas = gerenciador_estoque.pesquisar_manga(manga)
                    if mangas == []:
                        print("Cliente não encontrado.")
                        continue

                    data_with_index = []
                    for i, titulo in enumerate(mangas, 1):
                        data_with_index.append(
                            (i,) + titulo)

                    print(tabulate(data_with_index, headers=["ID", "ISBN", "Título", "Autor", "Volume", "Preço",
                                                             "Quantidade", "Categoria", "Local de fabricação"]))
                    print("Digite o id do mangá que deseja realizar a venda.")

                    id_manga = input("ID: ")
                    if id_manga:
                        id_manga = int(id_manga)-1
                    else:
                        print("ID inválido")
                        continue

                    print("Digite a quantidade.")
                    quantidade = int(input("Quantidade: "))
                    if (desconto):
                        mangas_vendidos.append((
                            mangas[id_manga][0], mangas[id_manga][1], mangas[id_manga][2], mangas[id_manga][3], mangas[id_manga][4]*0.9, mangas[id_manga][6], mangas[id_manga][7], quantidade))
                    else:
                        mangas_vendidos.append((
                            mangas[id_manga][0], mangas[id_manga][1], mangas[id_manga][2], mangas[id_manga][3], mangas[id_manga][4], mangas[id_manga][6], mangas[id_manga][7], quantidade))
                    continuar = input("Deseja adicionar mais mangás? (s/n)")
                    if continuar == "n":
                        break
                while True:
                    metodo_de_pagamento = input(
                        "Digite o método de pagamento: ")
                    if (metodo_de_pagamento == 'pix' or metodo_de_pagamento == 'cartao' or metodo_de_pagamento == 'boleto' or metodo_de_pagamento == 'berries'):
                        if (random.randint(1, 3) % 2):
                            status_pagamento = "Pagamento pendente"
                            break
                        else:
                            status_pagamento = "Pagamento aprovado"
                            break
                    elif (metodo_de_pagamento == 'dinheiro'):
                        status_pagamento = "Pagamento aprovado"
                        break
                    else:
                        status_pagamento = "Método de pagamento inválido"

                while True:
                    data = input("digite a data da venda (dd/mm/aaaa): ")
                    if data:
                        data = int(''.join(reversed(data.split("/"))))
                        break

                venda = Venda(vendedores[id_funcionario][1], clientes[id_cliente][1], None, sum([manga[7] for manga in mangas_vendidos]), sum(
                    [manga[4]*manga[7] for manga in mangas_vendidos]), metodo_de_pagamento, status_pagamento, data)
                quantidade_insuficiente = False
                for manga in mangas:
                    for manga_vendido in mangas_vendidos:
                        if manga[0] == manga_vendido[0]:
                            if manga[5] < manga_vendido[7]:
                                quantidade_insuficiente = True
                                print(
                                    f"Não foi possível realizar a venda. Quantidade insuficiente de {manga[1]}")
                                break
                            gerenciador_vendas.computa_venda_estoque(
                                manga[0], manga[5], manga_vendido[7])
                if not quantidade_insuficiente:
                    id_venda = gerenciador_vendas.inserir_venda(venda)
                    for manga in mangas_vendidos:
                        gerenciador_vendas.inserir_item_venda(
                            id_venda, manga[0], manga[7], manga[4], desconto)

            if opcao == "2":
                vendas = gerenciador_vendas.exibir_vendas()
                if vendas == []:
                    print("Não há vendas")
                    continue

                data_with_index = []
                for i, titulo in enumerate(vendas, 1):
                    data_with_index.append(
                        (i,) + titulo[1:7])

                print(tabulate(data_with_index, headers=["ID", "Cliente", "Vendedor", "Quantidade", "Total", "Método de pagamento",
                                                         "Status de pagamento"]))

                id = input("ID: ")
                if id:
                    id = int(id)-1
                else:
                    print("ID inválido")
                    continue

                itens_vendidos = gerenciador_vendas.exibir_itens_vendidos(
                    vendas[id][0])

                for i in range(len(itens_vendidos)):
                    itens_vendidos[i] = itens_vendidos[i][1:]

                print(tabulate(itens_vendidos, [
                    "Mangá", "Quantidade", "Preço", "Volume"
                ]))
            if opcao == "3":
                break
        else:
            print("\nMenu Compra:")
            print("1. Visualizar compras")
            print("2. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Digite o nome do cliente que deseja ver suas compras.")
                nome_cliente = input("Nome do cliente: ")
                clientes = gerenciador_pessoas.pesquisar_cliente(nome_cliente)

                if clientes == []:
                    print("Cliente não encontrado.")
                    continue

                data_with_index = []
                for i, titulo in enumerate(clientes, 1):
                    data_with_index.append(
                        (i,) + titulo)

                print(tabulate(data_with_index, headers=["ID", "Nome", "CPF", "Email", "Time", "Obra Favorita",
                                                         "Cidade Natal"]))
                print("Digite o id do cliente que deseja ver suas compras.")

                id_cliente = input("ID: ")
                if id_cliente:
                    id_cliente = int(id_cliente)-1
                else:
                    print("ID inválido")
                    continue

                vendas_cliente = gerenciador_vendas.exibir_vendas_cliente(
                    clientes[id_cliente][1])

                data_with_index = []
                for i, titulo in enumerate(vendas_cliente, 1):
                    data_with_index.append(
                        (i,) + titulo[1:7])

                print(tabulate(data_with_index, headers=["ID", "Cliente", "Vendedor", "Quantidade", "Total", "Método de pagamento",
                                                         "Status de pagamento"]))

                id = input("ID: ")
                if id:
                    id = int(id)-1
                else:
                    print("ID inválido")
                    continue
                itens_vendidos = gerenciador_vendas.exibir_itens_vendidos(
                    vendas_cliente[id][0])

                for i in range(len(itens_vendidos)):
                    itens_vendidos[i] = itens_vendidos[i][1:]

                print(tabulate(itens_vendidos, [
                    "Mangá", "Quantidade", "Preço", "Volume"
                ]))
            if opcao == "2":
                break


def exibir_menu_relatorios(conexao):
    relatorio = Relatorio(conexao)
    gerenciador_pessoas = GerenciadorPessoas(conexao)

    while True:
        print("Menu de relatórios:")
        print("1. Relatório de vendas")
        print("2. Relatório de estoque")
        print("3. Relatório de clientes")
        print("4. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("1. Relatório geral")
            print("2. Relatório por vendedor")
            opcao_relatorio = input("Escolha uma opção: ")
            if opcao_relatorio == "1":
                relatorio_vendas = relatorio.vendas(None, None, None)
                for linha in relatorio_vendas:
                    print(linha)
            elif opcao_relatorio == "2":
                vendedores = gerenciador_pessoas.pesquisar_vendedor(None)

                data_with_index = []
                for i, titulo in enumerate(vendedores, 1):
                    data_with_index.append(
                        (i,) + titulo)
                print(tabulate(data_with_index, headers=[
                    "ID", "Nome", "CPF", "Email", "Matrícula"]))
                print("Digite o id do vendedor que deseja ver o relatorio.")
                id_funcionario = int(input("ID: "))-1
                print("Digite o limite inferior da data: ")
                data_inferior = int(
                    ''.join(reversed(input("Data: ").split("/"))))
                print("Digite o limite superior da data: ")
                data_superior = int(
                    ''.join(reversed(input("Data: ").split("/"))))

                relatorio_vendas = relatorio.vendas(
                    vendedores[id_funcionario][1], data_inferior, data_superior)
                for linha in relatorio_vendas:
                    print(linha)
        elif opcao == "2":
            relatorio_estoque = relatorio.estoque()
            for linha in relatorio_estoque:
                print(linha)
        elif opcao == "3":
            relatorio_cliente = relatorio.clientes()
            for linha in relatorio_cliente:
                print(linha)
        elif opcao == "4":
            break


def exibir_menu_principal(conexao):
    while True:
        print("\nBem vindo ao sistema de gerenciamento!")
        print(
            "Você é um (\033[32mC\033[0m)liente ou um (\033[36mV\033[0m)endedor?")
        print("(\033[31mF\033[0m) para fechar")
        opcao = input("Escolha uma opção: ")

        if opcao == "v" or opcao == "V":

            senha = input("Qual a senha? ")

            if senha != "1":
                print("senha incorreta.")
                continue
            while True:
                print("\nO que você deseja acessar?")
                print("1. Estoque")
                print("2. Gerenciamento de pessoas")
                print("3. Vendas")
                print("4. Relatorios")
                print("5. Sair")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    exibir_menu_estoque(conexao, True)
                elif opcao == "2":
                    exibir_menu_pessoas(conexao)
                elif opcao == "3":
                    exibir_menu_vendas(conexao, True)
                elif opcao == "4":
                    exibir_menu_relatorios(conexao)
                elif opcao == "5":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "c" or opcao == "C":
            while True:
                print("\nO que você deseja acessar?")
                print("1. Estoque")
                print("2. Vendas")
                print("3. Sair")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    exibir_menu_estoque(conexao, False)
                elif opcao == "2":
                    exibir_menu_vendas(conexao, False)
                elif opcao == "3":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "f" or opcao == "F":
            print("Fechando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# # Função principal


def main():
    conexao = conectar()
    if not conexao:
        return

    exibir_menu_principal(conexao)
    conexao.close()


if __name__ == "__main__":
    main()
