
# # from collections import Counter

# # count = Counter("hi,hello,hey,here")
# # print(count['l'])


# # Question 1:

# Type: 1
print("Welcome to the Letter Counter App")
name = input("\nWhat is your name: ").capitalize()
print('Hello' + ' ' + name.capitalize() +'!')
print('I will count the number of times that a specific letter occurs in a message.\n')

msg = input('Please enter a message: ')
msg1 = input('\nWhich letter would you like to count the occurrences of: ').lower()

result = msg.count(msg1)

print(f"{name}, your message has {result} {msg1}'s in it.")

# Type: 2
print('Welcome to the Letter counter app' )
name= input(' What is your name:')
print('Hello', name,"!")
print('I will count the number of the times that a specific letter occurs in a message')

msg = input('Please enter message:')
ques = input('Which letter would you like to count the occurence of:')
occur =msg.count('')
print(name,',your message has',occur,'in it')

# # Type: 3
print("Welcome to the Letter Counter App\n")

name = input("What is your name? ")
print(f"Hello {name}!\n")

print("I will count the number in the given message!")
message = input("What is the message?: ").lower()
letter = input("Which letter you want to count: ").lower()

count_let = message.count(letter)

print(f"{name} you have {count_let} {letter}'s in your message")

