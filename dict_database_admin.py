
#welcome note
print("Welcome to the Database Admin Program\n")

dict = {
    'apple':'apple100',
    'samsung':'samsung80',
    'vivo':'vivo60000',
    'admin':'admin0007'
}

#         or    can add new items to empty dictionary as below

# users_list = {}
# users_list['oppo'] = 'oppo12345'
# users_list['android'] = 'android200'
# print(users_list)

user = input("Enter your username: ")

if user in dict.keys():
    pw = input("Enter your password: ")         #old password
    print(f"\nHello {user}! You are logged in")
    if user == 'admin' and pw == 'admin0007':
        print("\nHere is the current user database:")   #displaying database summary
        for key, value in dict.items():
            print(f"Username: {key} \t\tPassword: {value}")
    else:
        change = input("Would you like to change your password: ")  
        new_pass = input("What would you like your new password to be: ")   #new password
        if change == 'yes' and len(new_pass) >= 8:
            print(f"\n{user} your password is {new_pass}")
        else:
            print(f"{new_pass} is not the minimum eight characters.")
            print(f"\n{user} your password is {pw}")
else:
    print("Username not in database, goodbye.")





# Sol :2

dict = {'arika': 'arika1234',
'shubham': 'shubham6789',
'aditi': 'aditi56712',
'admin': 'admin0000',
}

#Welcome Note
print("Welcome to the Database Admin Program")

# user inputs of username and password
user = input("\nEnter your username: ")

if user in dict.keys():
    pw = input("Enter your password: ")
    if user == 'admin' and pw == 'admin0000':
        print("\nHere is the current user database:")
        for key, value in dict.items():
            print(f"Username: {key} \tPassword: {value}")
    else:
        # displaying the login details of user
        print(f"\nHello {user}!  You are logged in!")
        # prompting for a change of password with updation of new_password
        change = input("Would you like to change your password: ")
        new_password = input("What would you like your new password to be: ")

            #displaying results of user with pw change if yes
        if change == 'yes' and len(new_password) >= 8:
            print(f"\n{user} your password is {new_password}")
        else:
            print(f"{new_password} not the minimum eight characters")
            print(f"\n{user} your password is {pw}")
else:
    print("Username not in database, goodbye")




