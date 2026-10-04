class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        res = ""
        for key, values in count.items():
            if values == 1:
                k -= 1
                if k == 0:
                    return key
        return res