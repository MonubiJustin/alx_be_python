monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}")