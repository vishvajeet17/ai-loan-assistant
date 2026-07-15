def check_eligibility(age, salary, credit_score):
    reasons = []

    if age < 21:
        reasons.append("Age should be at least 21 years.")

    if salary < 30000:
        reasons.append("Monthly salary should be at least 30000.")

    if credit_score < 700:
        reasons.append("Credit score should be at least 700.")

    return reasons


print("Loan Eligibility Checker")

name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
salary = float(input("Enter Monthly Salary: "))
credit_score = int(input("Enter Credit Score: "))

reasons = check_eligibility(age, salary, credit_score)

print("\nLoan Report")
print("----------------------------")
print("Customer Name :", name)
print("Age           :", age)
print("Salary        :", salary)
print("Credit Score  :", credit_score)

if len(reasons) == 0:
    print("\nLoan Status : APPROVED")
    print("Reason : Customer meets all eligibility criteria.")
else:
    print("\nLoan Status : REJECTED")
    print("Reason :")

    for reason in reasons:
        print("-", reason)