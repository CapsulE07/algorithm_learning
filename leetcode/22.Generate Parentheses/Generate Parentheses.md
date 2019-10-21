## Generate Parentheses

### Tags
string | backtracking

### Description
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Examples
```
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

### code 
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res =[]
        def gen(strings, start, end):
            if len(strings) == 2 *n:
                res.append("".join(strings))
                return
            if start < n:
                 gen(strings+"(", start+1, end)
            if end < start:
                gen(strings + ")", start, end+1)
        gen("", 0, 0)
        return res
```