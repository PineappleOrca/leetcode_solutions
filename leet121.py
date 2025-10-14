def maxProfit(prices):
    # this solution is like O(n^2) ish 
    max_profit = 0
    for i in range(len(prices)-1):
        buying_price = prices[i]
        new_prices = prices[i:]
        for j in range(len(new_prices)):
            my_profit = new_prices[j] - buying_price
            print(buying_price, new_prices[j], my_profit)
            if(my_profit > max_profit):
                max_profit = my_profit
    return max_profit 

def maxProfit2(prices):
    # This solution utilises a sliding window and is O(n) in time complexity
    left = 0
    max_profit = 0
    for i in range(1,len(prices)):
        profit = prices[i] - prices[left]
        if(profit > 0):
            max_profit = max(profit, max_profit)
        else:
            left = i 
    return max_profit 


prices = [7,1,5,3,6,4]
print(maxProfit2(prices))

