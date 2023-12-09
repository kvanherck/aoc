class Monkey0:
    items = [79, 98]
    operation = lambda self, old: old * 19
    divider = 23
    targets = [2, 3]
    inspections = 0

class Monkey1:
    items = [54, 65, 75, 74]
    operation = lambda self, old: old + 6
    divider = 19
    targets = [2, 0]
    inspections = 0

class Monkey2:
    items = [79, 60, 97]
    operation = lambda self, old: old * old
    divider = 13
    targets = [1, 3]
    inspections = 0

class Monkey3:
    items = [74]
    operation = lambda self, old: old + 3
    divider = 17
    targets = [0, 1]
    inspections = 0

monkeys = [
    Monkey0(),
    Monkey1(),
    Monkey2(),
    Monkey3(),
]
