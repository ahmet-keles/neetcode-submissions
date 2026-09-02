class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        
        sort(piles.begin(), piles.end());

        int res;
        int l = 1;
        int r = piles[piles.size()-1];
        res = r;
        int k;

        while(l <= r)
        {
            k = (l+r)/2;
            int hours = 0;

            for(auto i : piles)
            {
                hours += ceil((double)i / k);
            }

            if(hours <= h)
            {
                res = min(res, k);
                r = k - 1;
            }
            else{
                l = k + 1;
            }

        }

        return res;

    }
};
