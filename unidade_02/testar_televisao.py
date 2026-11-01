# Disciplina: Programacao Orientada a Objetos - IFCE Campus Maranguape
# Aluna: Ana Maria Alves
# Atividade: Aula 02 (Classes e Objetos) - Questao 1: Programa de Teste

from televisao import Televisao

# Instanciando televisores de marcas diferentes e armazenando na lista
lista_tvs = [
    Televisao("Sony", 55),
    Televisao("TCL", 40),
    Televisao("AOC", 32),
    Televisao("Panasonic", 65),
]

# Modificando diretamente os atributos de cada objeto
lista_tvs[0].ligada = True
lista_tvs[0].canal = 8
lista_tvs[0].volume = 35

lista_tvs[1].ligada = True
lista_tvs[1].canal = 21
lista_tvs[1].volume = 50

# lista_tvs[2] (AOC 32") permanece desligada

lista_tvs[3].ligada = True
lista_tvs[3].canal = 45
lista_tvs[3].volume = 60

# Exibindo os dados de cada televisor da lista
for item in lista_tvs:
    if item.ligada:
        print(
            f'{item.marca} {item.polegadas}" | Ligada | '
            f"Canal {item.canal} | Volume {item.volume}"
        )
    else:
        print(f'{item.marca} {item.polegadas}" | Desligada')

# Contagem de ligados, busca do maior televisor e calculo da media
total_ligadas = 0
total_polegadas = 0
maior_televisor = None

for item in lista_tvs:
    if item.ligada:
        total_ligadas += 1

    total_polegadas += item.polegadas

    if maior_televisor is None or item.polegadas > maior_televisor.polegadas:
        maior_televisor = item

media = total_polegadas / len(lista_tvs)

print(f"\nTelevisores ligados: {total_ligadas}")
print(f'Maior televisor: {maior_televisor.marca} {maior_televisor.polegadas}"')
print(f"Média de polegadas: {media:.2f}")