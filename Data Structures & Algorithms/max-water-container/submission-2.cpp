class Solution {
public:
    int maxArea(vector<int>& heights) {
        
        int maxArea = 0;

        int i = 0;
        int j = heights.size()-1;

        while(i < j)
        {   
            int tempArea = min(heights[i], heights[j]) * (j-i);
            maxArea = max(maxArea, tempArea);

            if(heights[i] < heights[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }

        return maxArea;
    }
};
