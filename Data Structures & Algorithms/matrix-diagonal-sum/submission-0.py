class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i, row in enumerate(mat):
            j = len(mat) - i - 1
            res += row[i] + (0 if j == i else row[j])
        return res