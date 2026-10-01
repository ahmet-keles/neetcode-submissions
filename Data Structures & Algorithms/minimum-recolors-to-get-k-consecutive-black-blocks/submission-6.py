class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        white = blocks[:k].count('W')
        res = white
        while r < len(blocks):
            if blocks[l] == 'W':
                white -= 1
            if blocks[r] == 'W':
                white += 1
            res = min(white, res)
            r += 1
            l += 1

        return res
