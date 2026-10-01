class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k - 1
        res = len(blocks)
        while r < len(blocks):
            white = 0
            black = 0
            for i in range(l, r + 1, 1):
                if blocks[i] == 'B':
                    black += 1
                if blocks[i] == 'W':
                    white += 1
            
            res = min(white, res)

            l += 1
            r += 1

        return res
