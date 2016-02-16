for i in range(1, 101):
    if(i % 10 == 0):
        print("{:^6}".format(i))
    else:
        print("{:^6}".format(i), end = " ")

