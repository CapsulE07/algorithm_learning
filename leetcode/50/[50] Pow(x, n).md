## Pow(x, n)

### Tags
math | binary-search

### Description 
Implement pow(x, n), which calculates x raised to the power n (xn).

### Examples  
```
Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

```

### code 
1. 将指数化作二进制形式，只需在其二进制数上值为1的位数进行累成即可。 例如 $2^{10}$ ,可写为 $2^{(1010)_2}$, 即其只需在二进制位第1位及第3位进行累乘。 做法为：不断将指数右移，右移后的数与1进行与运算，即可判断当前位是否为1，如果是1，即将当前位对应的数累乘入结果中。 
2. 简单使用递归。
对于 n 是偶数的情况， $x^{n} = x^{n/2} * x^{n/2}$ 。
对于 n 是奇数的情况，$x^{n} = x^{n/2} * x^{n/2} * x$ 。
```
"""
304/304 cases passed (28 ms)
Your runtime beats 98.78 % of python3 submissions
Your memory usage beats 6.9 % of python3 submissions (13.9 MB)

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==-1:
            return -1 if n&1 != 0 else 1
        if x ==1:
            return 1
        if n == -2147483648:
            return 0
        if n > 0:
            return self.powNum(x, n)
        else:
            return 1 / self.powNum(x, -n) 

    
    def powNum(slef, x, n):
        ans = 1
        while n>0:
            if n & 1 == 1:
                ans = ans * x
            x = x * x
            n = n>>1
        return ans
            
```

1. 

```
"""
304/304 cases passed (40 ms)
Your runtime beats 40.27 % of python3 submissions
Your memory usage beats 6.9 % of python3 submissions (13.7 MB)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==-1:
            return -1 if n&1 != 0 else 1
        if x ==1:
            return 1
        if n == -2147483648:
            return 0

        def powRecursion(x, n):
            if n == 0:
                return 1
            ##偶数的情况
            if n & 1 == 0:  
                return powRecursion(x * x, n // 2)
            else: 
            ##奇数的情况 
                return powRecursion(x * x, n // 2) * x

        if n > 0:
            return powRecursion(x, n)
        else:
            return 1 / powRecursion(x, -n)

```