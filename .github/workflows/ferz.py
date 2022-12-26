import turtle as t
SIZE=50

import queen_class
queen8=queen_class.Queen(8)
res = queen8.get_result()
#########################################
def square(x,y,z):
    t.penup()
    t.goto(x,y)
    t.pendown()

    if z%2==1:
        t.color('black','hot pink')
    else:
        t.color('black','plum1')

    t.begin_fill()

    for i in range(4):
        t.forward(SIZE)
        t.left(90)

    t.end_fill()

#########################################
def rectangle(x,y,w,h):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()

    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

    t.end_fill()


def polyline(p):
    t.penup()
    t.goto(p[0][0],p[0][1])
    t.pendown()
    t.begin_fill()
    for c in p:
        t.goto(c[0],c[1])
    t.end_fill()

def queen(x,y,z):

    if z%2==0:
        t.color('black','gray89')
    else:
        t.color('black','gray60')

    rectangle(x+SIZE*0.1, y+SIZE*0.1, SIZE*0.8, SIZE*0.1)
    rectangle(x+SIZE*0.15, y+SIZE*0.2, SIZE*0.7, SIZE*0.1)

    p=((x+SIZE*0.15, y+SIZE*0.3),
       (x+SIZE*0.10, y+SIZE*0.4),
       (x+SIZE*0.90, y+SIZE*0.4),
       (x+SIZE*0.85, y+SIZE*0.3))
    polyline(p)

    p=((x+SIZE*0.10, y+SIZE*0.4),
       (x+SIZE*0.01, y+SIZE*0.95),
       (x+SIZE*0.30, y+SIZE*0.4),
       (x+SIZE*0.50, y+SIZE*0.95),
       (x+SIZE*0.70, y+SIZE*0.4),
       (x+SIZE*0.99, y+SIZE*0.95),
       (x+SIZE*0.9, y+SIZE*0.4))
    polyline(p)
#########################################

t.tracer(0)
t.hideturtle()
for j in range(8):
    for k in range(8):
        x=j*SIZE-4*SIZE
        y=k*SIZE-4*SIZE
        z=j*7+k
        square(x,y,z)
        if res[j][k] == 1:
            queen(x,y,z)
t.update()
