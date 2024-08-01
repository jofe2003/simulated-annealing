from sa.SimulatedAnnaling import *
from model.Model import *
    
def function(x, y):
    return x**2 + y**2

def program():
    model = Model(random.uniform(-1, 1), random.uniform(-1, 1), function)

    sa = SimulatedAnnaling(0.0001, 10000, model, 0.000000001)

    model = sa.minimize()

    model.toString()
program()
    