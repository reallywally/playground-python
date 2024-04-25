# simple generator
def number_generator():
    yield 0
    yield 1
    yield 2


ng = number_generator()

print(next(ng))
print(next(ng))
print(next(ng))


# generator with loop
def counter():
    print("I'm counter")
    i = 0

    while True:
        yield i
        i += 1


count = counter()
print(next(count))
print(next(count))
print(next(count))


# generator with class
class Counter:
    def __init__(self):
        print("I'm counter")
        self.i = 0

    def __next__(self):
        print(self.i)
        self.i += 1


counter_class = Counter()

next(counter_class)
next(counter_class)
next(counter_class)