from variaveis import Variaveis
from tela import Tela
from jogador import Jogador
from bola import Bola
from blocos import Blocos

import pygame


class ChecaEventoColisao:

    def __init__(self, tela: Tela, jogador: Jogador, bola: Bola, blocos: Blocos):
        self.variavel = Variaveis()
        self.tela = tela
        self.bola = bola
        self.jogador = jogador
        self.blocos = blocos


    def atualiza(self):
        self.bola.set_velocidade_x(self.colisao_bola_tela_eixo_x())
        self.bola.set_velocidade_y(self.colisao_bola_tela_eixo_y())
        self.bola.set_velocidade_y(self.colisao_bola_blocos())
        self.bola.set_velocidade_y(self.colisao_jogador_bola())
        self.checa_jodador_perdeu()
        self.pontuacao()
        self.ganhou()


    def colisao_bola_tela_eixo_x(self):
        velocidade_x = self.bola.get_velocidade_x()

        self.bola.get_entidade().x = (self.bola.get_entidade().x + velocidade_x)
        if self.bola.get_entidade().x <= 0:
            velocidade_x = -velocidade_x
        if self.bola.get_entidade().x >= self.tela.get_largura():
            velocidade_x = -velocidade_x

        return velocidade_x


    def colisao_bola_tela_eixo_y(self):
        velocidade_y = self.bola.get_velocidade_y()
        self.bola.get_entidade().y = (self.bola.get_entidade().y + velocidade_y)

        if self.bola.get_entidade().y <= 0:
            velocidade_y = -velocidade_y

        return velocidade_y

    def colisao_jogador_bola(self):
        velocidade_y = self.bola.get_velocidade_y()
        if self.jogador.get_entidade().collidepoint(self.bola.get_entidade().x,
                                                    (self.bola.get_entidade().y + 10)):
            velocidade_y = -velocidade_y

        return velocidade_y

    def colisao_bola_blocos(self):
        velocidade_y = self.bola.get_velocidade_y()
        for bloco in self.blocos.get_blocos():
            if bloco.collidepoint(self.bola.get_entidade().x,
                                  self.bola.get_entidade().y):
                self.blocos.remove_bloco(bloco)
                self.atualiza_pontuacao()
                velocidade_y = -velocidade_y

        return velocidade_y

    def checa_jodador_perdeu(self):
        if self.bola.get_bola().y >= self.tela.get_altura():
            return True
        return False

    def pontuacao(self):
       fonte = pygame.font.Font(None, 20)
       texto = fonte.render(f"Pontuação: {self.variavel.get_pontuacao()}",
                            1, self.variavel.get_cores('preto'))
       self.tela.get_tela().blit(texto, (0, 580))

    def atualiza_pontuacao(self):
        self.variavel.soma_pontuacao()

    def ganhou(self):
        if (self.variavel.get_pontuacao() >=
                (self.variavel.get_quantidadede_blocos_x() *
                 self.variavel.quantidadede_blocos_y)):
            return True
        return False