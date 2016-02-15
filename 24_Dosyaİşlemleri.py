iFile = open(r"C:/Users/Erdem/Desktop/IPython/testFiles/myFile.txt", "r")
oFile = open(r"C:/Users/Erdem/Desktop/IPython/testFiles/myFile2.txt", "w")

for line in iFile:
    print(line, file=oFile, end="", flush=True)

print("İşlem gerçekleştirildi")
             
