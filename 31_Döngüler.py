for i in range(1, 201):
    if(i % 2 == 0):
        if(i % 20 == 0):
            print("{:^6}".format(i))
        else:
            print("{:^6}".format(i), end = " ")
    else:
        continue
