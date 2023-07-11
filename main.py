# Example file showing a basic pygame "game loop"
import pygame

from player_controller import PlayerController

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0.1

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

my_instance = PlayerController()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    pygame.draw.circle(screen, "red", player_pos, 40)

    for bullet in my_instance.bullets:
        bullet.bullet_move()
        bullet.draw(pygame.display.get_surface())

    my_instance.player_movement(player_pos, screen.get_width())

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()