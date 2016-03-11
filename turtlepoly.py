n_str = raw_input ("How many sides do you want?:")
n = int(n_str)

l_str = raw_input ("Enter a side length:")
l = int(l_str)

import turtle

rico = turtle.Pen()

def draw_reg_polygon(t, num_sides, side_len):
    for i in range(num_sides):
        rico.forward(l)
        rico.left(360.0/n)

for j in range(1):
    draw_reg_polygon(rico, n, l)

inp = raw_input("Hit the <enter> key to quit!")

turtle.bye()
