#Steve
#10.17.23

import turtle
#get the input of informations: length, colors
lgth = float(input('whaat is length'))
sd = input('what\'s the color')
ct = input('what\'s the color')


def hex(cl, lg):
    '''
    function that draws central hexagon. take color and length as parameter to draw hexagon
    :return:
    '''
    turtle.begin_fill()
    turtle.fillcolor(cl)
    for a in range(6):
        turtle.forward(lg)
        turtle.right(60)
    turtle.end_fill()
def side_hex(cl):
    '''
    draws peripheral hexagons. take color as parameter and draw hexagon
    :return:
    '''
    for a in range(6):
        turtle.begin_fill()
        turtle.fillcolor(cl)
        for a in range(6):
            turtle.forward(lgth)
            turtle.left(60)
        turtle.forward(lgth)
        turtle.right(60)
        turtle.end_fill()
def draw_hex():
    '''
    draw full hexagon using two hexagon functions. no parameter, draw full hexagon
    :return:
    '''
    turtle.left(60)
    hex(ct, lgth)
    side_hex(sd)


draw_hex()

turtle.exitonclick()