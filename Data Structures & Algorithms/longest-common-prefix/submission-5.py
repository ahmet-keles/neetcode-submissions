class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)
        minn = len(strs[0])
        for i in range(1, n):
            minn = min(len(strs[i]), minn)

        res = ""


        for j in range(minn):
            flag = True
            for i in range(len(strs) - 1):
                if strs[i][j] != strs[i + 1][j]:
                    flag = False
            if flag:
                res += strs[0][j]
            else:
                break


        return res