fin=open("words.txt")
for line in fin:
    word=line.strip()
    i=0
    for l in word:
        if (len(word[i+1:])>=6):
            if word[i]==word[i+1]:
                if(word[i+2]==word[i+3] and word[i+4]==word[i+5] and word[i]!=word[i+2] and word[i]!=word[i+4] ):
                    print(word)
        i=i+1