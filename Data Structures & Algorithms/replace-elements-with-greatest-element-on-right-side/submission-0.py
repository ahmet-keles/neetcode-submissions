class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        temp = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            x = arr[i]
            arr[i] = temp
            temp = max(x, temp)
        return arr

