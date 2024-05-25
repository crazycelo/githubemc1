dict={}
for i in range(65,91):
    dict[chr(i).lower()]=i-64
def ascii(word):
    sum=0
    for i in range(len(word)):
        if word[i] in dict:
            char=word[i]
            sum+=dict[char]
    return sum