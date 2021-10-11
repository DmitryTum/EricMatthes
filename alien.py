import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """Загрузка изображения и назначение атрибута rect"""
        self.image = pygame.image.load('image/bad_alien.bmp')
        self.rect = self.image.get_rect()

        """Создание пришельца в левом верхнем углу"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Вывод пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Возврат True если пришелец находится у края экран"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещение пришельцев"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
