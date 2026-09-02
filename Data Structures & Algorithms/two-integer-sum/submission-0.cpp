#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int length = nums.size();
        
        vector<int> out;

        for(int i = 0; i < length; i++)
        {
            for(int k =i+1; k < length; k++)
            {
                if(nums[i] + nums[k] == target)
                {
                    out.push_back(i);
                    out.push_back(k);
                    return out;
                }
            }
        }
    }


};
