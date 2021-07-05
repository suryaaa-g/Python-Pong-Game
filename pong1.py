import turtle


window = turtle.Screen()
window.title("Pong by Surya")

window.bgcolor("black") #background 
window.setup(width = 800, height = 600)
window.tracer(0)

#Score
score_1 = 0
score_2 = 0

#Paddle 1
paddle_1 = turtle.Turtle();
paddle_1.speed(0) #needed for turtle module (animation speed)
paddle_1.shape("square") #default size is 20px * 20px

paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)

paddle_1.penup()
paddle_1.goto(-350, 0) #starting point




#Paddle 2
paddle_2 = turtle.Turtle();
paddle_2.speed(0) #needed for turtle module (animation speed)
paddle_2.shape("square") #default size is 20px * 20px

paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)

paddle_2.penup()
paddle_2.goto(350, 0) #starting point


#Ball
ball = turtle.Turtle();
ball.speed(0) #needed for turtle module (animation speed)
ball.shape("square") #default size is 20px * 20px
ball.color("white")
ball.penup()
ball.goto(0, 0) #starting point 
ball.dx = .2
ball.dy = .2


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



#function to move paddle 1 up
def paddle_1_up():
    y = paddle_1.ycor()
    y+=20
    paddle_1.sety(y)


#function to move paddle 1 down
def paddle_1_down():
    y = paddle_1.ycor()
    y-=20
    paddle_1.sety(y)
# end of function


#function to move paddle 2 up
def paddle_2_up():
    y = paddle_2.ycor()
    y+=20
    paddle_2.sety(y)


#function to move paddle 2 down
def paddle_2_down():
    y = paddle_2.ycor()
    y-=20
    paddle_2.sety(y)
# end of function




#key binding
window.listen() #listens to keyboard input
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")



#Main() - every game needs a main 
while True:
    window.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    #Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1