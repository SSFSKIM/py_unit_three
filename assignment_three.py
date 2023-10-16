#Steve
#10.17.23

import turtle

lgth = float(input('whaat is length'))
sd = input('what\'s the color')
ct = input('what\'s the color')


def hex():
    turtle.begin_fill()
    turtle.fillcolor(ct)
    for a in range(6):
        turtle.forward(lgth)
        turtle.right(60)
    turtle.end_fill()
def side_hex():
    for a in range(6):
        turtle.begin_fill()
        turtle.fillcolor(sd)
        for a in range(6):
            turtle.forward(lgth)
            turtle.left(60)
        turtle.forward(lgth)
        turtle.right(60)
        turtle.end_fill()
def draw_hex():
    turtle.left(60)
    hex()
    side_hex()


draw_hex()

turtle.exitonclick()