f = open("C://Users//Erdem//Desktop//IPython//testFiles//myFile.txt", "r")
fdurum = f.tell()
print("fdurum =", fdurum)

data = f.read()
print(len(data))
print(data)

fdurum = f.tell()
print("fdurum =", fdurum)


print("*" * 30)
data = f.read()
print(len(data))
print(data)

fdurum = f.tell()
print("fdurum =", fdurum)

print("*" * 30)

f.seek(0)

fdurum = f.tell()
print("fdurum =", fdurum)

data = f.read()
print(len(data))
print(data)

fdurum = f.tell()
print("fdurum =", fdurum)

print("*" * 30)

f.seek(100)

data = f.read()
print(len(data))
print(data)

fdurum = f.tell()
print("fdurum =", fdurum)
      
