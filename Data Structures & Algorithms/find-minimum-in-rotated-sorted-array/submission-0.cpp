class Solution {
public:
    int findMin(vector<int> &nums) {
        
        int minNum = nums[0];

        for(auto i : nums)
        {
            minNum = min(minNum, i);
        }

        return minNum;
    }
};
