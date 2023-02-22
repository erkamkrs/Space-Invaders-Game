import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Pygame Setup
font_type = 'freesansbold.ttf'
font = pygame.font.Font(font_type, 24)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("WELCOME TO:\n"
                           " SPACE INVADERS\n"
                           "by: ERKAM KIRIS")

# Score
score_val = 0
scoreX = 5
scoreY = 5

def display_score(x, y):
    score = font.render("Points: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Game Over
game_over_font = pygame.font.Font(font_type, 60)
def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (190, 250))


# Spaceship Setup
spaceship_image = pygame.image.load('images/spaceship.png')
spaceship_X = 370
spaceship_Y = 523
spaceship_Xchange = 0

# Alien Setup
alien_image = []
alien_X = []
alien_Y = []
alien_Xchange = []
alien_Ychange = []
num_of_aliens = 8

for num in range(num_of_aliens):
    alien_image.append(pygame.image.load('images/alien.png'))
    alien_X.append(random.randint(64, 737))
    alien_Y.append(random.randint(30, 180))
    alien_Xchange.append(1.2)
    alien_Ychange.append(50)

# Fireball
# rest - fireball is not moving
# fire - fireball is moving
fireball_image = pygame.image.load('images/fireball.png')
fireball_X = 0
fireball_Y = 500
fireball_Xchange = 0
fireball_Ychange = 3
fireball_state = "rest"

# Collusion
def collide(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False


def spaceship(x, y):
    screen.blit(spaceship_image, (x - 16, y + 10))


def alien(x, y, i):
    screen.blit(alien_image[i], (x, y))


def fireball(x, y):
    global fireball_state
    screen.blit(fireball_image, (x, y))
    fireball_state = "fire"


# Alien Movement
for i in range(num_of_aliens):
    if alien_Y[i] >= 450:
        if abs(spaceship_X - alien_X[i]) < 80:
            for j in range(num_of_aliens):
                alien_Y[j] = 2000
            game_over()
            break

    if alien_X[i] >= 735 or spaceship_X[i] <= 0:
        alien_Xchange[i] *= -1
        alien_Y[i] += alien_Ychange[i]

    # Collision
    collision = collide(fireball_X, alien_X[i], fireball_Y, alien_Y[i])
    if collision:
        score_val += 1
        fireball_Y = 600
        fireball_state = "rest"
        alien_X[i] = random.randint(64, 736)
        alien_Y[i] = random.randint(30, 200)
        alien_Ychange[i] *= -1

    alien(alien_X[i], alien_Y[i], i)

# Movement of Spaceship
if spaceship_X <= 16:
    spaceship_X = 16;
elif spaceship_X >= 750:
    spaceship_X = 750

spaceship(spaceship_X, spaceship_Y)
display_score(scoreX, scoreY)
pygame.display.update()
