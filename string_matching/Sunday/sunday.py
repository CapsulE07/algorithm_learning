
def sunday(inputs, pattern):
    next_map = get_next(pattern)
    print(next_map)
    i,j=0,0
    while i <= len(inputs) - len(pattern):
        j=0
        while j<len(pattern) and inputs[i+j]==pattern[j]:
            j+=1
        if j == len(pattern):
            return i
        else:
            i = i + next_map[pattern[i]]


def get_next(pattern):
    next_map={}
    for i in range(len(pattern)):
        next_map[pattern[i]] = i
    return next_map


if __name__ == "__main__":
 
    inputs = "abacababc"
    pattern = "abab"
    res = sunday(inputs, pattern)
    print("sunday 匹配结果： {}".format(res))   