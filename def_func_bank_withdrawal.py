# welcome screen
print('Welcome to the Python First National Bank')

# name
name = str(input('\nWhat is your name: ')).title().strip()
savings_account = int(input('How much money would you like to set up your saving account with: '))
checking_account = int(input('How much money would you like to set up your checking account with: '))

# empty dictionary
savings = [savings_account]
checking = [checking_account]

# a_list = [1, 2, 3, 4]
# a_list[0]

# current account variable
print(f'\nName: {name}')
print(f'Savings: {savings[0]}')
print(f'Checking: {checking[0]}')

# functions
def balance(name, savings, checking):
    print(f'\nName: {name}')
    print(f'Savings: {sum(savings)}')
    print(f'Checking: {sum(checking)}')

def func_savings(money):
    if transaction == 'deposit' or transaction == 'd':
        savings.append(money)
        print(f'\nDeposited {money} into {name}\'s saving account.')
    else:
        print('Operation not allowed.')

def func_checking(money):
    if transaction == 'deposit' or transaction == 'd':
        checking.append(money)
        print(checking)
        # print(f'\nDeposited {money} into {name}\'s checking account.')
    elif transaction == 'withdraw' or transaction == 'w':
        if money < sum(checking):
            checking[0] -= money
            print(checking)
            # print(f'\nWithdrawn {money} from checking account.')
            # checking.append(result)
        else:
            print(f'Sorry, by withdrawing ${money} you will have a negative balance.')
    else:
        print('Operation not allowed.')


flag = True
while flag:
    # balance(name, savings, checking)
    # que
    option = str(input('\nWhat account would you like to access (Savings/Checking): ')).lower().strip()
    transaction = str(input('What type of transaction would you like to make (Deposit/Withdrawal): ')).lower().strip()
    money = int(input('How much money: '))

    if option == 'savings' or option == 's':
        func_savings(money)
    elif option == 'checking' or option == 'c':
        func_checking(money)
    else:
        print('Sorry, we cannot do that for you today.')


    choice = str(input('\nWould you like to run the program again(y/n): ')).lower()
    if choice != 'y':
        flag = False
        # print(f'\nName: {name}')
        # print(f'Savings: {sum(savings)}')
        # print(f'Checking: {sum(checking)}')
        balance(name, savings, checking)
        print('Okay Goodby')
    else:
    #     print(f'\nName: {name}')
    #     print(f'Savings: {sum(savings)}')
    #     print(f'Checking: {sum(checking)}')
        balance(name, savings, checking)





# #Welcome Note
print('Welcome to the Python First National Bank\n')

res_dict = {}

name = input("Hello, what is your name: ").title()
saving = int(input("How much money would you like to set up your savings account with: "))
checking = int(input("How much money would you like to set up your savings account with: "))
    
print("\nCurrent Account Information")
print(f"Name: {name}")
print(f"Savings: ${saving}")
print(f"Checkings: ${checking}")

account = input("\nWhat account would you like to access(Savings or Checking): ").title()
transaction = input("What type of transaction would you like to make(Deposit or withdrawal): ")
money = int(input("How much money: "))

if account == 'savings' and transaction == 'deposit':
    res_dict['Savings'] = saving + money    
    print(f"Deposited ${money} into {name}'s savings account.")
elif account == 'savings' and transaction == 'withdrawal':
    res_dict['Savings'] = saving - money
    print(f"Withdrew ${money} from {name}'s savings account.")
elif account == 'checking' and transaction == 'deposit':
    res_dict['Checking'] = checking + money
    print(f"Deposited ${money} into {name}'s checking account.")
elif account == 'checking' and transaction == 'withdrawal':
    res_dict['Checking'] = checking - money
    print(f"Withdrew ${money} from {name}'s checking account.")
else:
    print("I'm sorry, we cannot do that for you today")
            
       
# flag = True
# while flag:
#     info()

        
        










