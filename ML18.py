import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(2)
t.pensize(2)
h = 0

for i in range(200):
    color  = colorsys.hsv_to_rgb(h,0.8,1)
    h+=0.006
    t.pencolor(color)
    t.left(179)
    t.backward(i*0.3)
    t.circle(i*0.3,120)
    t.right(14)
    t.forward(i*0.3)
    t.circle(i*0.3,120)
t.done()



