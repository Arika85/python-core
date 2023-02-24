
# Sol : 1         Dictionary Method
# #Welcome Note
print("welcome to the Yes or No Issue Polling App\n")

# taking user-inputs
issue = input("What is the yes or no issue you will be voting on today: ")
no_voters = int(input("What is the number of voters you will allow on the issue: "))
pass_word = input("Enter a password for polling results: ")

result = {}
yes = 0
no = 0

for i in range(no_voters):
    name = input("\nEnter your fullname: ").title().strip()
    if name in result.keys():
        print("Sorry, it seems that someone with that name has already voted")
    else:
        print(f"Here is our issue: {issue}")
        que = input("What do you think...yes or no: ").lower().strip()
        result[name] = que    #appending key and value to dictionary  
        if que == 'yes':
            yes += 1
        elif que == 'no':
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")
        print(f"Thank you {name}! Your vote of {que} has been recorded") #this statement prints for 1st else

#displaying the voters
print(f"\nThe following {len(result.keys())} people voted.")    #len(result) or len(result.keys())
for key in result.keys():
    print(key.title())

#displaying wins of yes/no
print(f"\nOn the following issue: {issue}")
if yes > no:
    print(f"Yes wins! {yes} votes to {no}")
elif no > yes:
    print(f"No wins! {no} votes to {yes}")
else:
    print(f"It's a tie! {yes} votes to {no}")

# Taking admin password input to display voting summary
pass_enter = input("\nTo see the voting results enter the admin password: ")
if pass_enter == pass_word:
    for key, value in result.items():
        print(f"Voter: {key} \t\t\tVote: {value}")
else:
    ("Wrong password")

print("\nThank you for using the Yes or No Issue Polling App")





# Sol 2:        List Method

#Welcome Note
print("welcome to the Yes or No Issue Polling App\n")

# taking user-inputs
issue = input("What is the yes or no issue you will be voting on today: ")
no_voters = int(input("What is the number of voters you will allow on the issue: "))
pass_word = input("Enter a password for polling results: ")

list_name = []
Yes = 0
No = 0

result = []

for i in range(no_voters):
    name = input("\nEnter your fullname: ").title().strip()
    if name not in list_name:
        list_name.append(name)  
        print(f"Here is our issue: {issue}")
        que = input("What do you think...yes or no: ")
        if que == 'yes':
            result.append(que)
            Yes += 1
        elif que == 'no':
            result.append(que)
            No += 1
        else:
            print("That is not a yes or no answer, but okay...")
            print(f"Thank you {name}! Your vote of {que} has been recorded")
    else:
        print("Sorry, it seems that someone with that name has already voted")


#displaying non-duplicated list_names
print(f"\nThe following {len(list_name)} people voted:")
for i in list_name:
    print(i.title())

# counting = input("\nOn the following issue: ").title().strip()
print(f"\nOn the following issue: {issue}")
if Yes > No:
    print(f"Yes wins {Yes} votes to {No}")
elif No > Yes:
    print(f"No wins {No} votes to {Yes}")
else:
    print(f"It was a tie! {Yes} votes to {No}")

# displaying summary
pass_enter = input("\nTo see the voting results enter the admin password: ")
for i, j in zip(list_name, result):
    print(f"Voter: {i} \t\tVote: {j}")

print("Thank you for using the Yes or No Issue Polling App.")


