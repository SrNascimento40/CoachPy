import pygame
from pygame.locals import *
from sys import exit
import random
import time


def skill_atk():
    jab = pygame.mixer.Sound("jab.wav")
    cross = pygame.mixer.Sound("direto.wav")
    hook_left = pygame.mixer.Sound("left_hook.wav")
    upper_left = pygame.mixer.Sound("left_upper.wav")
    hook_right = pygame.mixer.Sound("right_hook.wav")
    upper_right = pygame.mixer.Sound("right_upper.wav")
    body_jab = pygame.mixer.Sound("body_jab.wav")
    body_cross = pygame.mixer.Sound("body_cross.wav")
    body_hook_left = pygame.mixer.Sound("body_left_hook.wav")
    body_upper_left = pygame.mixer.Sound("body_left_upper.wav")
    body_hook_right = pygame.mixer.Sound("body_right_hook.wav")
    body_upper_right = pygame.mixer.Sound("body_right_upper.wav")
    golpes = [jab, cross, hook_left, hook_right, upper_right, upper_left, body_jab, body_cross, body_hook_left,
              body_hook_right, body_upper_right, body_upper_left]
    choosed_punch = golpes[random.randint(0, len(golpes) - 1)]
    choosed_punch.play()


def skill_comb():
    comb112 = pygame.mixer.Sound("112.wav")
    comb11b2 = pygame.mixer.Sound("11b2.wav")
    comb12 = pygame.mixer.Sound("12.wav")
    comb123 = pygame.mixer.Sound("123.wav")
    comb125b = pygame.mixer.Sound("125b.wav")
    comb123b5b = pygame.mixer.Sound("123b5b.wav")
    combinations = [comb123b5b, comb125b, comb12, comb123, comb112, comb11b2]
    choosed_comb = combinations[random.randint(0, len(combinations) - 1)]
    choosed_comb.play()


def skill_def():
    pendulo_r = pygame.mixer.Sound("pendulo_direita.wav")
    pendulo_l = pygame.mixer.Sound("pendulo_esquerda.wav")
    meio_pendulo = pygame.mixer.Sound("half_pendulum.wav")
    slip_r = pygame.mixer.Sound("slip_r.wav")
    slip_l = pygame.mixer.Sound("slip_l.wav")
    pivot = pygame.mixer.Sound("pivot.wav")
    diag_exit = pygame.mixer.Sound("saida_diag.wav")
    defensive_skills = (pendulo_l, pendulo_r, meio_pendulo, slip_l, slip_r, pivot, diag_exit)
    choosed_defence = defensive_skills[random.randint(0, len(defensive_skills) - 1)]
    choosed_defence.play()


def damato():
    x = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if x >= 300:
            break

        print(x)
        time.sleep(1)
        x += 1
        if (x % 5) == 0:
            the_choosen = random.randint(0, 3)
            if the_choosen == 0:
                skill_def()

            elif the_choosen == 1:
                skill_atk()

            elif the_choosen == 2 or 3:
                skill_comb()


pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Coach.Py')
screen.fill((0, 10, 0))

font = pygame.font.SysFont('arial', 20, True, True)
y = 0

while True:
    starter_txt = "START"
    starter = font.render(starter_txt, False, (212, 5, 2))
    starter_form = starter.get_rect()
    starter_form.center = (300, 300)
    pygame.draw.rect(screen, (250, 249, 230), (0, 280, 600, 35))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if y == 1:
        damato()
    y = 1

    screen.blit(starter, starter_form)

    pygame.display.update()
