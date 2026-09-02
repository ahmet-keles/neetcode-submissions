class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        bool output = false;
        
        int rNum = 0;
        int m = 0;
        int n = matrix[rNum].size()-1;
        int mid = (m+n)/2;

        while(m <= n)
        {

            if(target > matrix[rNum][n])
            {
                rNum++;
                if(rNum >= matrix.size())
                {
                    output = false;
                    return output;
                }
                n = matrix[rNum].size()-1;
                m = 0;
                cout << rNum << endl;
                if(target < matrix[rNum][m])
                {
                    output = false;
                    return output;
                }
            }
            else if(target > matrix[rNum][mid])
            {
                m = mid + 1;
                mid = (m+n)/2;
            }
            else if(target < matrix[rNum][mid])
            {
                n = mid - 1;
                mid = (m+n)/2;
            }
            else if(target == matrix[rNum][mid])
            {
                output = true;
                return output;
            }


        }

        return output;

    }
};
