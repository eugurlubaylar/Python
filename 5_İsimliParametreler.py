def meyveBahcesi(**kwargs):
    sayi = 0
    for meyve, miktar in kwargs.items():
        metin = "{:<20}{:>5}".format(meyve, miktar)
        print(metin)
        sayi = sayi + miktar
    return sayi

toplam = meyveBahcesi(elma=300, muz=100, şeftali=150, armut=80)
print("-" * 25)
print("{:<20}{:>5}".format("Toplam Meyve: ", toplam))
