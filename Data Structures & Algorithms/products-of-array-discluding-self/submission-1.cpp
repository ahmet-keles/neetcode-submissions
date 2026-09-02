class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int temp;
        vector<int> output;
        int size = nums.size();
        cout << size;
        for(int i = 0; i < size; i++)
        {
            temp = 1;
            for(int k = 0; k < size; k++)
            {
                if(i != k)
                    {
                        temp = temp * nums[k];
                    }
                cout << temp;
            }

            output.push_back(temp);
        }

        return output;
    }
};
