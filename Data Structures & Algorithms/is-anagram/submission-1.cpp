#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        int length = s.length();

        if(s.length() != t.length())
        {
            return false;
        }

        for(int i = 0; i < length; i++)
        {
            sMap[s[i]]++;
            tMap[t[i]]++;
        }
        
        for(const auto& pair : sMap)
        {

            char c = pair.first;
            if(sMap[c] != tMap[c])
            {
                return false;
            }

        }

    }
};
