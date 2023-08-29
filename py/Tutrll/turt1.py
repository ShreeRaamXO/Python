import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    return r,g,b

directions=[0,70,180,270]
tim.pensize(20000)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(1)
    tim.setheading(random.choice(directions))

print("hi")

