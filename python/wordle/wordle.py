# to do: add color
# to do: add solving bots (AI with multiple generations, handmade)
# to do: launch flags

import random

def attempt(word_list): # done (check jic)
    while True:
        att = input('the word is: ').lower()
        if att not in word_list:
            print('invalid word. Please try again')
        else:
            return att


def check_attempt(guess, word):
    spelling = []
    for i, letter in enumerate(guess):


        if letter == word[i]:
            spelling.append(f"\033[92m{letter.upper()}\033[0m" )
        elif letter in word:
            spelling.append(f"\033[93m{letter}\033[0m")
        else:
            spelling.append( '#' )
    return " ".join(spelling)


def game(word, word_list, used):
    attempts = int( input('atts: ') ) or 6
    player = str( input('play: ') ) or 'y' # to do
    if player == 'y':
        pass
    else:
        print('this will be an input to choose bots instead of a print')

    for _ in range(attempts):
        guess = attempt(word_list)
        
        if guess == word:
            print(f"\033[92m{word.upper()}\033[0m is correct! You win!")
            break
        else:
            tried = check_attempt(guess, word)  # remove `used` if not needed
            print(tried)
            used.append(guess)

################################################################################

with open("word_list.txt", "r") as f:
    word_list = [line.strip().lower() for line in f]

random_word = random.choice(word_list)

used_words = []

game(random_word, word_list, used_words)
