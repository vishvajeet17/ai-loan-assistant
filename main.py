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


def save_application(name, age, salary, credit_score, status):

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


def new_application():

    print("\nNew Loan Application\n")

    name = input("Enter Customer Name: ")
    age = int(input("Enter Age: "))
    salary = float(input("Enter Monthly Salary: "))
    credit_score = int(input("Enter Credit Score: "))

    reasons = check_eligibility(age, salary, credit_score)

    if reasons:
        status = "Rejected"
    else:
        status = "Approved"

    print("\nLoan Report\n")

    print("Customer Name :", name)
    print("Age           :", age)
    print("Salary        :", salary)
    print("Credit Score  :", credit_score)
    print("Loan Status   :", status)

    if reasons:
        print("\nReasons:")

        for reason in reasons:
            print("-", reason)

    save_application(
        name,
        age,
        salary,
        credit_score,
        status
    )

    print("\nApplication Saved Successfully.\n")


def view_applications():

    filename = "loan_data.csv"

    if not os.path.exists(filename):
        print("\nNo Applications Found.\n")
        return

    print("\nAll Applications\n")

    with open(filename, "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(f"{row[0]:15} {row[1]:5} {row[2]:10} {row[3]:10} {row[4]}")


def search_customer():

    filename = "loan_data.csv"

    if not os.path.exists(filename):
        print("\nNo Applications Found.\n")
        return

    customer_name = input("\nEnter Customer Name: ").lower()

    found = False

    with open(filename, "r") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            if row[0].lower() == customer_name:

                print("\nCustomer Details\n")
                print("Name          :", row[0])
                print("Age           :", row[1])
                print("Salary        :", row[2])
                print("Credit Score  :", row[3])
                print("Loan Status   :", row[4])

                found = True
                break

    if not found:
        print("\nCustomer Not Found.\n")


while True:

    print("\nAI Loan Assistant\n")
    print("1. New Loan Application")
    print("2. View All Applications")
    print("3. Search Customer")
    print("4. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        new_application()

    elif choice == "2":
        view_applications()

    elif choice == "3":
        search_customer()

    elif choice == "4":
        print("\nThank you for using AI Loan Assistant.")
        break

    else:
        print("\nInvalid Choice. Please try again.")



