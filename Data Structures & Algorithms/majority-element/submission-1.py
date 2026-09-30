class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        countsorted = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
        x = 0
        for key, value in countsorted.items():
            return key