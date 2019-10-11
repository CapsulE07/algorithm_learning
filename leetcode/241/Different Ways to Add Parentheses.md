## Different Ways to Add Parentheses

### description
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

### Tags
divide-and-conquer

### examples
```
Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

### 解决方案
分治法，动态规划

```
使用分治法与笛卡尔乘积
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ## 递归，笛卡尔积
        ## http://www.pianshen.com/article/6107277391/
        import itertools
        ops = {'+': lambda x, y: x+y,
               '-': lambda x, y: x-y,
               '*': lambda x, y: x*y}
        def ways(s):
            ans=[]
            for i in range(len(s)):
                if s[i] in "+-*":
                    ans += [ops[s[i]](l,r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
            if not ans: ans.append(int(s))
            return ans
        return ways(input)
```

```
"""基于上一版继续HashMap优化"""
class Solution:

    def diffWaysToCompute(self, input: str) -> List[int]:
        ## 递归，笛卡尔积
        ## http://www.pianshen.com/article/6107277391/
        
        import itertools
        hm = {}
        ops = {'+': lambda x, y: x+y,
               '-': lambda x, y: x-y,
               '*': lambda x, y: x*y}
        def ways(s):
            if s in hm.keys(): return hm[s]
            ans=[]
            for i in range(len(s)):
                if s[i] in "+-*":
                    ans += [ops[s[i]](l,r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
            if not ans: ans.append(int(s))
            hm[s] = ans
            return ans
            
        return ways(input)

```

```

```

