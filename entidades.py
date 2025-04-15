import pygame
from tela import Tela

class Entidades():

    """tela: Tela, altura: int, largura: int, cor: str, pos_x: int, pos_y: int"""
    def __init__(self, tela, altura, largura, cor, pos_x, pos_y):
        self._tela = tela
        self._altura = altura
        self._largura = largura
        self._cor = cor
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._entidade = pygame.Rect(self.get_pos_x(), self.get_pos_y(),
                                     self.get_largura(), self.get_altura())

    def atualiza(self):
        pass

    def get_entidade(self):
        return  self._entidade

    def get_pos_x(self):
        return self._pos_x

    def get_pos_y(self):
        return  self._pos_y

    def get_tela(self):
        return self._tela

    def get_altura(self):
        return self._altura

    def get_largura(self):
        return self._largura

    def get_cor(self):
        return self._cor