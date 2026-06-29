#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))

    def window(self, ):
        pass

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()


            # check-in dos eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar Janela
                    quit()  # Encerrar pygame
