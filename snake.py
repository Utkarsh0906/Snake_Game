from turtle import Turtle

class Snake:
    head = None
    turtles = []
    S_POSITION = [(0,0),(-20,0),(-40,0)]
    MOVE = 20
    
    #creating snake
    def __init__(self):
        for i in self.S_POSITION:
            t = Turtle("square")
            t.penup()
            t.color("White")
            t.goto(i)
            self.turtles.append(t)
        self.head = self.turtles[0]
        self.head.shape("arrow")
        

    
    #changing direction of snake
    def turn_leftwards(self):
        if(self.head.heading() != 0):
            self.head.setheading(180)
    def turn_rightwards(self):
        if(self.head.heading() != 180):
            self.head.setheading(0)
    def turn_downwards(self):
        if(self.head.heading() != 90):
            self.head.setheading(270)
    def turn_upwards(self):
        if(self.head.heading() != 270):
            self.head.setheading(90)

    #moving snake
    def move(self):
        head = self.head
        for i in range(len(Snake.turtles)-1,0,-1):
            Snake.turtles[i].goto(Snake.turtles[i-1].pos())
        head.forward(self.MOVE)
    
    #increasing snake length
    def extend(self):
        t = Turtle("square")
        t.penup()
        t.color("White")
        self.turtles.append(t)
              