
from collections import Counter
import collections

#Welcome Note
print("Welcome to the Frequency Analysis App")

sentence = """A woman finds a pot of treasure on the road while she is returning from work.
Delighted (very happy) with her luck, she decides to keep it. As she is taking it home, it keeps changing.
However, her enthusiasm refuses to fade away (disappear or faint slowly).
What Is Great About It: The old lady in this story is one of the most cheerful characters anyone can encounter in English fiction.
Her positive disposition (personality) tries to make every negative situation seem like a gift, and she helps us look at luck as a matter of our view rather than events.
This classic fable (story) tells the story of a very slow tortoise (turtle) and a speedy hare (rabbit).
The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than he, but the race leads to surprising results.
What Is Great About It: Have you ever heard the English expression, “Slow and steady wins the race”? This story is the basis for that common phrase.
This timeless (classic) short story teaches a lesson that we all know but can sometimes forget: Natural talent is no substitute for hard work, and overconfidence often leads to failure.
Timmie Willie is a country mouse who is accidentally taken to a city in a vegetable basket. When he wakes up, he finds himself at a party and makes a friend.
When he is unable to bear (tolerate or experience) the city life, he returns to his home but invites his friend to the village.
When his friend visits him, something similar happens.
What Is Great About It: Humans have been living without cities or villages for most of history.
That means that both village and city life are recent inventions. And just like every other invention, we need to decide their costs and benefits.
The story is precisely (exactly) about this debate. It is divided into short paragraphs and has illustrations for each scene. This is best for beginners who want to start reading immediately."""

print("\nHere is the analysis from key phrase 1: \n")

letters = []    #initiatlizing empty list to save only alphabets from sentence

# displaying only alphabets and appending to list of letters =[]
for char in sentence:
    if char.isalpha():
        le = char.lower()
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


sentence_2 = """ADHD symptoms arise from executive dysfunction,[6][7][8] and emotional dysregulation is often considered a core symptom.[9][10][11] In children, problems paying attention may result in poor school performance. ADHD is associated with other neurodevelopmental and mental disorders as well as some non-psychiatric disorders, which can cause additional impairment, especially in modern society. Although people with ADHD struggle to focus on tasks they are not particularly interested in completing, they are often able to maintain an unusually prolonged and intense level of attention for tasks they do find interesting or rewarding; this is known as hyperfocus.

The precise causes of ADHD are unknown in the majority of cases.[12][13] Genetic factors play an important role; ADHD tends to run in families and has a heritability rate of 74%.[14] Toxins and infections during pregnancy and brain damage may be environmental risks.

It affects about 5–7% of children when diagnosed via the DSM-IV criteria, and 1–2% when diagnosed via the ICD-10 criteria. Rates are similar between countries and differences in rates depend mostly on how it is diagnosed.[15] ADHD is diagnosed approximately twice as often in boys than in girls,[3] and 1.6 times more often in men than in women,[3] although the disorder is overlooked in girls or diagnosed in later life because their symptoms sometimes differ from diagnostic criteria.[16][17][18][19] About 30–50% of people diagnosed in childhood continue to have ADHD in adulthood, with 2.58% of adults estimated to have ADHD which began in childhood.[20][21][text–source integrity?] In adults, hyperactivity is usually replaced by inner restlessness, and adults often develop coping skills to compensate for their impairments. The condition can be difficult to tell apart from other conditions, as well as from high levels of activity within the range of normal behavior. ADHD has a negative impact on patients’ health related quality of life and that this may be further exacerbated by, or may increase the risk of, other psychiatric conditions such as anxiety and depression."""

print("\nHere is the analysis from key phrase 2: \n")

letters_2 = []    #initiatlizing empty list to save only alphabets from sentence

# displaying only alphabets and appending to list of letters =[]
for char in sentence_2:
    if char.isalpha():
        le_2 = char.lower()
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

print("\n**************************************")


# import base64
# import codecs

# choice = input("Would you like a encode or decode a message: ")

# if choice == 'encode':
#     phrase = input("What is the phrase: ").lower().strip()
#     phrase_enc = base64.b64encode(phrase.encode('utf-8', errors='strict'))
#     print(phrase_enc)
# else:
#     phrase_dec = base64.b64decode(input("What is the phrase: "))
#     print("The decoded message is: ")
#     print(phrase_dec)

a = ''.join(letter_ord)
b = ''.join(letter_ord_2)




# letters = []    #initiatlizing empty list to save only alphabets from sentence

# # displaying only alphabets and appending to list of letters =[]
# for char in phrase:
#     if char.isalpha():
#         le = char.lower()
#         letters.append(le)

# if choice == 'encode':
#     encoded_phrase = []
#     for letter in phrase:
#         index = a.index(letter)
#         letter = b[index]
#         encoded_phrase.append(letter)

# for letter in encoded_phrase:
#     print(letter, end='')