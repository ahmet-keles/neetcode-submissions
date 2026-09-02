class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());

        int j = 0;
        int k = nums.size()-1;

        vector<vector<int>> output;

            for(int i = 0; i < nums.size(); i++)
            {
                int target = -nums[i];
                j = i + 1;
                k = nums.size()-1;
                
                while(j < k)
                {
                    if(nums[j]+nums[k] < target)
                    {
                        j++;
                    }
                    else if(nums[j] + nums[k] > target)
                    {   
                        k--;
                    }
                    else
                    {
                        vector<int> temp = {nums[i], nums[j], nums[k]};
                    
                        bool flag = false;
                     
                        for(auto i : output)
                        {
                            if(i == temp)
                            {   
                                flag = true;
                            }
                        }

                        if(!flag)
                        {
                        output.push_back(temp);
                        }
                        j++;
                        k--;
                    }
                }
            }
        return output;

    }
};
