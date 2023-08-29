import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("slow")

tim.penup()
tim.hideturtle()

color_list=[(191, 79, 15), (213, 84, 210), (234, 241, 117), (35, 88, 65), (190, 84, 80), (41, 130, 30),
            (147, 174, 12), (66, 239, 169), (72, 188, 148), (83, 171, 5), (177, 18, 49), (228, 0, 96),
            (58, 174, 38), (241, 66, 158), (76, 155, 25), (86, 42, 246), (106, 185, 233), (190, 173, 76),
            (230, 72, 71), (81, 113, 234)]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)

number_of_dots=100
for dot_count in range(1,number_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()