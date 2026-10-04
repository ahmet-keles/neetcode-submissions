class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        res[-1] = -1
        x = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            res[i] = x
            if arr[i] >= x:
                x = arr[i]

        return res