class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int maxProfit = 0;
        int profit;
        int k = 0;

        for(int i = 1; i < prices.size(); i++)
        {
            if(prices[k] < prices[i])
            {
                profit = prices[i] - prices[k];
                maxProfit = max(maxProfit, profit);
            }
            else
            {
                k = i;
            }
        }

        return maxProfit;
    }
};
