fp = open(r"C:/Users/Erdem/Desktop/IPython/testFiles/myFile.txt", "r")

n = 0
for line in fp:
    n += 1
    print(n, line, end="")

fp.close()

print("\n")
print("Read {} lines.".format(n))
