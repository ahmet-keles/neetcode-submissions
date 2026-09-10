class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            temp_hour_count = 0

            middle = left + (right - left) // 2
            for i in piles:
                temp_hour_count += -(-i // middle)

            if temp_hour_count > h:
                left = middle + 1
            else:
                res = middle
                right = middle - 1
            
        return res



        