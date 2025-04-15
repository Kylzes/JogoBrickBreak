import pygame

from tela import Tela
from jogador import Jogador
from bola import Bola
from blocos import Blocos
from eventosDeTeclado import EventosDeTeclado
from variaveis import Variaveis
from checaEventoColisao import ChecaEventoColisao

class Jogo:
    def __init__(self):
        self._variavel = Variaveis()

        self._tela = Tela(self._variavel.get_altura_tela(), self._variavel.get_largura_tela(),
                          self._variavel.get_cores('cinza'))

        self._jogador = Jogador(self._tela.get_tela(), self._variavel.get_altura_jogador(),
                                self._variavel.get_largura_jogador(), self._variavel.get_cores('preto'),
                                self._variavel.get_posicao_inicial_jogador_x(),
                                self._variavel.get_posicao_inicial_jogador_y())

        self._bola = Bola(self._tela.get_tela(), self._variavel.get_altura_bola(),
                          self._variavel.get_largura_bola(), self._variavel.get_cores('azul'),
                          self._variavel.get_posicao_inicial_bola_x(),
                          self._variavel.get_posicao_inicial_bola_y())

        self._blocos = Blocos(self._tela.get_tela(), self._variavel.get_altura_bloco(),
                              self._variavel.get_largura_bloco(), self._variavel.get_cores('vermelho'),
                              self._variavel.get_posicao_inicial_bloco_x(),
                              self._variavel.get_posicao_inicial_bloco_y())

        self._blocos.set_quantidade_de_blocos_x(self._variavel.get_quantidadede_blocos_x())
        self._blocos.set_quantidade_de_blocos_y(self._variavel.get_quantidadede_blocos_y())
        self._blocos.cria_uma_lista_de_blocos()

        self._eventosDeTeclado = EventosDeTeclado(self._jogador)
        self._checaEventoColisao = ChecaEventoColisao(self._tela, self._jogador, self._bola, self._blocos)

        self.fim_jogo = False

    def estado_jogo(self):
        if self._checaEventoColisao.ganhou() or self._checaEventoColisao.checa_jodador_perdeu():
            return True

    def loop_jogo(self):
        while not self.fim_jogo:
            self.fim_jogo = self.estado_jogo()

            # Atualizar/Desenha na tela
            self._jogador.atualiza()
            self._tela.atualizar_tela()
            self._jogador.desenha_na_tela()
            self._bola.desenha_na_tela()
            self._blocos.desenha_na_tela()

            self._eventosDeTeclado.checa_eventos_teclado()
            self._checaEventoColisao.atualiza()

            pygame.time.wait(1)
            pygame.display.flip()

        pygame.quit()
