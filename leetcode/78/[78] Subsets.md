## Subsets

### Tags
array | backtracking | bit-manipulation

### Description
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

### Example
```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```



### code
思路：位运算使用技巧： 给定一个含补贴整数的集合，返回其所有的子集
解题思路： 使用一个正整数二进制表示第i位是1还是0， 代表集合的第i个数取或不取。从0到$2^{n-1}$总共有$2^n$个整数，对应着集合的$2^n$个子集。
```
s = {1,2,3}
n bit Combination
000 {}
001 {1}
010 {2}
011 {1,2}
100 {3}
101 {1,3}
110 {2,3}
111 {1,2,3}
```


```
10/10 cases passed (40 ms)
Your runtime beats 75.73 % of python3 submissions
Your memory usage beats 5.95 % of python3 submissions (13.9 MB)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        binanry_num= 2**(len(nums))
        for i in range(binanry_num):
            curRes = []
            idx = 0
            while i > 0:
                if i & 1 == 1:
                    curRes.append(nums[idx])
                i = i>>1
                idx += 1
            ans.append(curRes)
        return ans

```

2. 回溯法
   
