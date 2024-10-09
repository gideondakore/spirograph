from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
tim.shape("arrow")
tim.color("PaleGreen4")

# SPIROGRAPH
t.colormode(255)
tilt_angle = 5
loop_count = int(360/tilt_angle)
tim.speed(10)

def rand_colors_spirograph():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for i in range(1, loop_count+1):
    tim.tiltangle(tilt_angle*i)
    tim.pencolor(rand_colors_spirograph())
    tim.circle(100)
    tim.setheading(tim.tiltangle())
    # tim.tilt(tilt_angle*i)


screen = Screen()
screen.exitonclick()