#importing necessary modules
from turtle import Turtle
import os

#creating file to store high scores
if not os.path.isfile("score.txt"):
    file = open("score.txt","w+")
    file.write("0")
    file.close()

#opening file to store high scores
file = open("score.txt","r+")
    
class ScoreBoard(Turtle):
    
    #creating scoreboard
    high_score = int(file.readline()) #extracting previous high score 
    score = -1
    def __init__(self):
        super().__init__()
        self.color("Red")
        self.penup()
        self.hideturtle()
        self.new_score()
    
    #updating scoreboard
    def new_score(self):    
        self.score += 1
        self.clear()
        self.goto(0,300)
        self.write(f"Level = {self.score}",align = "Center",font = ("Arial",24,"bold"))
        self.goto(140,300)
        self.write(f"High Score = {self.high_score}",align = "Left", font = ("Arial",16,"bold"))
    
    #displaying gameover
    def game_over(self):
        #updating high score
        if(self.score>self.high_score):
            self.high_score = self.score
            file.seek(0)
            file.truncate()
            file.write(str(self.high_score))

        #displaying gameover screen
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!!",align = "Center",font = ("Arial",50,"bold"))
        self.goto(0,-50)
        self.write(f"Score = {self.score}",align = "Center",font = ("Arial",25,"bold"))
        self.goto(0,-100)
        self.write(f"High Score = {self.high_score}",align = "Center",font = ("Arial",25,"bold"))
    
    #closing the opened file
    def __del__(self):
        file.close()
        
