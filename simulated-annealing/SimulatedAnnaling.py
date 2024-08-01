import random
import math
import numpy as np

class SimulatedAnnaling:
    def __init__(self, rate, T, model, T_min):
        self.rate = rate
        self.T = T
        self.T_min = T_min
        self.model = model

    def next_state(self, model):
        return self.model.next_state()

    def minimize(self):
        best_model = self.model
        while self.T > self.T_min:
            model_tplus1 = self.next_state(self)

            value_t = self.model.calculate()
            value_tplus1 = model_tplus1.calculate()

            delta = value_tplus1 - value_t

            if delta < 0:
                self.model = model_tplus1
                if value_tplus1 < best_model.calculate():
                    best_model = model_tplus1
            else:
                if np.log(random.uniform(0,1)) < (-delta/self.T):
                    self.model = model_tplus1

            self.T *= (1-self.rate)
            # print(self.T)
        return best_model

class Model:
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.f = f

    def next_state(self):
        return Model(self.x + random.uniform(-1, 1), self.y + random.uniform(-1, 1), self.f)
    
    def calculate(self):
        return self.f(self.x, self.y)
    
    def toString(self):
        print(f"x:{self.x}\ny:{self.y}\nf:{self.f(self.x, self.y)}")
    
def function(x, y):
    return x**2 + y**2

def main():
    model = Model(random.uniform(-1, 1), random.uniform(-1, 1), function)

    sa = SimulatedAnnaling(0.0001, 10000, model, 0.000000001)

    model = sa.minimize()

    model.toString()
main()
    



