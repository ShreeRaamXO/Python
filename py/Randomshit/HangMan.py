import random

def ChooseRandWord():
    print('For Custom words Say custom , else press enter')
    choice = input()
    if choice != 'custom' or choice != 'Custom':
        words = ['python', 'hangman', 'computer', 'programming', 'language', 'game']
        return random.choice(words)
    else:
        words = []
        n = int(input('enter the number of words you want to have '))
        for i in range (0, n):
            wurd = input('word - ')
            words.append(wurd)
        return random.choice(words)


def showWord(word, GuessedLetters):
    display = ''
    for letter in word:
        if letter in GuessedLetters:
            display += letter
        else:
            display += '_'
            
    return display


print('Welcome to Hangman! ! ')
GuessThis = ChooseRandWord()
maxTries = int(input('enter the number of tries (1 - 10 pls ffs)'))

GuessedLetters = []
tries = 0

print(showWord(GuessThis, GuessedLetters))
running  = True

while running:
    guess = input('Guess a letter: ').lower()

    if guess in GuessedLetters:
        print('You already guessed that letter. Try again.')
    else:
        GuessedLetters.append(guess)

        if guess in GuessThis:
            print('Good guess!')
            print(showWord(GuessThis, GuessedLetters))

        else:
            tries += 1
            print('Incorrect guess.')
            print(f'you got {maxTries - tries} more tries ')

            print(showWord(GuessThis, GuessedLetters))

        if '_' not in showWord(GuessThis, GuessedLetters):
            print('Congratulations! You guessed the word:', GuessThis)
            running = False

        if tries == maxTries:
            print("Sorry, you've run out of tries. The word was: ", GuessThis)
            running = False
