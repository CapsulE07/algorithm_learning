def kmp(inputs, pattern):
    i=0
    j=0
    next_arr = get_next(pattern)
    while (i < len(inputs) and j < len(pattern)):
        if j==-1 or inputs[i]==pattern[j]:
            i +=1
            j+=1
        else:
            j=next_arr[j]
    if j==len(pattern):
        return i-j
    else:
        return -1

def get_next(pattern):
    next_arr=[0 for _ in range(len(pattern))] 
    next_arr[0] = -1
    k,j=-1,0
    while j < len(pattern) - 1:
        if k==-1 or pattern[k]==pattern[j]:
            k+=1
            j+=1
            next_arr[j]=k
        else:
            k=next_arr[k]
    return next_arr
    
if __name__ == "__main__":

    inputs = "abacababc"
    pattern = "abab"
    res = kmp(inputs, pattern)
    print("kmp匹配结果： {}".format(res))

