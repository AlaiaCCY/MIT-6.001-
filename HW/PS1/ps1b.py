# =============================================================================
# MIT 6.001 PS1b
# Chunyu Chen(Alaia)
# =============================================================================
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12

month = 0
time = 1
while (total_cost * portion_down_payment > current_savings):
    current_savings += current_savings*r/12
    current_savings += portion_saved * monthly_salary
    month += 1
    if (month/6 == time) and (month != 0):
        monthly_salary = monthly_salary * (1+semi_annual_raise)
        time += 1

print("Number of months:", month)