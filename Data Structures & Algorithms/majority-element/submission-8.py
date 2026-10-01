class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        canditate = nums[0]
        vote = 0
        for i in range(len(nums)):
            if nums[i] != canditate:
                vote -= 1
            else:
                vote += 1
            
            if vote == 0:
                canditate = nums[i]
                vote += 1

        return canditate