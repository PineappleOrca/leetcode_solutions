def maxProfit(prices):
    max_profit = 0
    profit = 0
    for i in prices:
        buying_price = i
        for j in prices[i+1:]:
            profit = j - buying_price
            print(buying_price, j, profit)
            if profit > max_profit:
                max_profit = profit 
    return max_profit 

prices = [7,1,5,3,6,4]
print(maxProfit(prices))


