def degSay(*args):
    toplam = 0
    for n in args:
        toplam = toplam + n
    return toplam

t = degSay(10, 40, 50, 60)
print("Toplam =", t)
