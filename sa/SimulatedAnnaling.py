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
        return best_model