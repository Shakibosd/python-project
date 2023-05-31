from turtle import *
import colorsys
speed(0)
pensize(1)
bgcolor('black')
h=0.4

for i in range(140):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    for j in range(5):
        fd(i)
        rt(20)
        rt(80)
    rt(140)
done()