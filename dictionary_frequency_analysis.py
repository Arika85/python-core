# Sol :1

from collections import Counter
import collections

#Welcome Note
print("Welcome to the Frequency Analysis App")

sentence = input("\nEnter a word or phrase to count the occurence of each letter: ").lower()

print("\nHere is the analysis from key phrase 1: \n")

letters = []    #initiatlizing empty list to save only alphabets from sentence

# displaying only alphabets and appending to list of letters =[]
for char in sentence:
    if char.isalpha():
        le = char
        letters.append(le)

# Counter used to convert alphabets and their counts in dictionary form
# saving counter of letters in x variable
x = Counter(letters)     
y = x.most_common()        # high frequency appears from 1st using [ .most_common() method ]

# iterating and saving numbers of y dictionary values in empty list of...... list_numbers = []
# to calculate sum and count of numbers for percentage
list_num = []

for key,value in y:
    num = value
    list_num.append(num)

total = sum(list_num)       # sum of all values to calc percentage
length = len(list_num)      # length/count of values to calc %

#diplaying summary of frequency
letter_ord = []

print("\tLetter\t\tOccurence\t\tPercentage")
for i,j in y:                                       # 1st method
    percent = 100*j/total
    letter_ord.append(i)
    print(f"\t{i}\t\t{j}\t\t\t{round(percent, 2)}%")

# for i in y:                                       # 2nd method
#     print(f"\t{i[0]}\t\t{i[1]}\t\t\t{0}")

#displaying letters in string from highest to lowest
print("\nLetters ordered from highest occurence to lowest:")
print(f"{''.join(letter_ord)}")

print("\n************************************************")

# copy of above code to generate second sentence
# code for second input for sentence / phrase - 2

sentence_2 = input("\nEnter a word or phrase to count the occurence of each letter: ").lower()

print("\nHere is the analysis from key phrase 2: \n")

letters_2 = []    #initiatlizing empty list to save only alphabets from sentence

# displaying only alphabets and appending to list of letters =[]
for char in sentence_2:
    if char.isalpha():
        le_2 = char
        letters_2.append(le_2)

# Counter used to convert alphabets and their counts in dictionary form
# saving counter of letters in x variable
x2 = Counter(letters_2)     
y2 = x2.most_common()        # high frequency appears from 1st using [ .most_common() method ]

# iterating and saving numbers of y dictionary values in empty list of...... list_numbers = []
# to calculate sum and count of numbers for percentage
list_num_2 = []

for key,value in y2:
    num_2 = value
    list_num_2.append(num_2)

total_2 = sum(list_num_2)       # sum of all values to calc percentage
length_2 = len(list_num_2)      # length/count of values to calc %

#diplaying summary of frequency
letter_ord_2 = []

print("\tLetter\t\tOccurence\t\tPercentage")
for i,j in y2:                                       # 1st method
    percent = 100*j/total_2
    letter_ord_2.append(i)
    print(f"\t{i}\t\t{j}\t\t\t{round(percent, 2)}%")

#displaying letters in string from highest to lowest
print("\nLetters ordered from highest occurence to lowest:")
print(f"{''.join(letter_ord_2)}")

print("\n************************************")

# Sol 2:        # Shubham's code

# welcom screen
from collections import Counter
print('Welcom to Frequency Analysis App.')

# user input 
phrase = input('\nEnter a word or phrase to count the occurrence of each letter: ').lower().strip()

# for loop to chech the alphabets
a_list= []
for i in phrase:
    if i.isalpha():
        a_list.append(i)

# joining back the letters from list
only_letters = ''.join(a_list)

# total occurances
total_occ = len(only_letters)


# ini letter counter
letter_count = Counter(only_letters)

# printing
print('\nHere is the frequency analysis from Key Phrase 1: ')
print('\n\tLetters\t\tOccurances\tPercentage')

# sort_letter = []
for key, value in letter_count.items():
    percentage = round(100*value/total_occ)
    # sort_letter.append(key)
    print(f'\t{key}\t\t{value} \t\t{percentage}%')

# sort_letter_1 = ''.join(sort_letter)
# printing highest to lowest
# print(f'\nLetters highest to lowest {sort_letters_1}')


print("\n************************************************")


# to sort a list
# y = sorted(x.items(), key=lambda pair: pair[1], reverse=True)


# from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
