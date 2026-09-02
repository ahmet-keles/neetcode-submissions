class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int i = 0;
        int j = numbers.size()-1;

        vector<int> output;

        while(i < j && output.size() < 2)
        {
            int tempTotal = numbers[i] + numbers[j];

            if(target == tempTotal)
            {
                output.push_back(i+1);
                cout << i << endl;
                output.push_back(j+1);
                cout << j << endl;
                i++;
                j--;
            }
            else
            {
                if((j-1) == i)
                {
                    i++;
                    j = numbers.size()-1;
                }
                else
                {
                j--;
                }
            }

         }

         return output;
        
    }
};
