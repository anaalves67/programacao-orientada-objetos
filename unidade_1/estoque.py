# Atividade: Revisão de Algoritmos (Aula 01) - Questão 1: Estoque de Produtos


def exibir_menu():
    print("\n===== ESTOQUE DA LOJA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


def ler_quantidade(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            qtd = int(valor)
            if qtd >= 0:
                return qtd
            print("Valor inválido! Informe uma quantidade inteira maior ou igual a 0.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def solicitar_nome_produto(mensagem):
    while True:
        nome = input(mensagem).strip().title()
        if nome:
            return nome
        print("O nome do produto não pode ser vazio. Digite novamente.")


def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print(
            f"O produto '{nome}' já está cadastrado. "
            "Use a opção 3 (Atualizar quantidade) para modificar o estoque."
        )
        return False
    estoque[nome] = quantidade
    print(f"Produto adicionado com sucesso: {nome} ({quantidade} un.).")
    return True


def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso.")
        return True
    print("Produto não encontrado.")
    return False


def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Estoque de '{nome}' atualizado com sucesso para {quantidade} un.")
        return True
    print("Produto não encontrado.")
    return False


def exibir_estoque(estoque):
    if len(estoque) == 0:
        print("\nEstoque vazio")
        return
    print("\n--- LISTAGEM DO ESTOQUE ---")
    for produto, qtd in estoque.items():
        print(f"Produto: {produto} | Quantidade: {qtd}")


def main():
    estoque = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = solicitar_nome_produto("Nome do produto: ")
            qtd = ler_quantidade("Quantidade em estoque: ")
            adicionar_produto(estoque, nome, qtd)
        elif opcao == "2":
            nome = solicitar_nome_produto("Nome do produto para remover: ")
            remover_produto(estoque, nome)
        elif opcao == "3":
            nome = solicitar_nome_produto("Nome do produto para atualizar: ")
            qtd = ler_quantidade("Nova quantidade: ")
            atualizar_quantidade(estoque, nome, qtd)
        elif opcao == "4":
            exibir_estoque(estoque)
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()