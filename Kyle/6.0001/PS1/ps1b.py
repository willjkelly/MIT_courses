import numpy as np
import pandas as pd

def AdvanceMonth(moneyIn, mo_salary, per_saved, interest):
    interest_add = moneyIn + moneyIn*interest/12
    new_savings = interest_add + mo_salary*per_saved

    return new_savings
  
def GetInput(question: str):
    val = input('Enter ' + question + ": ")
    return val
  
#Problem B

if __name__ == "__main__":
    PORTION_DOWN_PAYMENT = 0.25
    INTEREST_RATE = 0.04
    current_savings = 0
    
    annual_salary = float(GetInput("your annual salary"))
    monthly_salary = annual_salary/12
    portion_saved = float(GetInput("the percent of your salary to save, as a decimal"))
    total_cost = float(GetInput("the cost of your dream home"))
    semi_annual_raise = float(GetInput("the semi-annual raise, as a decimal"))
    month_count = 0
    
    while(current_savings < total_cost*PORTION_DOWN_PAYMENT):
        #print(current_savings)
        current_savings = AdvanceMonth(current_savings, monthly_salary, portion_saved, INTEREST_RATE)
        month_count+=1
        if(month_count % 6 == 0):
            monthly_salary += monthly_salary*semi_annual_raise
    
    print("Number of months:", month_count)
