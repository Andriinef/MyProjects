import controls
import pygame
from gun import Gun
from pygame.sprite import Group
from scores import Scores
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Комические защитники")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    scor = Scores(screen, stats)

    while True:  # главный цикл
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, scor, gun, inos, bullets)
            controls.update_bullets(screen, stats, scor, inos, bullets)
            controls.update_inos(stats, screen, scor, gun, inos, bullets)


run()
