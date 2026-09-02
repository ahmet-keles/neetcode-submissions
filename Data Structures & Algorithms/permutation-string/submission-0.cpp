class Solution {
public:
    bool checkInclusion(string s1, string s2) {

        bool res = false;

        int left = 0;
        int right = s1.length();

        unordered_map<char, int> count1;
        unordered_map<char, int> count2; 


        for(int i = 0; i < s1.length(); i++)
        {
            count1[s1[i]]++;
        }

        for(left; left < right; left++)
        {
            count2[s2[left]]++;
        }

        left = 0;

        for(int i = right; i < s2.length(); i++)
        {
            
            if(count1 == count2)
            {
                return true;
            }

            count2[s2[i]]++;
            count2[s2[left]]--;

            if (count2[s2[left]] == 0) 
            {
                count2.erase(s2[left]);
            }

            left++;



        }

        return count1 == count2;
        
    }
};
