# Example file showing a basic pygame "game loop"
import random

import pygame

from CoreMechanics.player_controller import PlayerController
from CoreMechanics.npc import NpcController

# pygame setup
pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0.1

font = pygame.font.Font(None, 36)

# Set up the Game States
MENU = 0
PLAYING = 1
state = MENU

score = 0

BLACK = (0, 0, 0)

player_pos = pygame.Vector2(screen.get_width()/2, 640)
npc_pos = pygame.Vector2(screen.get_width()/2, 120)

player_radius = 40
npc_radius = 30

my_instance = PlayerController(player_pos, player_radius)
my_npc_instance = [NpcController(pygame.Vector2(npc_pos.x, npc_pos.y), npc_radius),
                   NpcController(pygame.Vector2(npc_pos.x-100, npc_pos.y), npc_radius),
                   NpcController(pygame.Vector2(npc_pos.x-200, npc_pos.y), npc_radius),
                   NpcController(pygame.Vector2(npc_pos.x+100, npc_pos.y), npc_radius),
                   NpcController(pygame.Vector2(npc_pos.x+200, npc_pos.y), npc_radius)]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if state == MENU:
                    state = PLAYING

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    if state == MENU:
        text = font.render("Press F to start", True, BLACK)
        screen.blit(text, (WIDTH / 2 - text.get_width()/2, HEIGHT / 2 - text.get_height() / 2))
    elif state == PLAYING:
        my_instance.draw(screen, "red")
        my_instance.player_movement(player_pos, screen.get_width())
        text = font.render("Score : " + str(score), True, BLACK)
        screen.blit(text, (50 - text.get_width() / 2, HEIGHT-20 - text.get_height() / 2))
        for npc in my_npc_instance:
            npc.draw(screen, "blue")
            npc.pos = npc.npc_movement(npc.pos)
            for npc_bullet in npc.bullets:
                npc_bullet.bullet_move(False)
                npc_bullet.draw(pygame.display.get_surface())
            for bullet in my_instance.bullets:
                bullet.bullet_move(True)
                bullet.draw(pygame.display.get_surface())
                if npc.is_dead is False and bullet.bullet_rect.colliderect(
                        npc.drawable_object_rect):
                    my_instance.bullets.remove(bullet)
                    npc.is_dead = True
                    score += 1
                    print("Collision Detect")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screenaa
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
