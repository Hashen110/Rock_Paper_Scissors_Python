import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode([1081, 600])
running = True
rand = -1
clicked = -1
font = pygame.font.SysFont("monospace", 50)

rock = pygame.image.load('img/rock.png')
paper = pygame.image.load('img/paper.png')
scissors = pygame.image.load('img/scissors.png')


def click():
    screen.blit(font.render("You", True, (0, 255, 0)), (175, 100))
    screen.blit(font.render("Computer", True, (0, 255, 0)), (754, 100))
    if clicked == 0:
        screen.blit(rock, (100, 150))
    elif clicked == 1:
        screen.blit(paper, (100, 150))
    elif clicked == 2:
        screen.blit(scissors, (100, 150))
    if rand == 0:
        screen.blit(rock, (754, 150))
    elif rand == 1:
        screen.blit(paper, (754, 150))
    elif rand == 2:
        screen.blit(scissors, (754, 150))
    if clicked == rand:
        screen.blit(font.render("TIE", True, (255, 255, 255)), (500, 250))
    elif (clicked == 0 and rand == 2) or (clicked == 1 and rand == 0) or (clicked == 2 and rand == 1):
        screen.blit(font.render("YOU WIN", True, (0, 0, 255)), (425, 250))
    elif (clicked == 0 and rand == 1) or (clicked == 1 and rand == 2) or (clicked == 2 and rand == 0):
        screen.blit(font.render("YOU LOSE", True, (255, 0, 0)), (425, 250))
    screen.blit(font.render("Play Again", True, (255, 255, 255)), (400, 450))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if clicked == -1 and 100 < pos[0] < 327 and 200 < pos[1] < 427:
                clicked = 0
            elif clicked == -1 and 427 < pos[0] < 654 and 200 < pos[1] < 427:
                clicked = 1
            elif clicked == -1 and 754 < pos[0] < 981 and 200 < pos[1] < 427:
                clicked = 2
            elif clicked != -1 and 475 < pos[0] < 700 and 325 < pos[1] < 500:
                clicked = -1
                rand = -1
    screen.fill((0, 0, 0))
    screen.blit(font.render("Rock Paper Scissors", True, (255, 255, 255)), (250, 10))
    if clicked == -1:
        screen.blit(rock, (100, 200))
        screen.blit(paper, (427, 200))
        screen.blit(scissors, (754, 200))
    else:
        if rand == -1:
            rand = randrange(3)
        click()
    pygame.display.update()

pygame.quit()
