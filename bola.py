import pygame

from entidades import Entidades
from tela import Tela


class Bola(Entidades):

    """tela: Tela, altura: int, largura: int, cor: str, pos_x: int, pos_y: int"""
    def __init__(self, tela, altura, largura, cor, pos_x, pos_y):
        super().__init__(tela, altura, largura, cor, pos_x, pos_y)

        self.velocidade_x = 1
        self.velocidade_y = -1

    def desenha_na_tela(self):
        pygame.draw.rect(self.get_tela(), self.get_cor(), self.get_entidade())

    def get_bola(self):
        return super().get_entidade()

    def get_velocidade_x(self):
        return self.velocidade_x

    def get_velocidade_y(self):
        return self.velocidade_y

    def set_velocidade_x(self, valor):
        self.velocidade_x = valor

    def set_velocidade_y(self, valor):
        self.velocidade_y = valor