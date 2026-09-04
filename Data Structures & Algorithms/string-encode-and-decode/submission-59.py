class Solution:

    def encode(self, strs: List[str]) -> str:
        copy_strs = []
        for s in strs:
            copy_strs.append(str(len(s)) + "#" + s)
        res = "".join(copy_strs)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        begin = 0
        while i < len(s):
            
            if s[i] == '#':
                length = int(s[begin:i])
                res.append(s[i+1: i+length+1])
                i = i + length + 1
                begin = i
            else:
                i += 1
                
        return res
