import pgzero
from pgzero.builtins import Actor, keyboard
import pgzrun
import random
screen: pgzero.screen.Screen

WIDTH = 600
HEIGHT = 600

background = Actor("background")

score = 0
ticks = 2500

player = Actor("player1")
player.x = 450
player.y = 200

player2 = Actor("player2")
player2.x = 150
player2.y = 200

enemy = Actor("enemy")
enemy.x = 250
enemy.y = 525

coin = Actor("coin", pos=(300,300))

def draw():
    screen.clear()
    background.draw()
    player.draw()
    player2.draw()
    enemy.draw()
    coin.draw()
    score_string = str(score)
    screen.draw.text("Score: " + score_string, (0,0), color='white')
    time_string = str(round(ticks))
    screen.draw.text("Ticks: " + time_string, (100,0), color='white')

def update():

    global score, ticks

    ticks = ticks - 1
    if ticks == 2000:
        print()
        print("Noch 2000 Ticks!")
    elif ticks == 1500:
        print()
        print("Noch 2000 Ticks!")
    elif ticks == 1000:
        print()
        print("Noch 1000 Ticks!")
    elif ticks == 500:
        print()
        print("Noch 500 Ticks!")
    elif ticks == 200:
        print()
        print("Noch 200 Ticks!")
    elif ticks <= 0:
        print()
        print("Game Over! (Time)")
        print("Final Score:", score)
        print()
        exit()

    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

    if keyboard.d:
        player2.x = player2.x + 4
    if keyboard.a:
        player2.x = player2.x - 4
    if keyboard.s:
        player2.y = player2.y + 4
    if keyboard.w:
        player2.y = player2.y - 4
    if player2.colliderect(enemy):
        print()
        print("Game Over! (Death - Player 2)")
        print("Final Score:", score)
        print()
        exit()

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

    if player2.x > WIDTH:
        player2.x = 0
    if player2.x < 0:
        player2.x = WIDTH
    if player2.y < 0:
        player2.y = HEIGHT
    if player2.y > HEIGHT:
        player2.y = 0

    if enemy.x < player2.x:
        enemy.x = enemy.x + 1.5
    if enemy.x > player2.x:
        enemy.x = enemy.x - 1.5
    if enemy.y < player2.y:
        enemy.y = enemy.y + 1.5
    if enemy.y > player2.y:
        enemy.y = enemy.y - 1.5
    if player.colliderect(enemy):
        print()
        print("Game Over! (Death - Player 1)")
        print("Final Score:", score)
        print()
        exit()

    if coin.colliderect(player) or coin.colliderect(player2):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)

pgzrun.go()