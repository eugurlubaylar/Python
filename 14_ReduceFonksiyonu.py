import functools
liste = [10, 20, 30, 40, 50]
fn = lambda x, y : x + y
print(functools.reduce(fn, liste))
