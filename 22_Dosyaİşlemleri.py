fp = open(r"C:/Users/Erdem/Desktop/IPython/testFiles/myFile.txt", "r")
for line in fp:
    print(line, end="")

fp.close()
