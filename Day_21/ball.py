from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        #The ball is the default size#self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def bounce(self):
        self.y_move *= -1
        self.x_move *= -1
        
        
      