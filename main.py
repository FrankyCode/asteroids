import sys

import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def setupScreen():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()

    # Create a group for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    # Set the containers for the Player, Asteroids, and AsteroidField
    Asteroid.containers = (all_asteroids, updatable, drawable)
    Shot.containers = (all_shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    # Create the AsteroidField and Player objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all objects in the updatable group
        updatable.update(dt)

        # Check for collisions between the player and asteroids
        for asteroid in all_asteroids:
            for bullet in all_shots:
                if asteroid.collides_with(bullet):
                    asteroid.kill()
                    bullet.kill()

            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        # Draw all objects in the drawable group (Player, Asteroids, Bullets)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print("Starting Asteroids!")
    setupScreen()

if __name__ == "__main__":
    main()