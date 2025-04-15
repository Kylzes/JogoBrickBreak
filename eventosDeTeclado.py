import sys
import pygame

class EventosDeTeclado:

    """jogador: Jogador"""
    def __init__(self, jogador):
        self._jogador = jogador

    def checa_eventos_teclado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

            self.checa_tecla_pesionado(evento)
            self.checa_soltura_tecla(evento)

    def checa_tecla_pesionado(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                self._jogador.set_movimento_direita(True)
            if evento.key == pygame.K_LEFT:
                self._jogador.set_movimento_esquerda(True)

    def checa_soltura_tecla(self, evento):
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                self._jogador.set_movimento_direita(False)
            if evento.key == pygame.K_LEFT:
                self._jogador.set_movimento_esquerda(False)