import turtle
import turtle as t
import math
import itertools

# Set up the screen
t.Screen()
t.setup(810,710)
# t.hideturtle()
# t.tracer(False)
t.bgcolor('lightgreen')

master_turtle = turtle.Turtle()

master_turtle.color("black")
master_turtle.up()
master_turtle.goto(0,-50)
master_turtle.down()
# master_turtle.circle(50)

master_turtle.up()
master_turtle.goto(0,0)
t.tracer(0)

radius = 120

master_turtle.pensize(1)
color = itertools.cycle(['red', 'green', 'blue', 'black', 'purple'])
count = 0
x=0
y=0
for _ in range (0,3):
    count += 1
    for j in range(-200,201,200):
        for i in range(30,361,5):
            if count < 3:
                x = radius * math.cos(i)+j
                y = radius * math.sin(i)
            else:
                x = radius * math.cos(i)
                y = radius * math.sin(i)+j
            master_turtle.goto(x, y - radius)
            # master_turtle.dot(10)
            master_turtle.color(next(color))
            master_turtle.down()
            master_turtle.circle(radius)
            master_turtle.up()


t.done()

