def maxProfit(prices):
    minprice=prices[0]
    maxprofit=0
    for i in prices:
        if i < minprice:
            minprice = i
        profit = i - minprice
        if profit > maxprofit:
            maxprofit = profit
    return maxprofit

prices = [7, 6, 5, 4, 8, 2]
print(maxProfit(prices))