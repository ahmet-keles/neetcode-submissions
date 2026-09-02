#include <string>
#include <vector>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        int length = nums.size();

        for(int i = 0; i < length; i++)
        {
            for(int k = i+1; k < length; k++)
            {
                if(nums[k] ==  nums[i])
                {
                    return true;
                }
            }
        }

        return false;
    }
};
