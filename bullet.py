import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулей"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        """Создание пули в позиии 0,0 и назначение правильной позиции"""
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = self.rect.top

        """Позициия поли храниться в вещественной форме"""
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ПЕремещение пули вверх по экрану"""
        self.y -= self.speed_factor

        """Обновление позиции прямоугольника"""
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
