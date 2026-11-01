# Atividade: Aula 02 (Classes e Objetos) - Questao 2: Classe Aluno


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.faltas = 0