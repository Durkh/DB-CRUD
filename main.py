class Manga:
    def __init__(self, titulo, volume, autor, preco, quantidade):
        self.titulo = titulo
        self.volume = volume
        self.autor = autor
        self.preco = preco
        self.quantidade = quantidade


class EstoqueMangas:
    def __init__(self):
        self.mangas = []

    def adicionar_manga(self, manga):
        self.mangas.append(manga)
        print("Mangá adicionado com sucesso!")

    def pesquisar_manga(self, titulo):
        mangas_encontrados = []
        for manga in self.mangas:
            if manga.titulo.lower() == titulo.lower():
                mangas_encontrados.append(manga)
        if mangas_encontrados:
            print("Mangás encontrados:")
            for i, manga in enumerate(mangas_encontrados, 1):
                print(f"{i}. Título: {manga.titulo}, Volume: {manga.volume}, Autor: {manga.autor}, Preço: R${
                      manga.preco}, Quantidade: {manga.quantidade}")
        else:
            print("Mangá não encontrado.")
        return mangas_encontrados

    def alterar_manga(self, index, novo_manga):
        if 0 <= index < len(self.mangas):
            self.mangas[index] = novo_manga
            print("Mangá alterado com sucesso!")
        else:
            print("Índice inválido.")

    def remover_manga(self, index):
        if 0 <= index < len(self.mangas):
            del self.mangas[index]
            print("Mangá removido com sucesso!")
        else:
            print("Índice inválido.")

    def exibir_estoque(self):
        if not self.mangas:
            print("Estoque vazio.")
        else:
            print("Estoque de mangás:")
            for i, manga in enumerate(self.mangas, 1):
                print(f"{i}. Título: {manga.titulo}, Autor: {manga.autor}, Volume: {
                      manga.volume}, Preço: R${manga.preco}, Quantidade: {manga.quantidade}")


class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class GerenciadorClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente adicionado com sucesso!")

    def pesquisar_cliente(self, nome):
        clientes_encontrados = []
        for cliente in self.clientes:
            if cliente.nome.lower() == nome.lower():
                clientes_encontrados.append(cliente)
        if clientes_encontrados:
            print("Clientes encontrados:")
            for i, cliente in enumerate(clientes_encontrados, 1):
                print(f"{i}. Nome: {cliente.nome}, Email: {cliente.email}")
        else:
            print("Cliente não encontrado.")
        return clientes_encontrados

    def alterar_cliente(self, index, novo_cliente):
        if 0 <= index < len(self.clientes):
            self.clientes[index] = novo_cliente
            print("Cliente alterado com sucesso!")
        else:
            print("Índice inválido.")

    def remover_cliente(self, index):
        if 0 <= index < len(self.clientes):
            del self.clientes[index]
            print("Cliente removido com sucesso!")
        else:
            print("Índice inválido.")

    def listar_todos(self):
        if not self.clientes:
            print("Lista de clientes vazia.")
        else:
            print("Lista de clientes:")
            for i, cliente in enumerate(self.clientes, 1):
                print(f"{i}. Nome: {cliente.nome}, Email: {cliente.email}")


class Venda:
    def __init__(self, cliente, manga, volume, preco, quantidade):
        self.cliente = cliente
        self.manga = manga
        self.volume = volume
        self.quantidade = quantidade
        self.preco = preco
        self.total = preco * quantidade


class GerenciadorVendas:
    def __init__(self):
        self.vendas = []

    def realizar_venda(self, cliente, manga, volume, preco, quantidade):
        venda = Venda(cliente, manga, volume, quantidade, preco)
        self.vendas.append(venda)
        print("Venda realizada com sucesso!")

    def exibir_vendas(self):
        if not self.vendas:
            print("Nenhuma venda realizada.")
        else:
            print("Vendas realizadas:")
            total_geral = 0
            for i, venda in enumerate(self.vendas, 1):
                print(f"{i}. Cliente: {venda.cliente}, Mangá: {
                      venda.manga}, Volume: {venda.volume}, Quantidade: {venda.quantidade}, Total: R${venda.total}")
                total_geral += venda.total
            print(f"Total geral: R${total_geral}")

# Função para exibir o menu


