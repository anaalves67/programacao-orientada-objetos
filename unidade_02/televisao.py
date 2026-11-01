# Atividade: Aula 02 (Classes e Objetos) - Questao 1: Classe Televisao


class Televisao:
    def __init__(self, marca, polegadas):
        self.marca = marca
        self.polegadas = polegadas
        self.ligada = False
        self.canal = 1
        self.volume = 10