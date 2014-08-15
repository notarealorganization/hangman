import random
HANGMAN = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
def getrandomword (wordlist):
    wordindex = random.randint (0, len(wordlist) - 1)
    return wordlist [wordindex]
def displayboard (HANGMAN, missedletters, correctletters, sercretword):
    print(HANGMAN [len (missedletters)])
    print ()
    print ('missed letters:' , end=' ')
    for letter in missedletters :
        print (letter, end=' ')
    print ()

    blanks = '-' * len(secretword)

    for i in range(len(secretword)):
            if secretword[i] in correctletters :
                   blanks = blanks[:i] + secretword[i] + blanks[i + 1:]
    for letter in blanks:
         print (letter, end=' ')
    print ()

def getguess (alreadyguessed):
        while True :
                print ('Guess a letter.')
                guess = input()
                guess = guess.lower()
                if len(guess) != 1:
                   print ('Please enter a single letter')
                elif guess in alreadyguessed:
                   print ('you have already guessed that letter, choose again')
                elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                   print ('Please enter a LETTER.')
                else:
                   return guess

def playagain ():
            print ('do you want to play again?')
            return input ().lower().startswith ('y')



print ('H A N G M A N')
missedletters = ' '
correctletters = ' '
secretword = getrandomword(words)
gameisdone = False
while True:
    displayboard (HANGMAN, missedletters,correctletters,secretword)
    
    
    guess = getguess (missedletters + correctletters)
    
   
    if guess in secretword:
        correctletters = correctletters + guess

        foundallletters = True
        for i in range(len(secretword)):
             if secretword[i] not in correctletters:
                   foundallletters = False
                   break
        if foundallletters:
            displayboard(HANGMAN, missedletters, correctletters, secretword)
            print('Yes! The secret word is "' + secretword +'"! You won!')
            gameisdone = True
    else:
        
        missedletters = missedletters + guess

        if len(missedletters) == len(HANGMAN) - 1:
                   displayboard(HANGMAN, missedletters, correctletters, secretword)
                   print ('you ran out of guesses ! \nThe word was ' + secretword)
                   gameisdone = True
    
    if gameisdone:
        if playagain ():
            missedletters = ' '
            correctletters = ' '
            gameisdone = False
            secretword = getrandomword (words)
        else:
            break 
        
    
        
                   
