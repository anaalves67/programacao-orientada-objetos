# Atividade: Revisão de Algoritmos (Aula 01) - Questão 3: Controle de Tarefas


def exibir_menu():
    print("\n===== CONTROLE DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar tarefas")
    print("0 - Sair")


def ler_texto(mensagem):
    while True:
        conteudo = input(mensagem).strip()
        if conteudo:
            return conteudo
        print("Este campo não pode ficar em branco! Digite novamente.")


def buscar_tarefa(tarefas, titulo):
    chave_busca = titulo.strip().lower()
    for item in tarefas:
        if item["titulo"].strip().lower() == chave_busca:
            return item
    return None


def adicionar_tarefa(tarefas, titulo, descricao):
    if buscar_tarefa(tarefas, titulo) is not None:
        print(f"A tarefa '{titulo}' já está cadastrada.")
        return False

    tarefa = {
        "titulo": titulo.strip(),
        "descricao": descricao.strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' cadastrada com sucesso.")
    return True


def concluir_tarefa(tarefas, titulo):
    tarefa = buscar_tarefa(tarefas, titulo)
    if tarefa is None:
        print("Tarefa não encontrada.")
        return False

    if tarefa["status"] == "Concluído":
        print(f"A tarefa '{tarefa['titulo']}' já se encontra concluída.")
        return False

    tarefa["status"] = "Concluído"
    print(f"Tarefa '{tarefa['titulo']}' marcada como concluída.")
    return True


def listar_tarefas(tarefas):
    lista_pendentes = [t for t in tarefas if t["status"] == "Pendente"]
    lista_concluidas = [t for t in tarefas if t["status"] == "Concluído"]

    print(f"\nPENDENTES ({len(lista_pendentes)})")
    if len(lista_pendentes) == 0:
        print("Nenhuma tarefa")
    else:
        for i, t in enumerate(lista_pendentes, start=1):
            print(f"{i}. {t['titulo']}: {t['descricao']}")

    print(f"\nCONCLUÍDAS ({len(lista_concluidas)})")
    if len(lista_concluidas) == 0:
        print("Nenhuma tarefa")
    else:
        for i, t in enumerate(lista_concluidas, start=1):
            print(f"{i}. {t['titulo']}: {t['descricao']}")


def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = ler_texto("Título da tarefa: ")
            descricao = ler_texto("Descrição da tarefa: ")
            adicionar_tarefa(tarefas, titulo, descricao)
        elif opcao == "2":
            titulo = ler_texto("Informe o título da tarefa concluída: ")
            concluir_tarefa(tarefas, titulo)
        elif opcao == "3":
            listar_tarefas(tarefas)
        elif opcao == "0":
            print("Encerrando o sistema de tarefas...")
            break
        else:
            print("Opção inválida! Digite uma opção entre 0 e 3.")


if __name__ == "__main__":
    main()