import pygame.font


class Variaveis:

    def __init__(self):
        self.cores = {'preto': (0, 0, 0),
                 'azul': (0, 0, 255),
                 'vermelho': (255, 0, 0),
                 'cinza': (230, 230, 230),
                 'amarelo': (255,255,0)
                 }

        self.altura_tela = 600
        self.largura_tela = 600

        self.posicao_inicial_jogador_x = 300
        self.posicao_inicial_jogador_y = 560
        self.altura_jogador = 15
        self.largura_jogador = 100

        self.posicao_inicial_bola_x = 200
        self.posicao_inicial_bola_y = 200
        self.altura_bola = 15
        self.largura_bola = 15

        self.posicao_inicial_bloco_x = 0
        self.posicao_inicial_bloco_y = 0
        self.altura_bloco = 15
        self.largura_bloco = (self.largura_tela / 6) - 5

        self.quantidadede_blocos_x = 6
        self.quantidadede_blocos_y = 1

        self.movimento_bola_x = 1
        self.movimento_bola_y = 1

        self.pontuacao = 0

    def get_cores(self, cor: str):
        return self.cores[cor]

    def get_largura_tela(self):
        return self.largura_tela

    def get_altura_tela(self):
        return self.altura_tela

    def get_posicao_inicial_jogador_x(self):
        return self.posicao_inicial_jogador_x

    def get_posicao_inicial_jogador_y(self):
        return self.posicao_inicial_jogador_y

    def get_altura_jogador(self):
        return self.altura_jogador

    def get_largura_jogador(self):
        return self.largura_jogador

    def get_posicao_inicial_bola_x(self):
        return self.posicao_inicial_bola_x

    def get_posicao_inicial_bola_y(self):
        return self.posicao_inicial_bola_y

    def get_altura_bola(self):
        return self.altura_bola

    def get_largura_bola(self):
        return self.largura_bola

    def get_posicao_inicial_bloco_x(self):
        return self.posicao_inicial_bloco_x

    def get_posicao_inicial_bloco_y(self):
        return self.posicao_inicial_bloco_y

    def get_altura_bloco(self):
        return self.altura_bloco

    def get_largura_bloco(self):
        return self.largura_bloco

    def get_quantidadede_blocos_x(self):
        return self.quantidadede_blocos_x

    def get_quantidadede_blocos_y(self):
        return self.quantidadede_blocos_y

    def get_velocidade_bola_x(self):
        return self.movimento_bola_x

    def get_velocidade_bola_y(self):
        return self.movimento_bola_y

    def get_pontuacao(self):
        return self.pontuacao

    def soma_pontuacao(self):
        self.pontuacao += 1

    def get_fonte(self):
        return  self.texto_fonte

    def set_velocidade_bola_x(self, valor):
        self.movimento_bola_x = valor

    def set_velocidade_bola_y(self, valor):
        self.movimento_bola_y = valor