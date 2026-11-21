class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        
        def backtrack(i, total):
            if total == target:
                res.append(path.copy())
                return
            elif total > target or i == len(candidates):
                return
            
            path.append(candidates[i])
            backtrack(i+1, total + candidates[i])
            path.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            backtrack(j, total)
            
        backtrack(0, 0)
        return res
        