class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
    
        nums.sort(key = lambda n: (mp[n], -n))

        return nums

