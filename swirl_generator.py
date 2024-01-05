"""Generate cool swirl art-work
Keys:
r - generate new design by re-randomizing parameters
up/down - change the angle inputs (changes design)
left/right - changes distance of lines, the effect is either rotation or design modification depending on whether loop 1 is activated.
1 - activate loop 1. Adds complexity to the design"""

import turtle as t
import math
import random
import itertools

# Set up the screen
t.Screen()
t.setup(810,710)
# t.hideturtle()
# t.tracer(False)
t.bgcolor('lightgreen')
color = itertools.cycle(['red', 'green', 'blue', 'black', 'purple'])

master_turtle = t.Turtle()
t.tracer(0)

master_turtle.down()


class Swirl(t.Turtle):
    def __init__(self, angle, move, p1,p2):
        super().__init__()


    def reset_params(self):
        p1 = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
              random.randint(1, 100)]
        p2 = [0, math.cos(random.randint(10, 100)), 1, math.sin(random.randint(10, 100)), 8]
        master_turtle.clear()
        master_turtle.goto(0, 0)




    def draw(self):
        pass



class keyboard(t.Turtle):
    def __init__(self,p1,p2, angle, forward):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.angle = angle
        self.forward = forward

    def change_angle(self):
        pass



params = []
angle = 90
forward = 5
loop1 = False
loop2 = False
def reset_params():
    global angle
    global forward
    global loop1
    loop1 = False
    angle = 90
    forward = 5
    params.clear()
    p1 = [random.randint(1,100),random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100)]
    p2 = [0, math.cos(random.randint(10,100)), 1, math.sin(random.randint(10,100)),8]
    master_turtle.clear()
    master_turtle.goto(0,0)
    params.append(p1)
    params.append(p2)
    draw_swirl(p1,p2, angle, loop1=False)


    # master_turtle.clear()
    # master_turtle.goto(0,0)
    # draw_swirl(p1, p2)
    # t.update()


def change_angle(dir):
    global angle
    global forward
    global loop1
    if dir == 'up':
        # print(angle)
        angle +=1
        master_turtle.clear()
        master_turtle.color(next(color))
        master_turtle.goto(0, 0)
        draw_swirl(params[0], params[1], angle, forward, loop1 = loop1)
        print(loop1)

    if dir == 'down':
        # print(angle)
        angle -=1
        master_turtle.clear()
        master_turtle.color(next(color))
        master_turtle.goto(0, 0)
        draw_swirl(params[0], params[1], angle , forward, loop1=loop1)

def change_forward(dir):
    global angle
    global forward
    global loop1
    if dir == 'left':
        forward -=1
        master_turtle.clear()
        master_turtle.color(next(color))
        master_turtle.goto(0,0)
        draw_swirl(params[0], params[1], angle, forward, loop1=loop1)
    if dir == 'right':
        print('right')
        forward +=1
        master_turtle.clear()
        master_turtle.color(next(color))
        master_turtle.goto(0,0)
        draw_swirl(params[0], params[1], angle, forward , loop1=loop1)

def init_loop1():
    global angle
    global forward
    global loop1
    if not loop1:
        loop1 = True
    else:
        loop1 = False
    master_turtle.clear()
    master_turtle.color(next(color))
    master_turtle.goto(0, 0)
    draw_swirl(params[0], params[1], angle, forward, loop1=loop1)

def init_loop2():
    global loop2
    if not loop2:
        loop2 = True
    else:
        loop2 = False
    master_turtle.clear()
    master_turtle.color(next(color))
    master_turtle.goto(0, 0)
    draw_swirl(params[0], params[1], loop2=loop2)




def draw_swirl(a,b, n = 90, m=5, loop1 = False, loop2 = False):
    p1 = itertools.cycle(a)
    p2 = itertools.cycle(b)
    # print(n,m)
    print('*', loop1)
    master_turtle.color(next(color))
    for i in range(2,2000):
        master_turtle.color(next(color))
        master_turtle.forward(m+i/12)
        master_turtle.right(n/math.cos(next(p2)))
        master_turtle.forward(i/8)

        if loop1 == True:
            for j in range(4):
                master_turtle.left(next(p1)-m*math.cos(next(p2)))
                if i %2 == 0:
                    master_turtle.forward(math.cos(next(p1)))

        # if loop2 == True:
            # for j in range(10):
            #     # if i%2==0:
            #     #     master_turtle.goto(0,0)
            #     master_turtle.right(n / math.log(10, 7 + math.tan(next(p1))))

t.listen()
t.onkey(reset_params, "r") #reset to random parameters
t.onkey(lambda dir = 'up' :change_angle('up'), "Up")
t.onkey(lambda dir = 'down' :change_angle('down'), "Down")
t.onkey(lambda dir = 'left' :change_forward('left'), "Left")
t.onkey(lambda dir = 'right' :change_forward('right'), "Right")

t.onkey(init_loop1, '1')
t.onkey(init_loop2, '2')


t.getcanvas().postscript(file='test10.eps')

t.done()