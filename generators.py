import time

def get_1():
    yield 1
    time.sleep(2)

x = next(get_1())
print(x)
x = next(get_1())
print(x)
