import pygame


class Tela:
    _cores = {'cinza': (230, 230, 230)

             }
    """altura: int, largura: int, cor_fundo: str"""
    def __init__(self, altura, largura, cor_fundo):
        self._altura = altura
        self._largura = largura
        self._cor_fundo = cor_fundo
        self._tamanho_tela = (self._altura, self._largura)
        self._tela = pygame.display.set_mode(self.tamanho_tela())
        self.inicia_tela()


    def inicia_tela(self):
        pygame.init()
        pygame.display.set_caption("Jogo")

    def atualizar_tela(self):
        self._tela.fill(self.get_cores('cinza'))

    def tamanho_tela(self):
        return self._tamanho_tela

    def get_tela(self):
        return self._tela

    def get_altura(self):
        return self._altura

    def get_largura(self):
        return self._largura

    def get_cor(self):
        return self._cor_fundo

    def get_cores(self, cor):
        return self._cores[cor]