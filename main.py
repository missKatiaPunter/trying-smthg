import turtle
from random import randint

wn=turtle.Screen()
my_turtle=turtle.Turtle()
my_circle=turtle.Turtle()

my_circle.speed(0)
my_circle.pensize(12)
# wn.colormode(255)
my_circle.hideturtle()
my_turtle.shape('turtle')
my_turtle.speed(7)
my_circle.penup() 
my_circle.goto(randint(-300, 300), randint(-200, 170))  
my_circle.color(randint(0, 255),
      randint(0, 255),
      randint(0, 255))       
my_circle.begin_fill()       
my_circle.circle(10)         
my_circle.end_fill()         
my_circle.penup()       
my_circle.pendown()

def up():
    my_turtle.setheading(90)
    my_turtle.fd(5)
def left():
  if my_turtle.xcor()>-250:
    my_turtle.setheading(180)
    my_turtle.fd(5)
def right():
    my_turtle.setheading(0)
    my_turtle.fd(5)
def down():
    my_turtle.setheading(270)
    my_turtle.fd(5)
wn.onkey(up,'Up')
wn.onkey(left,'Left')
wn.onkey(right,'Right')
wn.onkey(down,'Down')
wn.listen()
wn.mainloop()