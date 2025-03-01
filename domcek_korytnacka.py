import turtle
import random

t = turtle.Turtle()
pole = []

def domcek (strana):
    t.pencolor("#{:06x}". format(random.randrange(200 ** 3)))
    for i in range (4):
        t.fd(strana)
        t.lt(90)
    t.pu()
    t.lt(90)
    t.fd(strana)
    t.rt(30)
    t.pd()

    t.pencolor("#{:06x}". format(random.randrange(200 ** 3)))
    for i in range(2):
        t.fd(strana)
        t.rt(120)
        
    t.pu()
    t.lt(180)
    t.fd(strana)
    t.pd() 
 
def ulica(pole):
    t.pu()
    t.setpos(-turtle.window_width() //2 + 10, 0)
    t.pd()
    for strana in pole:
        domcek(strana)

ulica([60, 50, 40, 30, 20, 10])
