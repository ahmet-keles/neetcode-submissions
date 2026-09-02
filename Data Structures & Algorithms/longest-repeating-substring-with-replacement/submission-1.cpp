class Solution {
public:
    int characterReplacement(string s, int k) {
        
        int tempk = k;

        int maxFreq = 0;
        int left = 0;
        int maxLen = 0;

        unordered_map<char, int> count;

        for(int i = 0; i < s.length(); i++)
        {
            
            count[s[i]]++;
            maxFreq = max(maxFreq, count[s[i]]);  

            if ((i - left + 1) - maxFreq > k) 
            {
                count[s[left]]--;
                left++;
            }

            
            
            maxLen = max(maxLen, i - left + 1);
            cout << maxLen << endl;
        }


        return maxLen;
        

    }
};
