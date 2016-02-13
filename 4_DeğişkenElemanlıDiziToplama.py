def seriSayiTopla(*args):
    toplamListe = []

    for s in args:
        toplam = 0
        for i in s:
            toplam = toplam + i
        toplamListe.append(toplam)

    return toplamListe


t = seriSayiTopla([1,2,3,4], [10, 20, 30], [111, 222, 333, 444, 555], [10, -1])
print("Toplam =", t)
