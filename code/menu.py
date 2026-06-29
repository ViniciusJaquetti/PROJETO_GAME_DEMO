#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
import self
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_BLACK, COLOR_WHITE, MENU_OPTION


def convert_alpha():
    pass


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Fundo_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/MusicaMenu.wav')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(200, "Monster", COLOR_BLACK, ((WIN_WIDTH / 2), 70))
            self.menu_text(180, "Hunter", COLOR_BLACK, ((WIN_WIDTH / 2), 180))

            for i in range(len(MENU_OPTION)):
                self.menu_text(80, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 400 + 70 * i))

            pygame.display.flip()

            # check-in dos eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar Janela
                    quit()  # Encerrar pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
