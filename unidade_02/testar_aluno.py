# Atividade: Aula 02 (Classes e Objetos) - Questao 2: Programa de Teste

from aluno import Aluno

lista_alunos = []

print("--- Leitura de Alunos (Pressione ENTER no nome para finalizar) ---")
while True:
    nome_lido = input("Digite o nome do aluno: ").strip()
    if nome_lido == "":
        break
    matricula_lida = input("Digite a matrícula: ").strip()
    aluno_obj = Aluno(nome_lido, matricula_lida)
    lista_alunos.append(aluno_obj)

# Atribuindo notas e faltas diretamente aos objetos (deixando ao menos um sem notas)
if len(lista_alunos) >= 1:
    lista_alunos[0].notas.append(9.0)
    lista_alunos[0].notas.append(8.0)
    lista_alunos[0].faltas += 3

if len(lista_alunos) >= 3:
    lista_alunos[1].notas.append(6.5)
    lista_alunos[1].notas.append(7.5)
    lista_alunos[1].faltas += 5
    # O terceiro aluno (lista_alunos[2]) permanece com a lista de notas vazia []
elif len(lista_alunos) == 2:
    lista_alunos[1].faltas += 5

print()
campeao_faltas = None

for a in lista_alunos:
    print(f"{a.nome} ({a.matricula})")
    print(f"Notas: {a.notas}")
    print(f"Faltas: {a.faltas}")

    if len(a.notas) > 0:
        media_aluno = sum(a.notas) / len(a.notas)
        print(f"Média: {media_aluno:.2f}\n")
    else:
        print("Média: sem notas\n")

    if campeao_faltas is None or a.faltas > campeao_faltas.faltas:
        campeao_faltas = a

if campeao_faltas is not None:
    print(f"Mais faltas: {campeao_faltas.nome} ({campeao_faltas.faltas})")