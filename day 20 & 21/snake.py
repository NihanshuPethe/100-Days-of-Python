import turtle
import random
screen=turtle.Screen()


START_POSITION=[(0,0),(-20,0),(-40,0)]
color_of_snake=["red","orange","yellow","green","blue","purple","pink"]
UP=90
DOWN=270
LEFT=180
RIGHT=0
I=-1
class Snake:
    def __init__(self) :
        self.segment=[]
        self.I=-1
        self.construct_a_snake()
        self.head = self.segment[0]

    def construct_a_snake(self):     #create 3 object
        # create a snake
        for Position in START_POSITION:
            self.add_segment(Position)
    
    def add_segment(self,position): #create an actual snake object and place it on given position 
        new_segment=turtle.Turtle("square")
        self.I+=1
        colour=color_of_snake[self.I%7]
        new_segment.color(colour)
        new_segment.up()
        new_segment.goto(position)
        self.segment.append(new_segment)
        # self.move()
    #Extend the snake
    def extend(self):
        self.add_segment(self.segment[-1].position())      # This function gives the position of the last segment of the snake
    #Continous Movement of Snake
    def move(self):                               # IMP logic
        for i in range(len(self.segment)-1,0,-1):
            new_x=self.segment[i-1].xcor() 
            new_y=self.segment[i-1].ycor()
            self.segment[i].goto(new_x,new_y)
        self.segment[0].fd(20)

    def reset_snake(self):
        for i in self.segment:
            i.goto(1000,1000)
        self.segment.clear()
        self.construct_a_snake()
        self.head= self.segment[0]
    # Snake Movement 
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)

