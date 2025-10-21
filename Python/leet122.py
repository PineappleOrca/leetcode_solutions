def maxProfit(prices):
    left = 0
    max_profit = 0
    i = 1
    while(i < len(prices)):
        print(left, i, prices)
        test_profit = prices[i] - prices[left]
        if(test_profit > 0):
            max_profit += test_profit
        left = i
        i += 1
        #prices = prices[left:]
    return max_profit 

prices = [7,6,4,3,1]
#prices = [7,1,5,3,6,4]
#prices = [1,2,3,4,5]
print(maxProfit(prices))
        