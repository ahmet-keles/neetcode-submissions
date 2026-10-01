class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        maxx = -1
        minn = 101
        for key, values in count.items():
            if values % 2 == 1:
                maxx = max(values, maxx)
            else:
                minn = min(values, minn)
        print(maxx, minn)
        return maxx - minn