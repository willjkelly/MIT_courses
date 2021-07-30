import numpy as np
import pandas as pd

def AdvanceMonth(moneyIn, mo_salary, per_saved, interest):
    interest_add = moneyIn + moneyIn*interest/12
    new_savings = interest_add + mo_salary*per_saved

    return new_savings
  
def GetInput(question: str):
    val = input('Enter ' + question + ": ")
    return val
  
#Problem C

if __name__ == "__main__":
    PORTION_DOWN_PAYMENT = 0.25
    INTEREST_RATE = 0.04
    current_savings = 0
    SEMI_ANNUAL_RAISE = 0.07
    TOTAL_COST = 1000000
    
    
    annual_salary = float(GetInput("the starting salary"))
    month_count = 1
    
    low=0
    high=10000
    solved = ""
    for x in range(0,12):
        monthly_salary = annual_salary/12

        while(month_count < 37):
            portion_saved = (((low + high) / 2) / 10000)
            current_savings = AdvanceMonth(current_savings, monthly_salary, portion_saved, INTEREST_RATE)
            month_count+=1
            #print(portion_saved, current_savings, month_count)

            if(month_count % 6 == 0):
                monthly_salary += monthly_salary*semi_annual_raise
        #print(portion_saved, current_savings, month_count, x)        
        if(current_savings > TOTAL_COST*PORTION_DOWN_PAYMENT + 100):
            high = portion_saved*10000
            month_count = 0
            current_savings = 0
        elif(current_savings < TOTAL_COST*PORTION_DOWN_PAYMENT - 100):
            low = portion_saved*10000
            month_count = 0
            current_savings = 0
        else:
            solved = True
            steps = x
    
    if solved:
        print("Best Savings Rate:", round(portion_saved, 4))
        print("Steps in bisection search: ", steps)
    if not solved:
        print("It is not possible to pay the downpayment in three years")
