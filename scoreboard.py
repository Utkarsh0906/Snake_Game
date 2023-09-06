from turtle import Turtle
import os
if not os.path.isfile("score.txt"):
    file = open("score.txt","w+")
    file.write("0")
    file.close()

file = open("score.txt","r+")
    
class ScoreBoard(Turtle):
    
    #creating scoreboard
    high_score = int(file.readline())
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
        if(self.score>self.high_score):
            self.high_score = self.score
            file.seek(0)
            file.truncate()
            file.write(str(self.high_score))
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!!",align = "Center",font = ("Arial",50,"bold"))
        self.goto(0,-50)
        self.write(f"Score = {self.score}",align = "Center",font = ("Arial",25,"bold"))
        self.goto(0,-100)
        self.write(f"High Score = {self.high_score}",align = "Center",font = ("Arial",25,"bold"))
    
    def __del__(self):
        file.close()
        
