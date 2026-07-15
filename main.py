print("Loan Eligibility Checker")

name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
salary = float(input("Enter Monthly Salary: "))
credit_score = int(input("Enter Credit Score: "))

print("\nLoan Report")
print("-")
print("Customer Name :", name)
print("Age           :", age)
print("Salary        :", salary)
print("Credit Score  :", credit_score)

if age >= 21 and salary >= 30000 and credit_score >= 700:
    print("\nLoan Status : APPROVED")
    print("Reason : Customer meets all eligibility criteria.")
else:
    print("\nLoan Status : REJECTED")
    print("Reason :")

    if age < 21:
        print("- Age should be at least 21 years.")

    if salary < 30000:
        print("- Monthly salary should be at least 30000.")

    if credit_score < 700:
        print("- Credit score should be at least 700.")