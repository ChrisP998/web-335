"""
Author: Christopher Phan
Date: 2/1/26
File Name: phan_lemonadeStand.py
Description: cost-profit calculator of a lemonade stand
"""

def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost

def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    profit = selling_price - total_cost
    return profit

lemons_cost = 4.00
sugar_cost = 3.50
selling_price = 12.00

total_cost = calculate_cost(lemons_cost, sugar_cost)
total_profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

cost_output = str(lemons_cost) + "+" + str(sugar_cost) + "=" + str(total_cost)
profit_output = "The total profit: $" + str(total_profit)

print(cost_output)
print(profit_output)