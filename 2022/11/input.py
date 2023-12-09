class Monkey0:
    items = [54, 53]
    operation = lambda self, old: old * 3
    divider = 2
    targets = [2, 6]
    inspections = 0

class Monkey1:
    items = [95, 88, 75, 81, 91, 67, 65, 84]
    operation = lambda self, old: old * 11
    divider = 7
    targets = [3, 4]
    inspections = 0

class Monkey2:
    items = [76, 81, 50, 93, 96, 81, 83]
    operation = lambda self, old: old + 6
    divider = 3
    targets = [5, 1]
    inspections = 0

class Monkey3:
    items = [83, 85, 85, 63]
    operation = lambda self, old: old + 4
    divider = 11
    targets = [7, 4]
    inspections = 0

class Monkey4:
    items = [85, 52, 64]
    operation = lambda self, old: old + 8
    divider = 17
    targets = [0, 7]
    inspections = 0

class Monkey5:
    items = [57]
    operation = lambda self, old: old + 2
    divider = 5
    targets = [1, 3]
    inspections = 0

class Monkey6:
    items = [60, 95, 76, 66, 91]
    operation = lambda self, old: old * old
    divider = 13
    targets = [2, 5]
    inspections = 0

class Monkey7:
    items = [65, 84, 76, 72, 79, 65]
    operation = lambda self, old: old + 5
    divider = 19
    targets = [6, 0]
    inspections = 0

monkeys = [
    Monkey0(),
    Monkey1(),
    Monkey2(),
    Monkey3(),
    Monkey4(),
    Monkey5(),
    Monkey6(),
    Monkey7(),
]
