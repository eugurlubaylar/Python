import functools
liste = [10, 43, 32, 85, 65, 66, 75, 74]
fn = lambda x, y : x if x > y else y
print(functools.reduce(fn, liste))
