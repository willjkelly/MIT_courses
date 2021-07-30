# 1. Your semi­annual raise is .07 (7%)
# 2. Your investments have an annual return of 0.04 (4%)  
# 3. The down payment is 0.25 (25%) of the cost of the house 
# 4. The cost of the house that you are saving for is $1M.

# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
# 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
# the required down payment. 
import sys

starting_salary = float(input("Enter the starting salary: "))
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
portion_down_payment = 0.25 * total_cost

if starting_salary * 36 < total_cost:
    print("It is not possible to pay the down payment in three years.")
    sys.exit(0)

search_min = 0
search_max = 10000
search_target = (search_min + search_max)/2

def next_search_target( search_min, search_max, current_target,  higher ):
    if higher:
        return int((current_target + search_max)/2), current_target, search_max
    else:
        return int((search_min + current_target)/2), search_min, current_target

def evaluate_savings_rate( rate, salary ):
    portion_saved = rate / 10000
    monthly_salary = salary / 12
    current_savings = 0
    for i in range(36):
        if ( i % 6 == 0 ) and ( i > 0 ):
            monthly_salary = monthly_salary * ( 1 + semi_annual_raise )
        current_savings += current_savings*r/12
        current_savings += monthly_salary*portion_saved

    return current_savings

optimal_savings_rate = search_target
diff = evaluate_savings_rate( optimal_savings_rate, starting_salary ) - portion_down_payment 
steps = 0
while abs( diff ) > 100:
    target_higher = (diff < 0)
    optimal_savings_rate, search_min, search_max = next_search_target( search_min, search_max, optimal_savings_rate, target_higher )
    diff = evaluate_savings_rate( optimal_savings_rate, starting_salary ) - portion_down_payment 
    steps += 1

print( f"Best savings rate: {optimal_savings_rate / 10000}" )
print( f"Steps in bisection search: {steps}" )
