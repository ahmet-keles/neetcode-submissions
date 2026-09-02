class Solution {
public:
    int findMin(vector<int> &nums) {
        
        int minNum = nums[0];

        int l = 0;
        int r = nums.size()-1;

        while(l <= r)
        {
            if(nums[l] > nums[r])
            {
                minNum = min(minNum, nums[r]);
                r--;

            }
            else      
            {
                minNum = min(minNum, nums[l]);
                return minNum;
            }
        }

        return minNum;
    }
};
