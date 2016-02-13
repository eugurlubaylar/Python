def ozelRange(ilk, son, artis):
    i = ilk
    while(i < son):
        yield i
        i = i + artis

r = ozelRange(0, 100, 5)
print(type(r))
for i in r:
    print(i, end=" ")
