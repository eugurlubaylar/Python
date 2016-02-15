BUFFSIZE = 25000

iDosyaIsim = "C://Users//Erdem//Desktop//IPython//testFiles//deneme.jpg"
oDosyaIsim = "C://Users//Erdem//Desktop//IPython//testFiles//deneme-2.jpg"

iDosya = open(iDosyaIsim, "rb")
oDosya = open(oDosyaIsim, "wb")

buffer = iDosya.read(BUFFSIZE)

while(len(buffer)):
    oDosya.write(buffer)
    print("{} byte {} ' ya yazıldı.".format(len(buffer), oDosyaIsim, flush=True))
    buffer = iDosya.read(BUFFSIZE)

print("İşlem başarıyla tamamlandı")
