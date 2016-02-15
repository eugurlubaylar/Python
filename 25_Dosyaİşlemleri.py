BUFFSIZE = 30000

iDosyaIsim = "C://Users//Erdem//Desktop//IPython//testFiles//largeFile.txt"
oDosyaIsim = "C://Users//Erdem//Desktop//IPython//testFiles//largeFile-2.txt"

iDosya = open(iDosyaIsim, "r")
oDosya = open(oDosyaIsim, "w")

buffer = iDosya.read(BUFFSIZE)

while(len(buffer)):
    oDosya.write(buffer)
    print("{} byte {} kaydedildi".format(len(buffer), oDosyaIsim, flush=True))
    buffer = iDosya.read(BUFFSIZE)
          
    

print("İşlem tamamlandı")
          
          
