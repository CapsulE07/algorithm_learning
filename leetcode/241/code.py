class Solution:

    def diffWaysToCompute(self, input):
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


if __name__ == "__main__":
    inputs = "2-1-1"
    so = Solution()
    so.diffWaysToCompute(inputs)