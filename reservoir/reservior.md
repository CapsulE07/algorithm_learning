# 蓄水池算法

给定一个数据流，数据流长度N很大，且N直到处理完所有数据之前都不可知，请问如何在只遍历一遍数据（O(N)）的情况下，能够随机选取出m个不重复的数据。

这个场景强调了3件事：

数据流长度N很大且不可知，所以不能一次性存入内存。
时间复杂度为O(N)。
随机选取m个数，每个数被选中的概率为m/N。

## 算法解析

构建一个长度为m的水池，将数据流中的前m项都存进去。  
其中所有的数值被保留的概率为1。在此我们命名其为$P_{currentSave}^{m}$，即为在在第m轮中，蓄水池中每一项被保留的概率。  
对应的，我们命名在第m轮时，蓄水池中每一项被替换的概率为$P_{currentReplace}^{m}$。  
那么某个蓄水池中的数能存在在蓄水池中的概率自然为自添加进蓄水池起，至当前轮次，每一轮被保留的概率的累乘。由于之前蓄水池未满，一直在添加数据，所以在第m项时，该实际保留的概率为1，命名为$P_{actualSave}^{m}$。  

当到第m+1项时，在$[1,m+1]$中随机生成一个数，则该数在水池大小m中的概率为$\frac{m}{m+1}$。
如果该随机数在m范围内，则将对应位置的数进行交换。
那么对于原本水池中的数而言，其被替换的概率$P_{currentReplace}^{m+1}$为$\frac{m}{m+1} * \frac{1}{m}$即$\frac{1}{m+1}$,则对应的被保留下来的概率$P_{currentSave}^{m+1}$为$1 - P_{currentReplace}^{m+1}$即$\frac{m}{m+1}$。  
实际上每一项被保留的概率$P_{actualSave}^{m+1}$ 则更新为$P_{currentSave}^{m+1} * P_{actualSave}^{m}$ 即$\frac{m}{m+1}$。而第m+1项被添加进蓄水池的概率与其相等，即蓄水池中每一项概率即都为  $\frac{m}{m+1}$。  
第m+2项时，在$[1,m+2]$中随机生成一个数，则该数在水池大小m中的概率为$\frac{m}{m+2}$。
如果该随机数在m范围内，则将对应位置的数进行交换。
那么对于原本水池中的数而言，其被替换的概率$P_{currentReplace}^{m+2}$为$\frac{m}{m+2} * \frac{1}{m}$即$\frac{1}{m+2}$,则对应的在该轮被保留下来的概率$P_{currentSave}^{m+2}$为$1 - P_{currentReplace}^{m+2}$即$\frac{m+1}{m+2}$。结合上一轮中蓄水池实际上每一项被保留的概率$P_{actualSave}^{m+2}$ 则更新为$P_{currentSave}^{m+2} * P_{actualSave}^{m+1}$ 即$\frac{m+1}{m+2} * \frac{m}{m+1}$,为$\frac{m}{m+2}$。  
以此类推，无论数据如何追加，蓄水池中每一项存在的概率都为$\frac{m}{n}$, n为实时的数据长度。  

## 算法代码
```
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

```
