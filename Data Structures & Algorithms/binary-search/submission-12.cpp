class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int output = -1;
        int l = 0;
        int r = nums.size()-1;

        int mid = (l+r)/2;

    do
    {
        if(target > nums[mid])
        {
            l = mid + 1;
            mid = (l+r)/2;
        }
        else if(target < nums[mid])
        {
            r = mid - 1;
            mid = (l+r)/2;
        }
        else if(target == nums[mid])
        {
            output = mid;
            return output;
        }
    }
    while(l <= r);


        return output;
    }
};
