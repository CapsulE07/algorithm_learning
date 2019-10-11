## Search a 2D Matrix II  

### description
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
### Tags
binary-search | divide-and-conquer

### Example
```
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
```

### 解决方案

#### 分治法
根据矩阵特征，从矩阵左下或者右上元素入手。判断其与target大小关系，每次可以过滤掉一部分矩阵元素。
```

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])

        if target < matrix[0][0] or target > matrix[row-1][col-1]:
            return False

        x = 0
        y = col - 1
        while True:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
            if x >= row or y < 0:
                return False
        return False

```


