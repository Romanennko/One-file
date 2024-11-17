import turtle

win = turtle.Screen()
win.title('Ping-Pong')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

blue_player = turtle.Turtle()
blue_player.speed(0)
blue_player.shape('square')
blue_player.color('blue')
blue_player.shapesize(stretch_len=1, stretch_wid=5)
blue_player.penup()
blue_player.goto(-350, 0)

red_player = turtle.Turtle()
red_player.speed(0)
red_player.shape('square')
red_player.color('red')
red_player.shapesize(stretch_len=1, stretch_wid=5)
red_player.penup()
red_player.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

score_blue_player = 0
score_red_player = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write('Blue player: 0\nRed player 0', align='center', font=('Verdana', 22, 'normal'))

blue_win = turtle.Turtle()
blue_win.speed(0)
blue_win.shape('square')
blue_win.color('white')
blue_win.penup()
blue_win.hideturtle()
blue_win.goto(0, 180)

red_win = turtle.Turtle()
red_win.speed(0)
red_win.shape('square')
red_win.color('white')
red_win.penup()
red_win.hideturtle()
red_win.goto(0, 180)

score = turtle.Turtle()
score.speed(0)
score.shape('square')
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 0)


def blue_player_up():
    y = blue_player.ycor()
    y += 10
    blue_player.sety(y)


def blue_player_down():
    y = blue_player.ycor()
    y -= 10
    blue_player.sety(y)


def red_player_up():
    y = red_player.ycor()
    y += 10
    red_player.sety(y)


def red_player_down():
    y = red_player.ycor()
    y -= 10
    red_player.sety(y)


win.listen()
win.onkeypress(blue_player_up, 'w')
win.onkeypress(blue_player_down, 's')
win.onkeypress(red_player_up, 'Up')
win.onkeypress(red_player_down, 'Down')

while True:
    win.update()

    if score_blue_player == 5:
        ball.goto(1000, 1000)
        pen.clear()
        blue_player.goto(1000, 1000)
        red_player.goto(1000, 1000)
        blue_win.write('Blue player win!!!', align='center', font=('Verdana', 22, 'normal'))
        score.write(f'Blue score: {score_blue_player}\nRed score: {score_red_player}',
                    align='center', font=('Verdana', 22, 'normal'))

    elif score_red_player == 5:
        ball.goto(1000, 1000)
        pen.clear()
        blue_player.goto(1000, 1000)
        red_player.goto(1000, 1000)
        red_win.write('Red player win!!!', align='center', font=('Verdana', 22, 'normal'))
        score.write(f'Blue score: {score_blue_player}\nRed score: {score_red_player}',
                    align='center', font=('Verdana', 22, 'normal'))

    else:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if red_player.ycor() > 250:
            red_player.sety(250)

        if red_player.ycor() < -240:
            red_player.sety(-240)

        if blue_player.ycor() > 250:
            blue_player.sety(250)

        if blue_player.ycor() < -240:
            blue_player.sety(-240)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_blue_player += 1
            pen.clear()
            pen.write(f'Blue player: {score_blue_player}\nRed player {score_red_player}', align='center',
                      font=('Verdana', 22, 'normal'))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_red_player += 1
            pen.clear()
            pen.write(f'Blue player: {score_blue_player}\nRed player {score_red_player}', align='center',
                      font=('Verdana', 22, 'normal'))

        if ball.xcor() > 340 and red_player.ycor() + 50 > ball.ycor() > red_player.ycor() - 50:
            ball.dx *= -1

        if ball.xcor() < -340 and blue_player.ycor() + 50 > ball.ycor() > blue_player.ycor() - 50:
            ball.dx *= -1
