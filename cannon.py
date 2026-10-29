"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Velocidad más rápida para el proyectil
        speed.x = (x + 200) / 5
        speed.y = (y + 200) / 5

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(30) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Velocidad más rápida para los balones
    for target in targets:
        target.x -= 3

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Reposicionar balones si salen de la ventana para que el juego nunca termine
        if target.x < -200:
            target.x = 200
            target.y = randrange(-150, 150)

        if abs(target - ball) > 13:
            targets.append(target)

    draw()
    ontimer(move, 30)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
