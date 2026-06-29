#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Bglevel1':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Bglevel1_{i}', (0, 0)))
                    list_bg.append(Background(f'Bglevel1_{i}', (WIN_WIDTH, 0)))
                return list_bg
