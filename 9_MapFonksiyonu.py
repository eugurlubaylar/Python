liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fn = lambda x : x * x if x % 2 == 0 else x * 2
print(list(map(fn, liste)))
