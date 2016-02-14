liste1 = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]
fn = lambda x, y : x * y
print(list(map(fn, liste1, liste2)))

