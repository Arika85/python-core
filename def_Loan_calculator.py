#Welcome note
print("Welcome to the Loan Calculator App")

# loan requirements information
def loan_info():
    loan_dict = {}

    loan_dict['Principal'] = float(input("\nEnter the loan amount: "))
    loan_dict['Rate'] = float(input("Enter the interest rate: "))/100
    loan_dict['Monthly Payment'] = int(input("Enter the desired monthly payment: "))
    loan_dict['Money Paid'] = 0
    return loan_dict

           
def repayment_info(loan_dict, period):
    print(f"\n----Loan information after {period} months")
    for key, value in loan_dict.items():
        print(f"{key}: {value}")

flag = True
while flag: 
    a = loan_info()
    repayment_info(a, 100)
    break


