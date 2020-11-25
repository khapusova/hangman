
import random
import string
import string
import re
WORDLIST_FILENAME = 'D:\words.txt'
letters_guessed = []


def ifguessed(secret_word,letters_guessed):
    if '_' in get_guessed_word(secret_word, letters_guessed):
        return False
    else:
        return True
def load_words():

    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')

    line = inFile.readline()

    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

    secret_word = list(secret_word)
    for i in secret_word:
        if not i in letters_guessed:
             return False
        return True


def get_guessed_word(secret_word, letters_guessed):

    outputdata = []
    for i in secret_word:
        if i in letters_guessed:
            outputdata.append(i)
        else:
            outputdata.append('_ ')
    outputdata = ''.join(outputdata)
    return outputdata


def get_available_letters(letters_guessed):
    alf = string.ascii_lowercase
    alf = list(alf)
    for i in letters_guessed:
        if i in alf:
          alf.remove(i)
        else:
            pass
    alf = ''.join(alf)
    return alf

def hangman(secret_word):
     guesses_remaining = 6
     warnings_remaining = 3

     def try_letter():
         nonlocal guesses_remaining
         nonlocal warnings_remaining
         if warnings_remaining > 0:
             warnings_remaining -= 1
             str1 = warnings_remaining, 'warnings left:'
             return str1
         else:
             guesses_remaining -= 1
             str2 = guesses_remaining, 'guesses left:'
             return str2

     lengthword = len(secret_word)
     letters_guessed = []
     lengthunic = len(set(secret_word))
     print('Welcome to the game Hangman!', '\n' , 'I am thinking of a word that is ', lengthword, ' letters long.', '\n',
          'You have 6 guesses left.', '\n' , 'Available letters:', get_available_letters(letters_guessed))

     while True:
        if ifguessed(secret_word, letters_guessed) == True:
             print('Congratulations, you won! Your total score for this game is:', (popytka * lengthunic))
             break
        letter = input('Please guess a letter: ')

        if not len(letter) == 1 or not (65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122) <= 122:
              print('Oops! That is not a valid letter. You have', try_letter(), '\n' ,'---------------------------------------------------------' , '\n' , 'You have', guesses_remaining,'guesses left.', '\n' , 'Available letters:', get_available_letters(letters_guessed))
        else:
             letter = letter.lower()
             if letter in letters_guessed:
                 print( try_letter())
             else:
                 letters_guessed.append(letter)
                 if letter in secret_word:
                     print('Good guess:', get_guessed_word(secret_word, letters_guessed), '\n' , 'You have', guesses_remaining,'guesses left.', '\n' , 'Available letters:', get_available_letters(letters_guessed))
                     continue
                 else:
                     if letter == 'a' or letter == 'o' or letter == 'i' or letter == 'e' or letter == 'u':
                         guesses_remaining -= 2
                         if guesses_remaining < 0:
                             print('Sorry, you ran out of guesses. The word was else', secret_word)
                             break
                     else:
                         guesses_remaining -= 1
                         if guesses_remaining < 0:
                             print('Sorry, you ran out of guesses. The word was else', secret_word)
                             break
                 print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed), '\n' ,'---------------------------------------------------------' , '\n' , 'You have', guesses_remaining,'guesses left.', '\n' , 'Available letters:', get_available_letters(letters_guessed))
                 continue

def match_with_gaps(my_word, other_word):
    p = '_ '
    k1 = []
    my_word = list(my_word)
    while my_word:
        x = my_word.pop(0)
        if x == '_':
            x += my_word.pop(0)
        k1.append(x)
    if len(k1)!= len(other_word):
        return False
    else:
        for i in range(len(k1)):
            if k1[i] != other_word[i] and k1[i] != p:
                return False
            else:
                pass
        return True


def show_possible_matches(my_word):
    mat = []
    k1 = []
    my_word = list(my_word)
    while my_word:
        x = my_word.pop(0)
        if x == '_':
            x += my_word.pop(0)
        k1.append(x)
    my_word = k1
    for word in wordlist:
        if len(my_word) == len(word):
            pokazatel = 0
            for i in range(0, len(my_word)):
                if my_word[i] =='_ ' or  my_word[i] == word[i]:
                    pass
                else:
                    pokazatel = 1
            if pokazatel == 0:
                mat.append(word)
        else:
                continue
    return mat
def hangman_with_hints(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3

    def try_letter():
        nonlocal guesses_remaining
        nonlocal warnings_remaining
        if warnings_remaining > 0:
            warnings_remaining -= 1
            str1 = warnings_remaining, 'warnings left:'
            return str1
        else:
            guesses_remaining -= 1
            str2 = guesses_remaining, 'guesses left:'
            return str2

    lengthword = len(secret_word)
    letters_guessed = []
    lengthunic = len(set(secret_word))
    print('Welcome to the game Hangman!', '\n', 'I am thinking of a word that is ', lengthword, ' letters long.', '\n',
          'You have 6 guesses left.', '\n', 'Available letters:', get_available_letters(letters_guessed))

    while True:
        if ifguessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won! Your total score for this game is:', (guesses_remaining * lengthunic))
            break
        letter = input('Please guess a letter: ')
        if letter == '*':
            print('Possible word matches are:', show_possible_matches(get_guessed_word(secret_word,letters_guessed)))
        elif not len(letter) == 1 or not (65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122):
            print('Oops! That is not a valid letter. You have', try_letter(), '\n',
                  '---------------------------------------------------------', '\n', 'You have', guesses_remaining,
                  'guesses left.', '\n', 'Available letters:', get_available_letters(letters_guessed))
        else:
            letter = letter.lower()
            if letter in letters_guessed:
                print(try_letter())
            else:
                letters_guessed.append(letter)
                if letter in secret_word:
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed), '\n', 'You have', guesses_remaining,
                          'guesses left.', '\n', 'Available letters:', get_available_letters(letters_guessed))
                    continue
                else:
                    if letter == 'a' or letter == 'o' or letter == 'i' or letter == 'e' or letter == 'u':
                        guesses_remaining -= 2
                        if guesses_remaining < 0:
                            print('Sorry, you ran out of guesses. The word was else', secret_word)
                            break
                    else:
                        guesses_remaining -= 1
                        if guesses_remaining < 0:
                            print('Sorry, you ran out of guesses. The word was else', secret_word)
                            break
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed), '\n',
                      '---------------------------------------------------------', '\n', 'You have', guesses_remaining,
                      'guesses left.', '\n', 'Available letters:', get_available_letters(letters_guessed))
                continue



if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

# для того, щоб програма не закривалася після перемоги
fornot = input()


 #   secret_word = choose_word(wordlist)
  #  hangman(secret_word)


