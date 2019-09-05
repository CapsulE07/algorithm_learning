def kmp(input, pattern):
    i = 0
    j=0
    while (i < len(input) and j < len(pattern)):
        if input[i]==pattern[j]:
            i +=1
            j +=1
        else:
            j=next[j]

    if j==len(pattern):
        return i-j
    else:
        return -1

def get_next(pattern):
    next[0] = -1
    i,j=0,-1
    while i < len(pattern):
        if 
    