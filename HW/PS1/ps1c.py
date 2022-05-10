# =============================================================================
# MIT 6.001 PS1c
# Chunyu Chen(Alaia)
# =============================================================================
portion_down_payment = 0.25
current_savings = 0
r = 0.04
semi_annual_raise = 0.07
total_cost = 1000000
totalmonth = 36

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12

top = 10000
low = 0
portion_saved = (low + top)/2
num_guess = 0

neededPayment = portion_down_payment * total_cost

# bisection search for saving rate
while abs(current_savings - neededPayment) > 100 and portion_saved <= top:
    if portion_saved == top:
        break
    current_savings = 0
    monthly_salary = annual_salary / 12
    # with this saving rate, what is the total saving after 3 years
    time = 1
    for month in range(0,totalmonth):
        current_savings += current_savings*r/12
        current_savings += monthly_salary * portion_saved/10000
        if (month/6 == time) and (month != 0):
            monthly_salary = monthly_salary * (1+semi_annual_raise)
            time += 1
    if current_savings < neededPayment:
        low = portion_saved
    else:
        top = portion_saved
    portion_saved = (low + top)/2
    num_guess += 1

# check if we find the rate
if abs(current_savings - neededPayment) > 100:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved/10000)
    print("Steps in bisection search:", num_guess)