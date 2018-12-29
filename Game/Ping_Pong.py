import turtle
import os
import time

# Score Varibale 
player_a_score = 0
player_b_score = 0

# Screen of the Game Ping  
wn = turtle.Screen()  # wn has the Screen now with the help of the turtle
wn.title("Ping Pong") # Title of the Screen 
wn.bgcolor("black") # change the color of the Screen 
wn.setup(width=800,height=600)  # the geometry of the screen  of the game 
wn.tracer(0)  # used for the stop the processes 


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



# paddle ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.penup()
ball.color("red")
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

#Game over Screen 


#Score Screen for the  players
game = turtle.Turtle()
game.speed()
game.shape("circle")
game.penup()
game.hideturtle()
game.color("green")
game.goto(0,270)
game.write("Player A = 0 || Player B = 0",align='center',font=('cursive',30,'normal'))



#Functions for movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 

def pad():
    wn.exitonclick()

#listen to the Keyboard commands
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')
wn.onclick(pad,btn=1,add=True)


while True:
    
    wn.update()
    

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)       # change the balls position on the screen 
    ball.sety(ball.ycor() + ball.dy)       # change in y coordinates


    #border checking for the ball

    if ball.ycor() > 290:
        ball.sety(290)          # for assign the value to that coordinates
        ball.dy *= -1           # reverse the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)              # for assign the value to that coordinates
        ball.dy *= -1   
    if ball.xcor() < -390:
        ball.goto(0,0)
        player_b_score += 20
        game.clear()
        game.write("Player A = {} || Player B = {},Winner = {}".format(player_a_score,player_b_score,max(player_a_score,player_b_score)),align='center',font=('cursive',30,'normal'))
        time.sleep(1)
        #Screen.textinput("b","name the score b")
    # for assign the value to that coordinates

        ball.dx *= -1 
    if ball.xcor() > 390:
        ball.goto(0,0)
        player_a_score += 20
        game.clear()
        game.write("Player A = {} || Player B = {} , Winner = {}".format(player_a_score,player_b_score,max(player_a_score,player_b_score)),align='center',font=('cursive',30,'normal'))
        time.sleep(2)              # for assign the value to that coordinates
        ball.dx *= -1 
        
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()- 50):
        ball.setx(340)
        ball.dx *= -1
        
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
       
        


