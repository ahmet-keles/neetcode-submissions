class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> anagramGroups;

        for(const string& str : strs)
        {
            int freq[26] = {0};

            for(char c : str)
            {
                freq[c-'a']++;
            }


            string key;
            for(int i = 0; i < 26; i++)
            {
                key+= to_string(freq[i]) + "#";
            }

            anagramGroups[key].push_back(str);
        }


        
    
        vector<vector<string>> result;
        for(auto& pair : anagramGroups) {
            result.push_back(pair.second);
        }
        
        return result;
        
    }
};
