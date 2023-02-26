import random

#Welcome note
print("Welcome to the Guess My Word App")

words_dict = {"fruits": ["apple", "banana", "grapes", "strawberry"],
"sports": ["basketball", "football", "cricket", "kabadi"],
"veggies": ["tomato", "potato", "carrots", "greenpeas"],
}

# words_keys = words_dict.keys()        #To access keys of dictionary

#saving keys of dictionary in an empty list
words_keys = []
for i in words_dict.keys():
    words_keys.append(i)

flag = True
while flag:

    #randomly choosing keys of dictionary
    game_category_key = random.choice(words_keys)

    #accessing values of dictionary from a choice random key of game_category
    game_word_value = random.choice(words_dict[game_category_key])

    #displaying len of word
    print(f"\nGuess a {len(game_word_value)} letter word from the following category: {(game_category_key).title()}")

    dash = []
    for i in game_word_value:
        # j = '-'
        # # print("-", end = "")
        dash.append('-')

    guess = ''
    guess_count = 0

    while guess != game_word_value:
        print(''.join(dash))
        guess = input("\nEnter your guess: ").lower()
        guess_count += 1
        if guess == game_word_value:
            print(f"Correct! You guessed the word in {guess_count} guesses.")
            break
        else:
            print("That is not correct.  Let us reveal a letter to help you!")
            while True:
                letter_index = random.randrange(0, len(game_word_value))
                if dash[letter_index] == "-":
                    dash[letter_index] = game_word_value[letter_index]
                    break

    choice = input("\nWould you like to play again(y/n): ").lower()
    if choice != 'y':
        flag = False
        print("Thank you for playing the game")


# sol:2
import random
# welcome screen
print('Welcome to the Guess My Word App')

# defining dictionaries
the_dict = {
    'sports': ['football', 'basketball', 'cricket', 'kabaddi'],
    'fruits': ['sitafal', 'mango', 'apple', 'orange'],
    'animals': ['dog', 'cat', 'fish', 'cow', 'crow']
}

# loop
playing = True
while playing:
    # randomly pick game category and game word
    the_seq =  random.choice(list(the_dict))    #the_dict[random.choice(sports)]
    the_word = random.choice(list(the_dict[the_seq]))

    # build a dashed word to represent game word
    blank_word = []
    for letter in the_word:
        blank_word.append('-')

    print(f'\nGuess the {len(the_word)} letter word from the following category: {the_seq.title()}')

    # initializing 
    guess_count = 0
    guess = ''

    # single round loop
    while guess != the_word:
        print("".join(blank_word))
        guess = str(input('\nEnter your guess: ')).lower().strip()
        guess_count += 1

        # guess is correct 
        if guess == the_word:
            print(f'\nCorrect you guessed it right {guess_count} tries')
            break
        # guess is incorrect user must keep guessing
        else:
            print('That is not correct let us reveal a letter to help you!')
            # loop to replace '-' in blank_word
            swapping = True
            while swapping:
                letter_index = random.randint(0, len(the_word)-1)
                # print(letter_index)
                if blank_word[letter_index] == '-':
                    blank_word[letter_index] = the_word[letter_index]
                    swapping = False

    # choice
    choice = str(input('\nWould you like play again(y/n): ')).lower()
    if choice != 'y':
        playing = False
        print('Thank you for playing game.')