from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *
from shot import *
import pygame
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = asteroids, updatable, drawable
    Player.containers = updatable, drawable
    Shot.containers = shots, updatable, drawable
    # Has to come before creating a class instance

    # short code for:
    #updatable.add(player1)
    #drawable.add(player1)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ##convention to use lower case
    asteroidfieldx = AsteroidField()

    


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for s in updatable:
            s.update(dt)      # tracking movement
        for c in asteroids:
            if c.collisions(player1) == True:
                print("Game Over!")
                sys.exit()
        for a in asteroids:
            for b in shots:
                if a.collisions(b) == True:
                    a.split()
                    b.kill()
        screen.fill((0,0,0))    # fills the screen black
        for s in drawable:
            s.draw(screen)    # needs to be BEFORE screen update!
        pygame.display.flip()   # updates screen
        dt = clock.tick(60) / 1000
        

        #Note: apparently clock.tick(60)/1000 = dt is not valid!



if __name__ == "__main__":
    main()