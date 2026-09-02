class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int lcs = 1;
        int maxlcs = 1;

        sort(nums.begin(), nums.end());

         if(nums.empty())
         {
            return 0;
         }


        for(auto k: nums)
        {
            int temp = k;

            for(auto i: nums)
            {

                if(i == temp+1)
                {
                    temp = i;
                    lcs++;

                }

                cout << i << " ";

            }

            if(lcs >= maxlcs)
            {
                maxlcs = lcs;
            }

            lcs = 1;

        }

        return maxlcs;
    }
};
