from turtle import Turtle

ALLIGMENT="center"
FONT=("Arial",12,"normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()   #Intake the turtle class 
        self.score=0
        self.high=0
        with open ("data.txt",mode= "r") as data:
            self.high=int(data.read())
        self.hideturtle()
        self.up()
        self.goto(0,280)
        self.color("white")        
        self.print_score()

    def print_score(self):
        self.clear()           # Clear the screen
        self.write(f"Score {self.score} High Score {self.high}",align=ALLIGMENT,font=FONT)
    
    def score_increase(self):  # Print Current Score
        self.score+=1          #increament the score 
        self.print_score()     #Print the current score

    def reset_high_score(self):
        if self.score > self.high:
            self.high=self.score
        with open("data.txt",mode='w') as data:
            data.write(f"{self.high}")
        self.score=0
        self.print_score()

        