def exibir_menu_estoque(estoque):
    while True:
        print("\nMenu Estoque:")
        print("1. Adicionar mangá")
        print("2. Alterar mangá")
        print("3. Pesquisar mangá")
        print("4. Remover mangá")
        print("5. Exibir estoque")
        print("6. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            volume = input("Volume: ")
            autor = input("Autor: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            manga = Manga(titulo, volume, autor, preco, quantidade)
            estoque.adicionar_manga(manga)
        elif opcao == "2":
            titulo = input("Título: ")
            estoque.pesquisar_manga(titulo)

            index = int(input("Índice do mangá: "))-1
            titulo = input("Título: ")
            volume = input("Volume: ")
            autor = input("Autor: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            manga = Manga(titulo, volume, autor, preco, quantidade)
            estoque.alterar_manga(index, manga)
        elif opcao == "3":
            titulo = input("Título: ")
            estoque.pesquisar_manga(titulo)
        elif opcao == "4":
            titulo = input("Título: ")
            estoque.pesquisar_manga(titulo)
            index = int(input("Índice do mangá: "))-1
            estoque.remover_manga(index)
        elif opcao == "5":
            estoque.exibir_estoque()
        elif opcao == "6":
            break


def exibir_menu_clientes(clientes):
    while True:
        print("\nMenu Clientes:")

        print("1. Adicionar cliente")
        print("2. Alterar cliente")
        print("3. Pesquisar cliente")
        print("4. Remover cliente")
        print("5. Exibir clientes")
        print("6. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            cliente = Cliente(nome, email)
            clientes.adicionar_cliente(cliente)
        elif opcao == "2":
            nome = input("Nome: ")
            clientes.pesquisar_cliente(nome)
            index = int(input("Índice do cliente: "))-1
            nome = input("Nome: ")
            email = input("Email: ")
            cliente = Cliente(nome, email)
            clientes.alterar_cliente(index, cliente)
        elif opcao == "3":
            nome = input("Nome: ")
            clientes.pesquisar_cliente(nome)
        elif opcao == "4":
            nome = input("Nome: ")
            clientes.pesquisar_cliente(nome)
            index = int(input("Índice do cliente: "))-1
            clientes.remover_cliente(index)
        elif opcao == "5":
            clientes.listar_todos()
        elif opcao == "6":
            break


def exibir_menu_vendas(vendas):
    while True:
        print("\nMenu Vendas:")
        print("1. Realizar venda")
        print("2. Exibir vendas")
        print("3. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("Nome do cliente: ")
            manga = input("Título do mangá: ")
            volume = input("Volume: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            vendas.realizar_venda(cliente, manga, volume, preco, quantidade)
        if opcao == "2":
            vendas.exibir_vendas()
        if opcao == "3":
            break


def exibir_menu_principal(estoque, clientes, vendas):
    while True:
        print("\nBem vindo ao sistema de gerenciamento!")
        print("1. Estoque")
        print("2. Clientes")
        print("3. Vendas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_menu_estoque(estoque)
        elif opcao == "2":
            exibir_menu_clientes(clientes)
        elif opcao == "3":
            exibir_menu_vendas(vendas)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função principal


def main():
    estoque = EstoqueMangas()
    clientes = GerenciadorClientes()
    vendas = GerenciadorVendas()

    estoque.adicionar_manga(
        Manga("Naruto", "1", "Masashi Kishimoto", 20.0, 10))
    estoque.adicionar_manga(
        Manga("Naruto", "2", "Masashi Kishimoto", 20.0, 10))
    estoque.adicionar_manga(
        Manga("Naruto", "3", "Masashi Kishimoto", 20.0, 10))
    estoque.adicionar_manga(Manga("One Piece", "1", "Eiichiro Oda", 25.0, 15))
    estoque.adicionar_manga(
        Manga("Dragon Ball", "1", "Akira Toriyama", 18.0, 20))
    estoque.adicionar_manga(Manga("Bleach", "1", "Tite Kubo", 22.0, 12))
    estoque.adicionar_manga(Manga("Death Note", "1", "Tsugumi Ohba", 30.0, 8))
    estoque.adicionar_manga(
        Manga("My Hero Academia", "1", "Kohei Horikoshi", 28.0, 18))
    estoque.adicionar_manga(
        Manga("Black Clover", "1", "Yūki Tabata", 26.0, 14))
    estoque.adicionar_manga(
        Manga("Demon Slayer", "1", "Koyoharu Gotouge", 32.0, 10))
    estoque.adicionar_manga(
        Manga("Attack on Titan", "1", "Hajime Isayama", 35.0, 16))
    estoque.adicionar_manga(
        Manga("The Seven Deadly Sins", "1", "Nakaba Suzuki", 24.0, 22))
    estoque.adicionar_manga(Manga("Tokyo Ghoul", "1", "Sui Ishida", 27.0, 20))

    clientes.adicionar_cliente(Cliente("João", "teste1@teste.com"))
    clientes.adicionar_cliente(Cliente("Maria", "teste2@teste.com"))
    clientes.adicionar_cliente(Cliente("Egidio", "tste3@teste.com"))

    exibir_menu_principal(estoque, clientes, vendas)


if __name__ == "__main__":
    main()
