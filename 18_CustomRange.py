def customRange(*args):
    ilk = son = step = 0

    if(len(args) == 3):
        ilk = args[0]
        son = args[1]
        step = args[2]

    elif(len(args) == 2):
        ilk = args[0]
        son = args[1]
        step = 1

    else:
        ilk = 0
        son = args[0]
        step = 1

    i = ilk
    while(i < son):
        yield i
        i = i + step

a = customRange(4, 30, 3)
print(list(a))
