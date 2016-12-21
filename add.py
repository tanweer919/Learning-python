fin=open("words.txt")
w=input()
for l in fin:
    wo=l.strip()
    if w==wo:
        print("found")