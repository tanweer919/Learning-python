for i in range(100000,1000000):
    a=str(i)
    b=a[2:]
    if b[::-1]==b:
        c=str(i+1)
        d=c[1:]
        if d[::-1]==d:
            e=str(i+2)
            f=e[1:5]
            if f[::-1]==f:
                print(i)