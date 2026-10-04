class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 2
        prev_prev = 1
        if n == 1:
            return prev_prev

        for i in range(n - 2):
            prev, prev_prev = prev_prev + prev, prev
        return prev