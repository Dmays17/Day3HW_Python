# functional Prompt

def flatten(*array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    print(arr)
    return sorted(arr)

# How does this solution ensure data immutability?
# Is this solution a pure function? Why or why not?
# Yes
# Is this solution a higher order function? Why or why not?
# This is not a higher order function
# Would it have been easier to solve this problem using a different programming style?
# no
# Why in particular is functional programming a helpful paradigm when solving this problem?

# Object Oriented


class Podracer():
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = 'trashed'


flatten([161, 77, 88], [25, 88, 99])
