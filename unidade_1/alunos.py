# Atividade: Revisão de Algoritmos (Aula 01) - Questão 2: Cadastro de Alunos e Notas


def exibir_menu():
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir médias")
    print("0 - Sair")


def solicitar_nome_aluno(mensagem):
    while True:
        nome = input(mensagem).strip().title()
        if nome:
            return nome
        print("O nome do aluno não pode ficar em branco.")


def ler_nota(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            nota = float(texto)
            if 0 <= nota <= 10:
                return nota
            print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Informe um número real (ex: 8.5).")


def ler_quatro_notas():
    lista_notas = []
    for indice in range(1, 5):
        nota = ler_nota(f"Informe a nota N{indice}: ")
        lista_notas.append(nota)
    return lista_notas


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print(
            f"O(A) aluno(a) '{nome}' já está cadastrado(a). "
            "Use a opção 2 (Atualizar notas) caso deseje alterar as notas."
        )
        return False
    alunos[nome] = notas
    print(f"Aluno(a) '{nome}' adicionado(a) com sucesso.")
    return True


def atualizar_notas(alunos, nome, notas):
    if nome in alunos:
        alunos[nome] = notas
        print(f"Notas do(a) aluno(a) '{nome}' atualizadas com sucesso.")
        return True
    print("Aluno não encontrado.")
    return False


def remover_aluno(alunos, nome):
    if nome in alunos:
        alunos.pop(nome)
        print(f"Aluno(a) '{nome}' removido(a) do cadastro.")
        return True
    print("Aluno não encontrado.")
    return False


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_alunos(alunos):
    if not alunos:
        print("\nNenhum aluno cadastrado")
        return
    print("\n--- RELAÇÃO DE ALUNOS E NOTAS ---")
    for nome, notas in alunos.items():
        print(
            f"{nome}: N1={notas[0]:.1f} | N2={notas[1]:.1f} | "
            f"N3={notas[2]:.1f} | N4={notas[3]:.1f}"
        )


def exibir_medias(alunos):
    if not alunos:
        print("\nNenhum aluno cadastrado")
        return
    print("\n--- MÉDIAS FINAIS ---")
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: {media:.2f}")


def main():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5],
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = solicitar_nome_aluno("Nome do aluno: ")
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)
        elif opcao == "2":
            nome = solicitar_nome_aluno("Nome do aluno para atualizar: ")
            notas = ler_quatro_notas()
            atualizar_notas(alunos, nome, notas)
        elif opcao == "3":
            nome = solicitar_nome_aluno("Nome do aluno para remover: ")
            remover_aluno(alunos, nome)
        elif opcao == "4":
            exibir_alunos(alunos)
        elif opcao == "5":
            exibir_medias(alunos)
        elif opcao == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida! Escolha entre 0 e 5.")


if __name__ == "__main__":
    main()