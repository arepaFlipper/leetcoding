class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int running_min = 1e9;
      int best_profit = 0;

      for (int price: prices){
        int best_selling_here = price - running_min;
        best_profit = max(best_profit, best_selling_here);
        running_min = min(running_min, price);
      }
      return best_profit;
    }
};
