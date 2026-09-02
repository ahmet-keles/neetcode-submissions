class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for i in range(len(strs)):
            x = sorted(strs[i])
            y = "".join(x)
            if y not in my_dict:
                my_dict[y] = []
            my_dict[y].append(strs[i])
        
        lists = []
        for i in my_dict.values():
            lists.append(i)
        return lists