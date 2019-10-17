class Solution:
    def findMin(self, nums):
        left = 0; right =len(nums) -1
        if nums[left] <= nums[right]:
            return nums[left]
        while left +1< right:
            mid = (left + right) //2
            if nums[mid] >= nums[left]:
                left = mid 
            else:
                right = mid 
        return nums[right]

if __name__ == "__main__":
    so = Solution()
    nums= [1,1,1,1,1,1,0,1]
    print(so.findMin(nums))
    ## 这种情况下会返回结果为1