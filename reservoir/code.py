import random

def reservior_sampling(sequence, k):
    length = len(sequence)
    if length <= k:
        return sequence
    
    reservior = list()
    
    for i in range(k):
        reservior.append(sequence[i])
    
    for i in range(k, length):
        rand_num = random.randint(0, i)
        if rand_num >= k:
            continue
        reservior[rand_num] = sequence[i]
    return reservior


if __name__ == "__main__":
    sample = [1,2,3,4,5,6,7,8,9]
    k = 4
    count = 0 
    iter_num = 1000000
    for i in range(iter_num):
        count += reservior_sampling(sample, k).count(3)

    print(count / iter_num)
    print(4/9)