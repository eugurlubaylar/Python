liste = [i for i in range(2367, 4578)]
fn = lambda x : x % 3 == 1
a =(list(filter(fn, liste)))
print(len(a))
print(a)

