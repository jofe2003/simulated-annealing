import random
import math
from plot.Plot import Plot

def function(x, y):
    return (x-1)**2+(y-1)**2



def program():
    rate = 0.001
    temp_init = 100000
    temp_min = 0.00000001

    
    x_t = random.random()
    y_t = random.random()

    x = []
    y = []
    z = []
    while temp_min < temp_init:
        x_tplus1 = x_t + random.uniform(-1, 1)
        y_tplus1 = y_t + random.uniform(-1, 1)

        value_t = function(x_t, y_t)
        value_tplus1 = function(x_tplus1, y_tplus1)

        x.append(x_t)
        y.append(y_t)
        z.append(value_t)

        delta = value_t - value_tplus1

        if delta > 0:
            x_t = x_tplus1
            y_t = y_tplus1
        else:
            if math.log1p(-random.uniform(0, 1)) < delta / temp_init:
                x_t = x_tplus1
                y_t = y_tplus1

        temp_init = temp_init*(1-rate)
    plot = Plot()
    plot.plot(x[::10], y[::10], z[::10], function)

program()

