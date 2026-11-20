class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return

            path.append(nums[i])
            backtrack(i+1)
            
            path.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(j)
        
        backtrack(0)

        return res