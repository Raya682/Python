# Import the turtle module with all its functions
from turtle import *

# Create a new turtule object
turtle = Turtle()

# Set the objects speed (0 is the fastest speed)
turtle.speed(0)

# Set the background color of the window
bgcolor('black')

# Create a list of color for the pen to use
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

# Loop 120 times to draw the shape
for i in range(120):
    hideturtle()  # Hide the turtle cursor (optional)
    pencolor(colors[i % 6])  # Set the pen color to one of the colors in the list
                             # The color is chosen based on the remainder of i divided by 6
                             # This ensures that the colors cycle through the list
    forward(i * 2)  # Move the turtle forward
    right(61)  # Turn the turtle to the right 
    
# Keeps the window open
done()