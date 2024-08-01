import random


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