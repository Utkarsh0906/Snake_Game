#importing libraries
from turtle import Screen,Turtle
from snake import Snake
from food import Food  
from scoreboard import ScoreBoard
import time      
        
#settting up screen
screen = Screen()
screen.setup(700,700)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

#creating objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#moving snake
game_on = True
while(game_on):
    snake.move()
    screen.update()
    time.sleep(0.09)  
    head = snake.head
    
    #Wall Collision
    if(head.xcor()>=330 or  head.xcor()<= -330 or head.ycor()>=330 or head.ycor()<= -330): #stop the snake when it reaches the border
        game_on = False
        scoreboard.game_over()
    
    #Food Acquired
    if(head.distance(food)<20):
        food.new_food()
        scoreboard.new_score()
        snake.extend()
    
    #Tail Collision
    for i in snake.turtles[1:]:
        if(head.distance(i)<10):
            game_on = False
            scoreboard.game_over()
        
    #changing direction     
    screen.onkey(key="Right", fun=snake.turn_rightwards)
    screen.onkey(key="Left", fun=snake.turn_leftwards)
    screen.onkey(key="Up", fun=snake.turn_upwards)
    screen.onkey(key="Down", fun=snake.turn_downwards)

#exiting turtle
screen.exitonclick()    



