def karisikFonk(n1, n2, n3, *args, **kwargs):
    toplam1 = toplam2 = toplam3 = 0
    toplam1 = n1 + n2 + n3
    for n in args:
        toplam2 = toplam2 + n
    for k, v in kwargs.items():
        toplam3 = toplam3 + v

    toplam = [ toplam1, toplam2, toplam3]
    return toplam

t = karisikFonk(10, 20, 30, 11, 22, 33, 44, 55, elma=100, armut=200, karpuz=300)
print(t)
