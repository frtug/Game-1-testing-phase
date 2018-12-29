import turtle
import time
import random
from tkinter import messagebox
delay = 0.1

s = 0

score = 0
highscore = 0
#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('Red')
food.penup()
food.goto(0,100)

# speed of the snake

sp = turtle.Turtle()
sp.speed(0)
sp.shape('square')
sp.color('blue')
sp.penup()
sp.hideturtle()
sp.goto(275,260)
sp.write("Speed = 0",align ='right',font=('Cursive',15,'normal'))



wn = turtle.Screen()
wn.title('Game')
wn.bgcolor('Black')
wn.setup(width=600, height=600)
wn.tracer(0) #turn off the screen updates

#HEAd of the snake
#
head = turtle.Turtle()
head.speed(1)
head.shape('circle')
head.color('Yellow')
head.penup()
head.goto(100,100)
head.direction = "stop"
segments = []

# Soring for the User
run = turtle.Turtle()
run.speed(0)
run.color('Red')
run.shape('square')
run.penup()
run.hideturtle()
run.goto(0,260)
run.write("Score = 0 HighScore = 0",align = 'center',font=("courier",24,"normal"))

#Functions
def go_up():
   if head.direction != "down":
    head.direction = "up"
def go_down():
   if head.direction != "up":
    head.direction = "down"
def go_left():
   if head.direction != "right":
    head.direction = "left"
def go_right():
   if head.direction != "left":
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

# Main game loop
while True:
    wn.update()



    # check for collisions
    if head.xcor() >290 or head.xcor() <-290 or head.ycor() >260 or head.ycor() <-290:
        msg = messagebox.showinfo("Game Over","You are Out")

        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        delay = 0.1
       # msg = messagebox.showinfo("Game Over","You loose")
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        #reset the score
        s = 0
        score = 0
        run.clear()
        run.write("Score: {}  HighScore :{}".format(score, highscore), align="center", font=("Courier", 24, 'normal'))

        sp.clear()
        sp.write("Speed = {}".format(s),align="right",font=('cursive', 15, 'normal'))

    if head.distance(food) <= 20:
        # move random
        x = random.randint(-245, 245)
        y = random.randint(-245, 245)
        food.goto(x,y)
        s = s + 0.00001
        delay = delay - s

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        score += 10
        if score >= highscore:
            highscore = score
        run.clear()
        run.write("Score: {}  HighScore :{}".format(score,highscore),align="center",font=("Courier",24,'normal'))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)




    # move segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    # Collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            msg = messagebox.showinfo("Game Over", "You are out")

            time.sleep(1)
            head.goto(0,0)
            head.direction == "stop"

            s = 0
            sp.clear()
            sp.write("Speed = {}".format(s),align="right",font=('cursive',15,'normal'))
            delay = 0.1

            for segment in segments:
              segment.goto(1000,1000)
            segments.clear()
            score = 0
            run.clear()
            run.write("Score: {}  HighScore :{}".format(score, highscore), align="center",font=("Courier", 24, 'normal'))

    time.sleep(delay)
    # quit for enter the q

#
wn.mainloop()
