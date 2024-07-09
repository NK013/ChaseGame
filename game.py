import pgzero
from pgzero.builtins import Actor, keyboard
import pgzrun
import random
screen: pgzero.screen.Screen

WIDTH = 600
HEIGHT = 600

background = Actor("background")

game_state = "start_screen"

score = 0
mins = input("Wie lange möchtest du spielen? : ")
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

    if game_state == "game":
        player.draw()
        player2.draw()
        enemy.draw()
        coin.draw()
        score_string = str(score)
        screen.draw.text("Score: " + score_string, (10, 10), color='white')
        time_string = str(round(ticks / 60))
        screen.draw.text("Time: " + time_string + "s", (90, 10), color='white')

    if game_state == "start_screen":
        screen.draw.text("Drücke 'SPACE' um das Spiel zu starten!", (WIDTH/2 - 200, HEIGHT/2 - 100), fontname="fredoka_condensed-bold", color='white')
        #screen.draw.text("Wie lange möchtest du spielen?", (WIDTH/2 - 125, HEIGHT/2 - 50), color='white')
        #textfield
        screen.draw.text("Spieler 1:\n [W] - Oben\n [S] - Unten\n [A] - Links\n [R] - Rechts", (50 , HEIGHT - 150), color='white')
        screen.draw.text("Spieler 2:\n [I] - Oben\n [K] - Unten\n [J] - Links\n [L] - Rechts", (WIDTH - 150 , HEIGHT - 150), color='white')

    if game_state == "gameover_screen":
        screen.draw.text("Drücke 'SPACE' um das Spiel zu schließen!", (WIDTH/2 - 150, HEIGHT/2 - 100), fontname="fredoka_condensed-bold", color='white')
        screen.draw.text("Finaler Score: " + str(score), (WIDTH/2 - 50, HEIGHT/2 - 25), color='white')
        screen.draw.text("Übrige Zeit: " + str(round(ticks / 60)) + "s", (WIDTH/2 - 50, HEIGHT/2 - 0), color='white')


def handleTicks():

    global ticks

    ticks = ticks - 1


def handlePlayerMoving():

    if keyboard.l:
        player.x = player.x + 4
    if keyboard.j:
        player.x = player.x - 4
    if keyboard.k:
        player.y = player.y + 4
    if keyboard.i:
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

    global score, ticks, game_state

    if player2.colliderect(enemy):
        game_state = "gameover_screen"
        print()
        print("Game Over! (Death - Player 2)")
        print(" - Final Score:", score)
        print(" - Remeaning Time: " + str(round(ticks / 60)) + "s")
        print()
    
    if player.colliderect(enemy):
        game_state = "gameover_screen"
        print()
        print("Game Over! (Death - Player 1)")
        print(" - Final Score:", score)
        print(" - Remeaning Time: " + str(round(ticks / 60)) + "s")
        print()

    if ticks <= 0:
        game_state = "gameover_screen"
        print()
        print("Game Over! (Time)")
        print(" - Final Score:", score)
        print(" - Remeaning Time: " + str(round(ticks / 60)) + "s")
        print()


def handleCoins():

    global score

    if coin.colliderect(player) or coin.colliderect(player2):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1


def update():
    global game_state

    if game_state == "game":
        handleTicks()
        handlePlayerMoving()
        handleEnemyMoving()
        handleCoins()
        handleGameover()
    
    if game_state == "start_screen":
        if keyboard.space:
            game_state = "game"
    
    if game_state == "gameover_screen":
        if keyboard.space:
            print("Spiel wird geschlossen!")
            exit()


def startGame(game_state):

    if game_state == "start_screen":
        pgzrun.go()

    if game_state == "starting":
        print()
        print("Spiel wird gestartet...")
        print()

        pgzrun.go()

startGame("start_screen")