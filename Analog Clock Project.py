from turtle import Turtle, Screen
import datetime

window = Screen()
window.title("Analog Digital Clock")
window.bgcolor("black")
window.setup(width=1000, height=800)
circle = Turtle()
circle.penup()
circle.pencolor("#118893")
circle.speed(0)
circle.pensize(25)
circle.hideturtle()
circle.goto(0, -390)
circle.pendown()
circle.fillcolor("#17202A")
circle.begin_fill()
circle.circle(400)
circle.end_fill()
hHand = Turtle()
hHand.shape("arrow")
hHand.color("white")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=18)
mHand = Turtle()
mHand.shape("arrow")
mHand.color("white")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)
sHand = Turtle()
sHand.shape("arrow")
sHand.color("dark red")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=36)
centerCircle = Turtle()
centerCircle.shape("circle")
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=1.5,
stretch_len=1.5)
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(170, 260)
pen.write("1", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(300, 140)
pen.write("2", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(340, -30)
pen.write("3", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(300, -200)
pen.write("4", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(170, -325)
pen.write("5", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(0, -370)
pen.write("6", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(-170, -325)
pen.write("7", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(-300, -200)
pen.write("8", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(-340, -30)
pen.write("9", align="center", font=("Algerian", 50,
"bold"))
pen.penup()
pen.hideturtle()
pen.goto(-280, 140)
pen.write("10", align="center", font=("Algerian",
50, "bold"))
pen.penup()
pen.hideturtle()
pen.goto(-160, 260)
pen.write("11", align="center", font=("Algerian",
50, "bold"))
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("12", align="center", font=("Algerian",
50, "bold"))


def moveHourHand():
 currentHourInternal = datetime.datetime.now().hour
 degree = (currentHourInternal - 15) * -30
 currentMinuteInternal = datetime.datetime.now().minute
 degree = degree + -0.5 * currentMinuteInternal
 hourHand.setheading(degree)
 wn.ontimer(moveHourHand, 60000)


# moving minute hand
def moveMinuteHand():
 currentMinuteInternal = datetime.datetime.now().minute
 degree = (currentMinuteInternal - 15) * -6
 currentSecondInternal = datetime.datetime.now().second
 degree = degree + (-currentSecondInternal * 0.1)
 minuteHand.setheading(degree)
 wn.ontimer(moveMinuteHand, 60000)


# moving second hand
def moveSecondHand():
 currentSecondInternal = datetime.datetime.now().second
 degree = (currentSecondInternal - 15) * -6
 secondHand.setheading(degree)
 wn.ontimer(moveSecondHand, 60000)