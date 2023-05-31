from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(2)
h=0
n=80

for i in range(180):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h+=1/n
    begin_fill()
    circle(180-i,70)
    lt(80)
    circle(180-i,70)
    rt(20)

    for j in range(4):
        rt(60)
    lt(120)
    end_fill()
done()

