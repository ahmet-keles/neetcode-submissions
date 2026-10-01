class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k - 1
        white = 0
        res = len(blocks)
        for i in range(l, r + 1, 1):
            if blocks[i] == 'W':
                white += 1
        res = min(white, res)
        r += 1
        while r < len(blocks):
            if blocks[l] == 'W':
                white -= 1
            if blocks[r] == 'W':
                white += 1
            res = min(white, res)
            r += 1
            l += 1

        return res
