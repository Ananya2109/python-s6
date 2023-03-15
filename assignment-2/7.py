
# 7. Write a program that computes an investment report.
#Analysis
#The inputs to this program are the following:
#An initial amount to be invested(a floating-point number)
#A period of years(an integer)
#An interest rate(a percentage expressed as an integer)
initial_amount = float(input("Enter the initial amount to be invested: "))
years = int(input("Enter the period of years: "))
interest_rate = int(input("Enter the interest rate: "))


print("Year\tStarting Balance\tInterest\tEnding Balance")
print("-" * 50)


total_interest = 0


for year in range(1, years+1):
    interest = round(initial_amount * interest_rate / 100, 2)
    ending_balance = round(initial_amount + interest, 2)
    print(f"{year}\t{initial_amount}\t\t{interest}\t\t{ending_balance}")
    total_interest += interest
    initial_amount = ending_balance


print("-" * 50)
print(f"Ending balance: {round(ending_balance, 2)}")
print(f"Total Interest Earned: {round(total_interest, 2)}")


