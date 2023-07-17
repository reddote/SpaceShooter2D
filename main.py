# Example file showing a basic pygame "game loop"
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

BLACK = (0, 0, 0)

player_pos = pygame.Vector2(screen.get_width()/2, 640)
npc_pos = pygame.Vector2(screen.get_width()/2, 120)

player_radius = 40
npc_radius = 30

my_instance = PlayerController(player_pos, player_radius)
my_npc_instance = NpcController(npc_pos, npc_radius)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == MENU:
                    state = PLAYING

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    if state == MENU:
        text = font.render("Press SPACE to start", True, BLACK)
        screen.blit(text, (WIDTH / 2 - text.get_width()/2, HEIGHT / 2 - text.get_height() / 2))
    elif state == PLAYING:
        my_npc_instance.draw(screen, "blue")

        my_instance.draw(screen, "red")

        for bullet in my_instance.bullets:
            bullet.bullet_move()
            bullet.draw(pygame.display.get_surface())
            if my_npc_instance.is_dead is False and bullet.bullet_rect.colliderect(
                    my_npc_instance.drawable_object_rect):
                my_instance.bullets.remove(bullet)
                my_npc_instance.is_dead = True
                print("Collision Detect")

        my_instance.player_movement(player_pos, screen.get_width())
        my_npc_instance.npc_movement(npc_pos, screen.get_width())

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()