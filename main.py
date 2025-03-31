import sys

import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def initialize_game():
    pygame.init()
    print("Starting Asteroids!")

def create_screen():
    # Set up the screen and clock
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()
    return screen, clock

def create_sprites_groups():
    # Create a group for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()
    return updatable, drawable, all_asteroids, all_shots

def set_sprite_containers(updatable, drawable, all_asteroids, all_shots):
    # Set the containers for the Player, Asteroids, and AsteroidField
    Asteroid.containers = (all_asteroids, updatable, drawable)
    Shot.containers = (all_shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

def create_game_objects():
    # Create the AsteroidField and Player objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    return asteroid_field, player

def handle_inputs_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def update_game_state(updatable, all_asteroids, all_shots, player, dt):
    # Updates all game objects and check for collisions
    updatable.update(dt)

     # Check for collisions
    for asteroid in all_asteroids:
            
        # Check for collisions between Asteroids and Bullets
        for bullet in all_shots:
            if asteroid.collides_with(bullet):
                asteroid.split()
                bullet.kill()

        # Check for collisions between Asteroids and the Player
        if asteroid.collides_with(player):
            print("Game Over!")
            sys.exit()

def render_game(screen, drawable):
    # Fills the screen, draws all objects, and updates the display.
    screen.fill("black")

    # Draw all objects in the drawable group (Player, Asteroids, Bullets)
    for obj in drawable:
        obj.draw(screen)

    pygame.display.flip()


def setupScreen():
    # Sets up the game screen and runs the main game loop.
    screen, clock = create_screen()
    updatable, drawable, all_asteroids, all_shots = create_sprites_groups()
    set_sprite_containers(updatable, drawable, all_asteroids, all_shots)
    asteroid_field, player = create_game_objects()

    dt = 0

    while True:
     if handle_inputs_events():
        return

     update_game_state(updatable, all_asteroids, all_shots, player, dt)
     render_game(screen, drawable)      
     # limit the framerate to 60 FPS
     dt = clock.tick(60) / 1000


def main():
    initialize_game()
    setupScreen()

if __name__ == "__main__":
    main()