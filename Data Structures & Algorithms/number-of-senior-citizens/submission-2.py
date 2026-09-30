class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            num = int(d[11:13])
            if num > 60:
                res += 1
        
        return res