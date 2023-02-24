
# Sol 1:

import random

#Welcome note
print("Welcome to the Thesarus App!")

print("\nChoose a word from the thesarus and I will give you a synonym.")

# defining a dictionary
words = {'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
        'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
        'happy': ['content', 'cherry', 'merry', 'jovial', 'jocular'],
        'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
}

#displaying thesarus summary
print("\nHere are the words in thesarus: ")
for key, value in words.items():
    print(f"\t-{key}")

#user input of keys
name = input("\nWhat word would you like a synonym for: ").lower().strip()

if name not in words.keys():
    print("I'm sorry, that word is not currently in the thesarus")
else:
#displaying random choice of values for keys
    for key, value in words.items():
        if name == key:
            print(f"A synonym for {name} is {random.choice(value)}.")

# if name in words.keys():                      another method for above
#     values = random.randint(0,4)                      
#     print(f"A synonym for {name} is {words[name][values]}.")

    #asking yes/no
    que = input("\nWould you like to see the whole thesarus (yes/no): ")

    #displaying final thesarus summary as per que = yes/no
    if que == 'yes':
        for keys, values in words.items():
            print(f"\n{keys.title()} synonyms are:")
            for value in values:
                print(f"\t- {value}")
    else:
        print("I hope you enjoyed the program.  Thank you!")




# Sol :2
import random

#Welcome Note
print("Welcome to the Thesarus App!")

print("\nChoose a word from the Thesarus and I will give you a synonym.")

#displaying keys of dictionary
words = {'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
        'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
        'happy': ['content', 'cherry', 'merry', 'jovial', 'jocular'],
        'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
}

#displaying keys of thesarus
print("\nHere are the words in the thesarus: ")

#looping through words dictionary
for key in words.keys():
    print(f"\t-{key}")

#user choice of input
user_input = input("\nWhat word would you like a synonym for: ").lower().strip()

# radomly choosing values for keys
value = words.values()

#displaying values of user_input keys
for key,value in words.items():
    if key == user_input:
        print(f"A synonym for {user_input} is {random.choice(value)}.")

#displaying whole thesarus    
result = input("\nWould you like to see the whole thesarus (yes/no): ")

if result == 'yes':
    for key, values in words.items():
        print(f"\n{key.title()} synonyms are:")
        for value in values:
            print(f"\t- {value}")
else:
    print("\nI hope you enjoyed the program. Thank you!")    

    