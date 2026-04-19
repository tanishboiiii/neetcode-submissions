class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = max_profit
        sell_date = 1
        buy_date = 0
        while sell_date < len(prices):
            max_profit = max(max_profit, prices[sell_date] - prices[buy_date])
            
            if prices[sell_date] < prices[buy_date]:
                buy_date = sell_date
                
            
            sell_date += 1
           
        return max_profit