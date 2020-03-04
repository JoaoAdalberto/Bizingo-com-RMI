import pygame
import numpy as np
from bolas import Bola
from triangulos import Triangulo

preto = (0, 0, 0, 255)
roxo = (128, 0, 128, 255)
vermelho = (255, 0, 0, 255)
amarelo = (255, 128, 0, 255)
verde = (0, 255, 0, 255)
branco = (255, 255, 255, 255)
brancola = (255, 255, 254, 255)
cinza = (128, 128, 128, 255)
azul = (0, 0, 255, 255)
overmelhovenceu = pygame.image.load("Vitoria_do_Vermelho.jpg")
opretovenceu = pygame.image.load("Vitoria_do_Preto.jpg")

def verifica_dentro_do_circulo(self, x, y, a, b, r):
    return (x - a) * (x - a) + (y - b) * (y - b) < r * r

class Tabuleiro():
    def __init__(self):
        self.vizinhos = []
        self.triangulos = np.array(
            [Triangulo(verde, 235, 61, 220, 99, 250, 99), Triangulo(branco, 235, 61, 265, 61, 250, 99),
             Triangulo(verde, 265, 61, 250, 99, 280, 99),
             Triangulo(branco, 295, 61, 280, 99, 265, 61), Triangulo(verde, 295, 61, 280, 99, 310, 99),  # 1 Linha
             Triangulo(verde, 220, 99, 205, 137, 235, 137), Triangulo(branco, 220, 99, 235, 137, 250, 99),
             Triangulo(verde, 250, 99, 235, 137, 265, 137),
             Triangulo(branco, 250, 99, 265, 137, 280, 99), Triangulo(verde, 280, 99, 264, 137, 295, 137),
             Triangulo(branco, 280, 99, 295, 137, 310, 99),
             Triangulo(verde, 310, 100, 295, 137, 325, 137),  # 2 Linha
             Triangulo(verde, 205, 137, 190, 175, 220, 175), Triangulo(branco, 220, 175, 205, 137, 235, 137),
             Triangulo(verde, 235, 137, 220, 175, 250, 175),
             Triangulo(branco, 250, 175, 235, 137, 265, 137), Triangulo(verde, 265, 137, 250, 175, 280, 175),
             Triangulo(branco, 280, 175, 265, 137, 295, 137),
             Triangulo(verde, 295, 137, 280, 175, 310, 175), Triangulo(branco, 310, 175, 295, 137, 325, 137),
             Triangulo(verde, 325, 137, 310, 175, 340, 175),  # 3 Linha
             Triangulo(verde, 190, 175, 175, 213, 205, 213), Triangulo(branco, 205, 213, 190, 175, 220, 175),
             Triangulo(verde, 220, 175, 205, 213, 235, 213),
             Triangulo(branco, 235, 213, 220, 175, 250, 175), Triangulo(verde, 250, 175, 235, 213, 265, 213),
             Triangulo(branco, 265, 213, 250, 175, 280, 175),
             Triangulo(verde, 280, 175, 265, 213, 295, 213), Triangulo(branco, 295, 213, 280, 175, 310, 175),
             Triangulo(verde, 310, 175, 295, 213, 325, 213),
             Triangulo(branco, 325, 213, 310, 175, 340, 175), Triangulo(verde, 340, 175, 325, 213, 355, 213),  # 4 Linha
             Triangulo(verde, 175, 213, 160, 250, 190, 250), Triangulo(branco, 190, 250, 175, 213, 205, 213),
             Triangulo(verde, 205, 213, 190, 250, 220, 250),
             Triangulo(branco, 220, 250, 205, 213, 235, 213), Triangulo(verde, 235, 213, 220, 250, 250, 250),
             Triangulo(branco, 250, 250, 235, 213, 265, 213),
             Triangulo(verde, 265, 213, 250, 250, 280, 250), Triangulo(branco, 280, 250, 265, 213, 295, 213),
             Triangulo(verde, 295, 213, 280, 250, 310, 250),
             Triangulo(branco, 310, 250, 295, 213, 325, 213), Triangulo(verde, 325, 213, 310, 250, 340, 250),
             Triangulo(branco, 340, 250, 325, 213, 355, 213), Triangulo(verde, 355, 213, 340, 250, 370, 250),  # 5Linha
             Triangulo(verde, 160, 250, 145, 288, 175, 288), Triangulo(branco, 160, 250, 190, 250, 175, 288),
             Triangulo(verde, 190, 250, 175, 288, 205, 288),
             Triangulo(branco, 190, 250, 220, 250, 205, 288), Triangulo(verde, 220, 250, 205, 288, 235, 288),
             Triangulo(branco, 220, 250, 250, 250, 235, 288),
             Triangulo(verde, 250, 250, 235, 288, 265, 288), Triangulo(branco, 250, 250, 280, 250, 265, 288),
             Triangulo(verde, 280, 250, 265, 288, 295, 288), Triangulo(branco, 280, 250, 310, 250, 295, 288),
             Triangulo(verde, 310, 250, 295, 288, 325, 288), Triangulo(branco, 310, 250, 340, 250, 325, 288),
             Triangulo(verde, 340, 250, 325, 288, 355, 288), Triangulo(branco, 340, 250, 370, 250, 355, 288),
             Triangulo(verde, 370, 250, 355, 288, 385, 288),  # 6linha
             Triangulo(verde, 145, 288, 130, 325, 160, 325), Triangulo(branco, 145, 288, 160, 325, 175, 288),
             Triangulo(verde, 175, 288, 160, 325, 190, 325), Triangulo(branco, 175, 288, 190, 325, 205, 288),
             Triangulo(verde, 205, 288, 190, 325, 220, 325), Triangulo(branco, 205, 288, 220, 325, 235, 288),
             Triangulo(verde, 235, 288, 220, 325, 250, 325), Triangulo(branco, 235, 288, 250, 325, 265, 288),
             Triangulo(verde, 265, 288, 250, 325, 280, 325), Triangulo(branco, 265, 288, 280, 325, 295, 288),
             Triangulo(verde, 295, 288, 280, 325, 310, 325), Triangulo(branco, 295, 288, 310, 325, 325, 288),
             Triangulo(verde, 325, 288, 310, 325, 340, 325), Triangulo(branco, 325, 288, 340, 325, 355, 288),
             Triangulo(verde, 355, 288, 340, 325, 370, 325), Triangulo(branco, 355, 288, 370, 325, 385, 288),
             Triangulo(verde, 385, 288, 370, 325, 400, 325),  # 7 linha
             Triangulo(verde, 130, 325, 115, 363, 145, 363), Triangulo(branco, 130, 325, 160, 325, 145, 363),
             Triangulo(verde, 160, 325, 145, 363, 175, 363), Triangulo(branco, 160, 325, 190, 325, 175, 363),
             Triangulo(verde, 190, 325, 175, 363, 205, 363), Triangulo(branco, 190, 325, 220, 325, 205, 363),
             Triangulo(verde, 220, 325, 205, 363, 235, 363), Triangulo(branco, 220, 325, 250, 325, 235, 363),
             Triangulo(verde, 250, 325, 235, 363, 265, 363), Triangulo(branco, 250, 325, 280, 325, 265, 363),
             Triangulo(verde, 280, 325, 265, 363, 295, 363), Triangulo(branco, 280, 325, 310, 325, 295, 363),
             Triangulo(verde, 310, 325, 295, 363, 325, 363), Triangulo(branco, 310, 325, 340, 325, 325, 363),
             Triangulo(verde, 340, 325, 325, 363, 355, 363), Triangulo(branco, 340, 325, 370, 325, 355, 363),
             Triangulo(verde, 370, 325, 355, 363, 385, 363), Triangulo(branco, 370, 325, 400, 325, 385, 363),
             Triangulo(verde, 400, 325, 385, 363, 415, 363),  # 8 linha
             Triangulo(verde, 115, 363, 100, 400, 130, 400), Triangulo(branco, 115, 363, 130, 400, 145, 363),
             Triangulo(verde, 145, 363, 130, 400, 160, 400), Triangulo(branco, 145, 363, 160, 400, 175, 363),
             Triangulo(verde, 175, 363, 160, 400, 190, 400), Triangulo(branco, 175, 363, 190, 400, 205, 363),
             Triangulo(verde, 205, 363, 190, 400, 220, 400), Triangulo(branco, 205, 363, 220, 400, 235, 363),
             Triangulo(verde, 235, 363, 220, 400, 250, 400), Triangulo(branco, 235, 363, 250, 400, 265, 363),
             Triangulo(verde, 265, 363, 250, 400, 280, 400), Triangulo(branco, 265, 363, 280, 400, 295, 363),
             Triangulo(verde, 295, 363, 280, 400, 310, 400), Triangulo(branco, 295, 363, 310, 400, 325, 363),
             Triangulo(verde, 325, 363, 310, 400, 340, 400), Triangulo(branco, 325, 363, 340, 400, 355, 363),
             Triangulo(verde, 355, 363, 340, 400, 370, 400), Triangulo(branco, 355, 363, 370, 400, 385, 363),
             Triangulo(verde, 385, 363, 370, 400, 400, 400), Triangulo(branco, 385, 363, 400, 400, 415, 363),
             Triangulo(verde, 415, 363, 400, 400, 430, 400),  # 9 linha
             Triangulo(branco, 115, 440, 100, 400, 130, 400), Triangulo(verde, 115, 440, 130, 400, 145, 440),
             Triangulo(branco, 145, 440, 130, 400, 160, 400), Triangulo(verde, 145, 440, 160, 400, 175, 440),
             Triangulo(branco, 175, 440, 160, 400, 190, 400), Triangulo(verde, 175, 440, 190, 400, 205, 440),
             Triangulo(branco, 205, 440, 190, 400, 220, 400), Triangulo(verde, 205, 440, 220, 400, 235, 440),
             Triangulo(branco, 235, 440, 220, 400, 250, 400), Triangulo(verde, 235, 440, 250, 400, 265, 440),
             Triangulo(branco, 265, 440, 250, 400, 280, 400), Triangulo(verde, 265, 440, 280, 400, 295, 440),
             Triangulo(branco, 295, 440, 280, 400, 310, 400), Triangulo(verde, 295, 440, 310, 400, 325, 440),
             Triangulo(branco, 325, 440, 310, 400, 340, 400), Triangulo(verde, 325, 440, 340, 400, 355, 440),
             Triangulo(branco, 355, 440, 340, 400, 370, 400), Triangulo(verde, 355, 440, 370, 400, 385, 440),
             Triangulo(branco, 385, 440, 370, 400, 400, 400), Triangulo(verde, 385, 440, 400, 400, 415, 440),
             Triangulo(branco, 415, 440, 400, 400, 430, 400),  # 10 linha
             Triangulo(branco, 115, 440, 130, 478, 145, 440),
             Triangulo(verde, 145, 440, 130, 478, 160, 478), Triangulo(branco, 145, 440, 160, 478, 175, 440),
             Triangulo(verde, 175, 440, 160, 478, 190, 478), Triangulo(branco, 175, 440, 190, 478, 205, 440),
             Triangulo(verde, 205, 440, 190, 478, 220, 478), Triangulo(branco, 205, 440, 220, 478, 235, 440),
             Triangulo(verde, 235, 440, 220, 478, 250, 478), Triangulo(branco, 235, 440, 250, 478, 265, 440),
             Triangulo(verde, 265, 440, 250, 478, 280, 478), Triangulo(branco, 265, 440, 280, 478, 295, 440),
             Triangulo(verde, 295, 440, 280, 478, 310, 478), Triangulo(branco, 295, 440, 310, 478, 325, 440),
             Triangulo(verde, 325, 440, 310, 478, 340, 478), Triangulo(branco, 325, 440, 340, 478, 355, 440),
             Triangulo(verde, 355, 440, 340, 478, 370, 478), Triangulo(branco, 355, 440, 370, 478, 385, 440),
             Triangulo(verde, 385, 440, 370, 478, 400, 478), Triangulo(branco, 385, 440, 400, 478, 415, 440),
             # 11 linha
             ])
        self.bolas = np.array([Bola(preto, 235, 165), Bola(preto, 265, 165), Bola(preto, 295, 165),  # 1 linha
                               Bola(preto, 220, 203), Bola(preto, 250, 203), Bola(preto, 280, 203),
                               Bola(preto, 310, 203),  # 2linha
                               Bola(preto, 205, 241), Bola(preto, 235, 241), Bola(preto, 265, 241),
                               Bola(preto, 295, 241), Bola(preto, 325, 241),  # 3 linha
                               Bola(preto, 190, 279), Bola(roxo, 220, 279), Bola(preto, 250, 279),
                               Bola(preto, 280, 279), Bola(roxo, 310, 279), Bola(preto, 340, 279),  # 4 linha
                               Bola(vermelho, 175, 338), Bola(amarelo, 205, 338), Bola(vermelho, 235, 338),
                               Bola(vermelho, 265, 338), Bola(vermelho, 295, 338), Bola(amarelo, 325, 338),
                               Bola(vermelho, 355, 338),  # 5 linha
                               Bola(vermelho, 190, 376), Bola(vermelho, 220, 376), Bola(vermelho, 250, 376),
                               Bola(vermelho, 280, 376), Bola(vermelho, 310, 376), Bola(vermelho, 340, 376),  # 6 linha
                               Bola(vermelho, 205, 414), Bola(vermelho, 235, 414), Bola(vermelho, 265, 414),
                               Bola(vermelho, 295, 414), Bola(vermelho, 325, 414)

                               ])
        self.bolas_consulta = np.array([Bola(preto, 235, 165), Bola(preto, 265, 165), Bola(preto, 295, 165),  # 1 linha
                                        Bola(preto, 220, 203), Bola(preto, 250, 203), Bola(preto, 280, 203),
                                        Bola(preto, 310, 203),  # 2linha
                                        Bola(preto, 205, 241), Bola(preto, 235, 241), Bola(preto, 265, 241),
                                        Bola(preto, 295, 241), Bola(preto, 325, 241),  # 3 linha
                                        Bola(preto, 190, 279), Bola(roxo, 220, 279), Bola(preto, 250, 279),
                                        Bola(preto, 280, 279), Bola(roxo, 310, 279), Bola(preto, 340, 279),  # 4 linha
                                        Bola(vermelho, 175, 338), Bola(amarelo, 205, 338), Bola(vermelho, 235, 338),
                                        Bola(vermelho, 265, 338), Bola(vermelho, 295, 338), Bola(amarelo, 325, 338),
                                        Bola(vermelho, 355, 338),  # 5 linha
                                        Bola(vermelho, 190, 376), Bola(vermelho, 220, 376), Bola(vermelho, 250, 376),
                                        Bola(vermelho, 280, 376), Bola(vermelho, 310, 376), Bola(vermelho, 340, 376),
                                        # 6 linha
                                        Bola(vermelho, 205, 414), Bola(vermelho, 235, 414), Bola(vermelho, 265, 414),
                                        Bola(vermelho, 295, 414), Bola(vermelho, 325, 414)

                                        ])

    def desenha_tabuleiro(self, screen):
        for triangulo in self.triangulos:
            triangulo.cria_triangulo(screen)
        for bola in self.bolas:
            bola.cria_bola(screen)
        pygame.display.flip()


    def verifica_se_e_bola(self, x, y):
        for circolo in self.bolas:
            (a, b) = circolo.get_x_y()
            if verifica_dentro_do_circulo(x, y, a, b, 7):
                return circolo

    def muda_posicao_circulo(self, x_atual, y_atual, x_desejada, y_desejado):
        global circulo, a, b
        for teste in self.bolas:
            (a, b) = teste.get_x_y()
            if verifica_dentro_do_circulo(x_atual, y_atual, a, b, 7):
                circulo = teste
                if circulo is not None:
                    cor = circulo.get_cor()
                    eh_preto_ou_roxo = (cor == preto) or (cor == roxo)
                    eh_amarelo_ou_vermelho = (cor == amarelo) or (cor == vermelho)
                    if eh_preto_ou_roxo:
                        preto_ou_roxo_quer_ir_para_direita = (
                                a + 45 > x_desejada > a + 15 and b - 28 < y_desejado < b + 10)
                        preto_ou_roxo_quer_ir_para_esquerda = (
                                a - 15 > x_desejada > a - 45 and b - 28 < y_desejado < b + 10)
                        preto_ou_roxo_quer_ir_para_diagonal_direita_cima = (
                                a + 30 > x_desejada > a and b - 28 > y_desejado > b - 66)
                        preto_ou_roxo_quer_ir_para_diagonal_direita_baixo = (
                                a + 30 > x_desejada > a and b + 10 < y_desejado < b + 48)
                        preto_ou_roxo_quer_ir_para_diagonal_esquerda_cima = (
                                a - 30 < x_desejada < a and b - 28 > y_desejado > b - 66)
                        preto_ou_roxo_quer_ir_para_diagonal_esquerda_baixo = (
                                a - 30 < x_desejada < a and b + 10 < y_desejado < b + 48)
                        if preto_ou_roxo_quer_ir_para_direita:
                            circulo.set_x_y((a + 30, b))
                        elif preto_ou_roxo_quer_ir_para_esquerda:
                            circulo.set_x_y((a - 30, b))
                        elif preto_ou_roxo_quer_ir_para_diagonal_direita_cima:
                            circulo.set_x_y((a + 15, b - 38))
                        elif preto_ou_roxo_quer_ir_para_diagonal_direita_baixo:
                            circulo.set_x_y((a + 15, b + 38))
                        elif preto_ou_roxo_quer_ir_para_diagonal_esquerda_cima:
                            circulo.set_x_y((a - 15, b - 38))
                        elif preto_ou_roxo_quer_ir_para_diagonal_esquerda_baixo:
                            circulo.set_x_y((a - 15, b + 38))
                    elif eh_amarelo_ou_vermelho:
                        amarelo_ou_vermelho_quer_ir_para_direita = (
                                a + 45 > x_desejada > a + 15 and b - 25 < y_desejado < b + 13)
                        amarelo_ou_vermelho_quer_ir_para_esquerda = (
                                a - 15 > x_desejada > a - 45 and b - 25 < y_desejado < b + 13)
                        amarelo_ou_vermelho_quer_ir_para_diagonal_direita_cima = (
                                a + 30 > x_desejada > a and b - 13 > y_desejado > b - 50)
                        amarelo_ou_vermelho_quer_ir_para_diagonal_direita_baixo = (
                                a + 30 > x_desejada > a and b + 25 < y_desejado < b + 62)
                        amarelo_ou_vermelho__quer_ir_para_diagonal_esquerda_cima = (
                                a - 30 < x_desejada < a and b - 13 > y_desejado > b - 50)
                        amarelo_ou_vermelho__quer_ir_para_diagonal_esquerda_baixo = (
                                a - 30 < x_desejada < a and b + 25 < y_desejado < b + 62)
                        if amarelo_ou_vermelho_quer_ir_para_direita:
                            circulo.set_x_y((a + 30, b))
                        elif amarelo_ou_vermelho_quer_ir_para_esquerda:
                            circulo.set_x_y((a - 30, b))
                        elif amarelo_ou_vermelho_quer_ir_para_diagonal_direita_cima:
                            circulo.set_x_y((a + 15, b - 38))
                        elif amarelo_ou_vermelho_quer_ir_para_diagonal_direita_baixo:
                            circulo.set_x_y((a + 15, b + 38))
                        elif amarelo_ou_vermelho__quer_ir_para_diagonal_esquerda_cima:
                            circulo.set_x_y((a - 15, b - 38))
                        elif amarelo_ou_vermelho__quer_ir_para_diagonal_esquerda_baixo:
                            circulo.set_x_y((a - 15, b + 38))

    def verifica_se_peca_foi_comida(self, x_agr, y_agr):
        for bola in self.bolas:
            (i, k) = bola.get_x_y()
            if verifica_dentro_do_circulo(x_agr, y_agr, i, k, 7):
                bolab = bola
                if bolab is not None:
                    x, y = bolab.get_x_y()
                    cor = bolab.get_cor()
                    eh_preto_ou_roxo = (cor == preto) or (cor == roxo)
                    eh_amarelo_ou_vermelho = (cor == amarelo) or (cor == vermelho)
                    if eh_preto_ou_roxo:
                        for circolo in self.bolas:
                            (a, b) = circolo.get_x_y()
                            verifica_se_ta_em_cima_direita = (a == x + 15) and (b == y - 38)
                            verifica_se_ta_em_baixo_direita = (a == x + 15) and (b == y + 38)
                            verifica_se_ta_em_baixo_esquerda = (a == x - 15) and (b == y + 38)
                            verifica_se_ta_do_lado_direito = (a == x + 30) and (b == y)
                            verifica_se_ta_do_lado_esquerdo = (a == x - 30) and (b == y)
                            if verifica_se_ta_do_lado_esquerdo:
                                for circolo_do_lado_esquerdo in self.bolas:
                                    (a, b) = circolo_do_lado_esquerdo.get_x_y()
                                    verifica_se_ta_em_cima_esquerda = (a == x - 15) and (b == y - 38)
                                    if verifica_se_ta_em_cima_esquerda:
                                        for circolo_dentro_do_triangulo in self.bolas:
                                            (a, b) = circolo_dentro_do_triangulo.get_x_y()
                                            verifica_se_ta_dentro_pela_esquerda = (a == x - 15) and (b == y - 17)
                                            if verifica_se_ta_dentro_pela_esquerda:
                                                circolo_dentro_do_triangulo.set_x_y((0, 0))
                                                circolo_dentro_do_triangulo.set_cor(cinza)
                            elif verifica_se_ta_do_lado_direito:
                                for circolo_do_lado_direito in self.bolas:
                                    (a, b) = circolo_do_lado_direito.get_x_y()
                                    verifica_se_tem_em_cima_direito = (a == x + 15) and (b == y - 38)
                                    if verifica_se_tem_em_cima_direito:
                                        for circulo_dentro_do_triangulo in self.bolas:
                                            (a, b) = circulo_dentro_do_triangulo.get_x_y()
                                            verifica_se_ta_dentro_pela_direita = (a == x + 15) and (b == y - 17)
                                            if verifica_se_ta_dentro_pela_direita:
                                                circulo_dentro_do_triangulo.set_x_y((0, 0))
                                                circulo_dentro_do_triangulo.set_cor(cinza)
                            elif verifica_se_ta_em_baixo_direita:
                                for circolo_do_lado_esqurdo in self.bolas:
                                    (a, b) = circolo_do_lado_esqurdo.get_x_y()
                                    verifica_se_tem_do_lado_esquerdo_em_baixo = (a == x - 15) and (b == y + 38)
                                    if verifica_se_tem_do_lado_esquerdo_em_baixo:
                                        for circulo_dentro_do_triangolo in self.bolas:
                                            (a, b) = circulo_dentro_do_triangolo.get_x_y()
                                            verifica_se_ta_dentro_pela_direita = (a == x) and (b == y + 21)
                                            if verifica_se_ta_dentro_pela_direita:
                                                circulo_dentro_do_triangolo.set_x_y((0, 0))
                                                circulo_dentro_do_triangolo.set_cor(cinza)
                    elif eh_amarelo_ou_vermelho:

                        for circolo in self.bolas:
                            (a, b) = circolo.get_x_y()
                            verifica_se_ta_em_cima_esquerda = (a == x - 15) and (b == y - 38)
                            verifica_se_ta_em_cima_direita = (a == x + 15) and (b == y - 38)
                            verifica_se_ta_em_baixo_direita = (a == x + 15) and (b == y + 38)
                            verifica_se_ta_em_baixo_esquerda = (a == x - 15) and (b == y + 38)
                            verifica_se_ta_do_lado_direito = (a == x + 30) and (b == y)
                            verifica_se_ta_do_lado_esquerdo = (a == x - 30) and (b == y)
                            if verifica_se_ta_do_lado_esquerdo:

                                for circolo_do_lado_esquerdo in self.bolas:
                                    (a, b) = circolo_do_lado_esquerdo.get_x_y()
                                    verifica_se_ta_em_baixo_esquerda = (a == x - 15) and (b == y + 38)
                                    if verifica_se_ta_em_baixo_esquerda:

                                        for circolo_dentro_do_triangulo in self.bolas:
                                            (a, b) = circolo_dentro_do_triangulo.get_x_y()
                                            verifica_se_ta_dentro_pela_esquerda = (a == x - 15) and (b == y + 17)
                                            if verifica_se_ta_dentro_pela_esquerda:
                                                circolo_dentro_do_triangulo.set_x_y((0, 0))
                                                circolo_dentro_do_triangulo.set_cor(cinza)
                            elif verifica_se_ta_do_lado_direito:
                                for circolo_do_lado_direito in self.bolas:
                                    (a, b) = circolo_do_lado_direito.get_x_y()
                                    verifica_se_tem_em_baixo_direito = (a == x + 15) and (b == y + 38)
                                    if verifica_se_tem_em_baixo_direito:
                                        for circulo_dentro_do_triangulo in self.bolas:
                                            (a, b) = circulo_dentro_do_triangulo.get_x_y()
                                            verifica_se_ta_dentro_pela_direita = (a == x + 15) and (b == y + 17)
                                            if verifica_se_ta_dentro_pela_direita:
                                                circulo_dentro_do_triangulo.set_x_y((0, 0))
                                                circulo_dentro_do_triangulo.set_cor(cinza)
                            elif verifica_se_ta_em_cima_direita:
                                for circolo_do_lado_esqurdo in self.bolas:
                                    (a, b) = circolo_do_lado_esqurdo.get_x_y()
                                    verifica_se_tem_do_lado_esquerdo_em_cima = (a == x - 15) and (b == y - 38)
                                    if verifica_se_tem_do_lado_esquerdo_em_cima:
                                        for circulo_dentro_do_triangolo in self.bolas:
                                            (a, b) = circulo_dentro_do_triangolo.get_x_y()
                                            verifica_se_ta_dentro_pela_direita = (a == x) and (b == y - 21)
                                            if verifica_se_ta_dentro_pela_direita:
                                                circulo_dentro_do_triangolo.set_x_y((0, 0))
                                                circulo_dentro_do_triangolo.set_cor(cinza)




    def teste(self):
        count = 0
        for i in self.bolas_consulta:
            a, b = i.get_x_y()
            cor = i.get_cor()
            self.bolas[count].set_x_y((a, b))
            self.bolas[count].set_cor(cor)
            count = count + 1
        pygame.display.flip()

    def verifica_se_tem_ganhador(self):
        cor_preto_ou_roxo = 0
        cor_amarelho_ou_vermelho = 0
        for bola in self.bolas:
            cor = bola.get_cor()
            if cor == preto or cor == roxo:
                cor_preto_ou_roxo = cor_preto_ou_roxo + 1
            if cor == amarelo or cor == vermelho:
                cor_amarelho_ou_vermelho = cor_amarelho_ou_vermelho + 1
        if cor_preto_ou_roxo <= 2:
            ganhador = "vermelho"
            screen.blit(overmelhovenceu, (0, 0))
            return ganhador
        elif cor_amarelho_ou_vermelho <= 2:
            ganhador = "preto"
            screen.blit(opretovenceu, (0, 0))
            return ganhador
