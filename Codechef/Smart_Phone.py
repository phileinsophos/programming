'''
        Problem Statement : Smart Phone 
        Link : https://www.codechef.com/LRNDSA01/problems/ZCO14003
        score : accepted
'''

customers = int(input())
budgets = []
for c in range(customers):
    budgets.append(int(input()))
budgets.sort(reverse=True)
profit = 0
for index,cb in enumerate(budgets):
    value = (index+1)*cb
    if value > profit:
        profit = value
    
print(profit)

