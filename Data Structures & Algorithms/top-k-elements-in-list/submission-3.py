class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums) + 1)]
        my_dict = defaultdict(int)
        res = []

        for num in nums:
            my_dict[num] += 1

        for num, count in my_dict.items():
            frequency[count].append(num)

        for i in range(len(frequency)-1, -1, -1):
            for num in frequency[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        

                
            




        
        