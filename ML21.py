from turtle import *
import turtle

turtle.bgcolor('black')
turtle.pencolor('red')
turtle.speed(900)

def flower_design():
    for i in range(200):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
flower_design()
mainloop()