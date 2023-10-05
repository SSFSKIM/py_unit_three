#Steve
#10.05.23

import math
a = int(input('what\' one side '))
b = int(input('what\'s the other side?'))
c = int(input('what\s the last side?'))

def tr_a(x, y, z):
    s = (x+y+z)/2
    print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
tr_a(a, b, c)