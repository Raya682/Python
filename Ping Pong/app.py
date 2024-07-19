from turtle import *

class PingPong:
    
    def __init__(self):
        self.window = Screen()  # Intialize screen
        self.window.title("Ping Pong Game")  # Set the title of the window
        self.window.bgcolor("black")  # Set the background-color of the window
        self.window.setup(width=800, height=600)  # Set the width and height of the window
        self.window.tracer(0)   # Stops the window from updating automatically
        
        self.game_started = False
            
        # Display start message
        self.start_msg = Turtle()
        self.start_msg.speed(0)
        self.start_msg.color("white")
        self.start_msg.penup()
        self.start_msg.hideturtle()
        self.start_msg.goto(0,0)
        self.start_msg.write("Press SPACE to start the game", align="center", font=("Courier", 24, "normal"))
        
        # Players
        self.player1 = Turtle()  # Intializes turtle object(shape)
        self.player1.speed(0)  # Set the speed of the animation
        self.player1.shape("square")  # Set the shape of the object
        self.player1.color("blue")  # Set the color of the object
        self.player1.shapesize(stretch_wid=5, stretch_len=1)  # Stretches the shape to meet the size
        self.player1.penup()  # Stops the object from drawing lines
        self.player1.goto(-370, 0)  # The position of the object
        
        self.player2 = Turtle()
        self.player2.speed(0)
        self.player2.shape("square")
        self.player2.color("red")
        self.player2.shapesize(stretch_wid=5, stretch_len=1)
        self.player2.penup()
        self.player2.goto(370, 0)
        
        # Ball
        self.ball = Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.5
        self.ball.dy = -0.5
        
        # Score
        self.score1 = 0
        self.score2 = 0
        self.score = Turtle()
        self.score.speed(0)
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 260)
        self.update_score()
                    
        # Keyboard Bindings
        self.window.listen()  # Tells the window to expect keyboard input
        self.window.onkeypress(self.player1_up, "w")
        self.window.onkeypress(self.player1_down, "s")
        self.window.onkeypress(self.player2_up, "Up")
        self.window.onkeypress(self.player2_down, "Down")
        self.window.onkeypress(self.start_game, "space")
        
        self.main_game_loop()
        
    def start_game(self):
            self.game_started = True
            self.start_msg.clear()
            
    def player1_up(self):
        y = self.player1.ycor()
        if y < 250:
            self.player1.sety(y + 20)
            
    def player1_down(self):
        y = self.player1.ycor()
        if y > -240:
            self.player1.sety(y - 20)
            
    def player2_up(self):
        y = self.player2.ycor()
        if y < 250:
            self.player2.sety(y + 20)
            
    def player2_down(self):
        y = self.player2.ycor()
        if y > -240:
            self.player2.sety(y - 20)
        
    def update_score(self):
        self.score.clear()
        self.score.write("Player 1: {} Player 2: {}".format(self.score1, self.score2), 
                         align="center", font = ("Courier", 24, "normal"))

    # Main Game Loop
    def main_game_loop(self):
        while True:
            self.window.update()
            
            if self.game_started:
                # Starts at 0 and everytime the loop runs the x-axis is increased by the value of dx
                self.ball.setx(self.ball.xcor() + self.ball.dx)
                # Starts at 0 and everytime the loop runs the y-axis is increased by the value of dy
                self.ball.sety(self.ball.ycor() + self.ball.dy)
                
                # If the ball hit the top border
                if self.ball.ycor() > 290 or self.ball.ycor() < -290: 
                    self.ball.dy *= -1 
                
                # If ball hits the right border
                if self.ball.xcor() > 390: 
                    self.ball.goto(0, 0)
                    self.ball.dx *= -1
                    self.score1 += 1
                    self.update_score()
                
                if self.ball.xcor() < -390:
                    self.ball.goto(0,0)
                    self.ball.dx *= -1
                    self.score2 += 1
                    self.update_score()
                
                # Ball Collision
                if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and \
                    (self.ball.ycor() < self.player2.ycor() + 50 and self.ball.ycor() > self.player2.ycor() - 50):
                    self.ball.setx(340)
                    self.ball.dx *= -1.1
    
                if (self.ball.xcor() < -340 and self.ball.xcor() > -350) and \
                    (self.ball.ycor() < self.player1.ycor() + 50 and self.ball.ycor() > self.player1.ycor() - 50):
                    self.ball.setx(-340)
                    self.ball.dx *= -1.1
                
ping_pong = PingPong()