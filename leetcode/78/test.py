class Solution:
    def subsets(self, nums):
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

if __name__ == "__main__":
    nums = [1,2,3]
    so = Solution()
    print(so.subsets(nums))