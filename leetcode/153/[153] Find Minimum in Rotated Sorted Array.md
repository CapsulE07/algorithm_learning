## [153] Find Minimum in Rotated Sorted Array



### Tags
array | binary-search

### Description  
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
### Examples
```
Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
```

### code
1. 开发过程中的错误代码
   ```
   class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums) == 1: return nums[0]
        if len(nums) ==2:
            return min(nums[0], nums[1])
        start = 0
        end = len(nums) - 1
        mid = (start + end) //2

        if nums[start] == nums[end]==nums[mid]:
            return self.minLinear(nums)
        if nums[start] <= nums[mid]:
            start = mid
        if nums[mid] <= nums[end]:
            end = mid
        return self.findMin(nums[start:end + 1])
    
    def minLinear(self, nums):
        minNum=  nums[0]
        for i in nums:
            if i < minNum:
                minNum = i
        return minNum
   ```
```
迭代： 正确代码
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right =len(nums) -1

        ##存在类似这样的情况 [1,1,1,1,1,0,1],在这种情况下,无法使用二分，需依次比较获得最小值
        mid = (left+right)//2
        if mid!= left and nums[left] == nums[mid] == nums[right]:
            return self.minLinear(nums)

        if nums[left] <= nums[right]:
            return nums[left]
        

        while left +1< right:
            mid = (left + right) //2
            if nums[mid] >= nums[left]:
                left = mid 
            else:
                right = mid 
        return nums[right]

    def minLinear(self, nums):
        minNum=  nums[0]
        for i in nums:
            if i < minNum:
                minNum = i
        return minNum

递归： 正确代码
class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        def recursion(nums, l, r):
            if l < r:
                mid = (l+r)//2
                if nums[mid] < nums[r]:
                    r = mid
                elif nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r -= 1
                return recursion(nums, l, r)
            else:
                return nums[l]
    	return recursion(nums, 0, len(nums) - 1)
```