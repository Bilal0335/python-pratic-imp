age = int(input("Enter your age: "))

years_left = 90 - age
days_left = years_left * 365
months_year = years_left * 12
weeks_left = years_left * 52

print(f"You have {days_left} days, {weeks_left} weeks and {months_year} months left")
