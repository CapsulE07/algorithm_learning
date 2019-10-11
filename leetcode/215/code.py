class Solution:
    def findKthLargest(self, nums, k):
        ## 转换为寻找第n个最小值，这样在使用数组计数时更加方便
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self._partition_doubule(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    def _partition_doubule(self, nums, l, r):
        ## 双指针快排思路 
        ## 随机选择基准，将其与第一项交换，随后将其他项进行交换比较，
        ## 最后最终的基准元素与遍历后的index进行交换
        import random
        ind = random.randint(l, r)
        nums[l], nums[ind] = nums[ind], nums[l]
        pivot = nums[l]
        i, j = l+1, r
        while True:
            while i <= r and nums[i] < pivot:  
                # 不能改为nums[i] <= pivot, 因为这种方式则      
                # 会将连续出现的这些值归为其中一方，使得两棵子树不平衡
                i += 1
            while j >= l + 1 and nums[j] > pivot:  
                # 不能改为nums[j] >= pivot.
                j -= 1
            if i > j:
                break
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[j], nums[l] = nums[l], nums[j]
        return j


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    nums =[3,2,3,1,2,4,5,5,6]
    k = 4
    so = Solution()
    print(so.findKthLargest(nums,2))