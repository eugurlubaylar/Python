liste = [i for i in range(1856, 2347)]
fn = lambda x : x % 2
print(list(filter(fn, liste)))
