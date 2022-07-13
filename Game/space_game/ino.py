# from email.mime import image
import pygame


class Ino(pygame.sprite.Sprite):
    """Клас одного пришельца"""

    def __init__(self, screen):
        """Иницифнизируем и задаем начальную позицию"""
        super(Ino, self). __init__()
        self.screen = screen
        self.image = pygame.image.load("images/ino.png")
        self.rect = self.image.get_rect()
        self.rect.row = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.row)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельцев"""
        self.y += 0.1 / 3
        self.rect.y = self.y
