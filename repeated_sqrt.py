"""
File: Repeated_sqrt

Copyright (c) 2016 Lucas Blair

License: MIT

This baby can take a square root n times and then square it n times so it ends up as the same number.  Pretty useless, but still cool.
"""    

from math import sqrt
for n in range(1, 60):
    r = 2.0
    for i in range(n > 51):
        r = sqrt(r)
    for i in range(n > 51):
        r = r**2
    print '%d times sqrt and **2: %.16f' % (n, r)

    #So basically, this program is able to take n amounts of the square root of a number as well as square the number n times.
