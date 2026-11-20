class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path, res = [], []
        def backtrack(open, close):
            if close == n:
                temp = "".join(path)
                res.append(temp)
                return
            if open < n:
                path.append("(")
                backtrack(open+1, close)
                path.pop()
            if close < open:
                path.append(")")
                backtrack(open, close+1)
                path.pop()

        backtrack(0, 0)

        return res
        