import turtle
import random

# Function to draw a branch
def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Function to draw a cherry
def draw_cherry(t):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-150, 150))
    t.pendown()
    t.dot(10, "red")

# Setup turtle
t = turtle.Turtle()
t.speed("fastest")  # Set turtle speed to fastest
t.hideturtle()  # Hide turtle

# Draw trunk
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()
t.color("brown")
t.pensize(20)
t.forward(100)

# Draw tree branches
t.pensize(5)
t.color("green")
draw_branch(80, t)

# Draw cherries
t.color("red")
for _ in range(20):
    draw_cherry(t)



turtle.done()
