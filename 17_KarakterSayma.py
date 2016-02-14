def karakterSay(*args):
    karakterListesi = {}

    for s in args:
        for k in s:
            k = k.upper()
            if(k in karakterListesi):
                karakterListesi[k] = karakterListesi[k] + 1
            else:
                karakterListesi[k] = 1
    return karakterListesi

liste = karakterSay("Erdem", "Batuhan", "İpek", "Aslı", "Ceyhun")
print(liste)
