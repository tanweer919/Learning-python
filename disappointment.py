t = [[1, 2], [3], [4, 5, 6]]
su=0
for i in t:
    if (type(i)==list):
        s=0
        for j in i:
            s=s+j
        su=su+s
    else:
        su=su+i
print(su)
a = [1, 2, 3]
sum=0
i=0
for b in a:
    sum=sum+b
    a[i]=sum
    i+=1
print(a)
    