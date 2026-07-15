import csv
import os


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

if not reasons:
    status = "Approved"
else:
    status = "Rejected"

print("\nLoan Report")
print("-")
print("Customer Name :", name)
print("Age           :", age)
print("Salary        :", salary)
print("Credit Score  :", credit_score)
print("Loan Status   :", status)

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)

filename = "loan_data.csv"

file_exists = os.path.isfile(filename)

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Name",
            "Age",
            "Salary",
            "Credit Score",
            "Status"
        ])

    writer.writerow([
        name,
        age,
        salary,
        credit_score,
        status
    ])

print("\nApplication saved successfully.")