class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 * i for i in range(1 ,n + 1)]
        print(res)
        return list(set(res) - set(nums))
        # for i in range(n):
        #    res[nums[i] - 1] = nums[i]
        # return res
