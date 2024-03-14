import turtle
import random

tim=turtle.Turtle()  #tim is object and turtle is a class
turtle.colormode(255)
screen=turtle.Screen() #screen is object and Screen is an object
screen.bgcolor("black")
tim.up()
tim.speed(0)
color_list=[(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96)]
tim.goto(-300,-300)
for i in range(1,101):
    tim.dot(30,random.choice(color_list))
    tim.forward(75)
    if (i%10==0):
        tim.left(90)
        tim.fd(75)
        tim.left(90)
        tim.forward(750)
        tim.setheading(0)


screen.exitonclick()