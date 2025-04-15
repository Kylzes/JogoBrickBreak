
import pygame

from entidades import Entidades
from tela import Tela

class Jogador(Entidades):

    """tela: Tela, altura: int, largura: int, cor: str, pos_x: int, pos_y: int"""
    def __init__(self, tela, altura, largura, cor, pos_x, pos_y):
        super().__init__(tela, altura, largura, cor, pos_x, pos_y)

        self._movimento_direita = False
        self._movimento_esquerda = False
        self._velocidade = 1

        self.desenha_na_tela()

    def desenha_na_tela(self):
        pygame.draw.rect(self.get_tela(), self.get_cor(), self.get_jogador())

    def get_jogador(self):
        return super().get_entidade()

    def atualiza(self):
        if self._movimento_direita and (self.get_jogador().x < 500):
            self.get_entidade().x += self._velocidade
        if self._movimento_esquerda and (self.get_jogador().x > 0):
            self.get_entidade().x -= self._velocidade

    def set_movimento_direita(self, valor):
        self._movimento_direita = valor

    def set_movimento_esquerda(self, valor):
        self._movimento_esquerda = valor
