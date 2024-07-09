import pgzero
from pgzero.builtins import Actor, keyboard
import pgzrun
import random
screen: pgzero.screen.Screen

WIDTH = 600
HEIGHT = 600

background = Actor("background")

score = 0
mins = input("Wie lange möchtest du spielen? (In Minuten) : ")
ticks = int(mins) * 60 * 60 #: 60 Ticks = 1 second | 1*60*60 = 1 minute

player = Actor("player_1")
player.x = 450
player.y = 200

player2 = Actor("player_2")
player2.x = 150
player2.y = 200

enemy = Actor("enemy")
enemy.x = 250
enemy.y = 525

coin = Actor("coin")
coin.x = 300
coin.y = 300


def draw():
    screen.clear()
    background.draw()
    player.draw()
    player2.draw()
    enemy.draw()
    coin.draw()
    score_string = str(score)
    screen.draw.text("Score: " + score_string, (10, 10), color='white')
    time_string = str(round(ticks / 60))
    screen.draw.text("Time: " + time_string + "s", (90, 10), color='white')


def handleTicks():

    global ticks

    ticks = ticks - 1


def handlePlayerMoving():

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


def handleEnemyMoving():

    d_p1 =  enemy.distance_to(player)
    d_p2 =  enemy.distance_to(player2)

    if d_p1 > d_p2:
        if enemy.x < player2.x:
            enemy.x = enemy.x + 0.8
        if  enemy.x > player2.x:
            enemy.x = enemy.x - 0.8
        if enemy.y < player2.y:
            enemy.y = enemy.y + 0.8
        if enemy.y > player2.y:
            enemy.y = enemy.y - 0.8
    else:
        if enemy.x < player.x:
            enemy.x = enemy.x + 0.8
        if  enemy.x > player.x:
            enemy.x = enemy.x - 0.8
        if enemy.y < player.y:
            enemy.y = enemy.y + 0.8
        if enemy.y > player.y:
            enemy.y = enemy.y - 0.8


def handleGameover():

    global score, ticks

    if player2.colliderect(enemy):
        print()
        print("Game Over! (Death - Player 2)")
        print(" - Final Score:", score)
        print(" - Remeaning Time: " + str(round(ticks / 60)) + "s")
        print()
        exit()
    
    if player.colliderect(enemy):
        print()
        print("Game Over! (Death - Player 1)")
        print(" - Final Score:", score)
        print(" - Remeaning Time: " + str(round(ticks / 60)) + "s")
        print()
        exit()

    if ticks <= 0:
        print()
        print("Game Over! (Time)")
        print(" - Final Score:", score)
        print(" - Remeaning Time: " + str(round(ticks / 60)) + "s")
        print()
        exit()


def handleCoins():

    global score

    if coin.colliderect(player) or coin.colliderect(player2):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1


def update():

    handleTicks()
    handlePlayerMoving()
    handleEnemyMoving()
    handleCoins()
    handleGameover()


def startGame():

    print()
    print("Spiel wird gestartet...")
    print()

    pgzrun.go()

startGame()