"""
File: Turtlestar

Copyright (c) 2016 Lucas Blair

License: MIT

This one can draw a star with any odd number of points you input.  
"""    

n_str = raw_input ("How many points do you want?:")
n = int(n_str)

l_str = raw_input ("Enter a side length:")
l = int(l_str)

import turtle

rico = turtle.Pen()

def draw_a_star(t, num_points, sid_len):
    for i in range(num_points):
        rico.forward(l)
        rico.left(180.0-(180.0/n))


for j in range(1):
    draw_a_star(rico, n, l)

inp = raw_input("Hit <enter> to quit!")

turtle.bye()
