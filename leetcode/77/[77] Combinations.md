## Combinations

### Tags
backtracking

### Description
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

### Example
```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

### code
1. 使用位运算，超时
```
Time Limit Exceeded
26/27 cases passed (N/A)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        binanry_num= 2**(n)
        isOneIndex = []
        for i in range(binanry_num):
            idx = 0
            while i > 0:
                if i & 1 == 1:
                    isOneIndex.append(idx+1)
                i = i>>1
                idx +=1
            if len(isOneIndex) == k:
                ans.append(isOneIndex)
            isOneIndex = []
            
        return ans
```

