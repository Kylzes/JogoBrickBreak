import pygame

from entidades import Entidades

class Blocos(Entidades):

    """tela: Tela, altura: int, largura: int, cor: str, pos_x: int, pos_y: int"""
    def __init__(self, tela, altura, largura, cor, pos_x, pos_y):
        super().__init__(tela, altura, largura, cor, pos_x, pos_y)

        self._quantidades_de_blocos_x = 0
        self._quantidades_de_blocos_y = 0
        self._blocos = []

    def cria_uma_lista_de_blocos(self):
        for j in range(self.get_quantidade_de_blocos_y()):
            for i in range(self.get_quantidade_de_blocos_x()):
                self._blocos.append(pygame.Rect(
                    (i * (self.get_largura() + 5)),
                    (j * (self.get_altura() + 5)),
                    self._largura, self._altura))

    def desenha_na_tela(self):
        for bloco in self.get_blocos():
            pygame.draw.rect(self.get_tela(), self.get_cor(), bloco)

    def get_blocos(self):
        return self._blocos

    def set_quantidade_de_blocos_x(self, quantidade_de_blocos_x):
        self._quantidades_de_blocos_x = quantidade_de_blocos_x

    def set_quantidade_de_blocos_y(self, quantidade_de_blocos_y):
        self._quantidades_de_blocos_y = quantidade_de_blocos_y

    def get_quantidade_de_blocos_x(self):
        return self._quantidades_de_blocos_x

    def get_quantidade_de_blocos_y(self):
        return self._quantidades_de_blocos_y

    """bloco: Bloco"""
    def remove_bloco(self, bloco):
        self._blocos.remove(bloco)