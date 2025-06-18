import datetime as dt

gameWords = []
playerPoints = 0
computerPoints = 0
moreRounds = True
loss = False
f1 = open("dictionary.txt")
allWords = f1.read().splitlines()
numEntries = len(allWords)
print("New Game:")
valid = False
computerWord = ""
while not valid :
    word = input("Please enter the first word: ")
    word.strip().lower()
    valid = True if word.lower() in allWords else False
wordPoints = len(word)
playerPoints += wordPoints
print(f"Your word was '{word}' worth {wordPoints} points")
gameWords.append(word)
necessaryLetter = word[-1]
while computerWord == "":
    for i in range(numEntries):
        if allWords[i][0] == necessaryLetter:
            computerWord = allWords[i].lower()
gameWords.append(computerWord)
wordPoints = len(computerWord)
computerPoints += wordPoints
print(f"The computers word was '{computerWord}' worth {wordPoints} points")
print(f"TOTAL SCORE:")
print(f"Player: {playerPoints} points")
print(f"Computer: {computerPoints} points")
userInput = input("Would you like to continue? ").strip()
moreRounds = True if userInput.lower() == "yes" else False
while moreRounds and not loss:
    timerStart = dt.datetime.now().second
    valid = False
    necessaryLetter = computerWord[-1]
    while not valid:
        word = input(f"Please enter a unique word starting with '{necessaryLetter}' in under 30 seconds: ")
        word = word.strip().lower()
        now = dt.datetime.now().second
        timePassed = now - timerStart
        if timePassed >= 30 or word in gameWords or word not in allWords or word[0] != computerWord[-1]:
            loss = True
            break
        valid = True
    computerWord = ""
    if loss:
        break
    else:
        wordPoints = len(word)
        playerPoints += wordPoints
        print(f"Your word was '{word}' worth {wordPoints} points")
        gameWords.append(word)
        necessaryLetter = word[-1]
        while computerWord == "":
            for i in range(numEntries):
                if allWords[i][0] == necessaryLetter and allWords[i] not in gameWords:
                    computerWord = allWords[i].lower()
        gameWords.append(computerWord)
        wordPoints = len(computerWord)
        computerPoints += wordPoints
        print(f"The computers word was '{computerWord}' worth {wordPoints} points")
        print(f"TOTAL SCORE:")
        print(f"Player: {playerPoints} points")
        print(f"Computer: {computerPoints} points")
        userInput = input("Would you like to continue? ").strip()
        moreRounds = True if userInput.lower() == "yes" else False
if loss:
    print("Invalid word, better luck next time")
else:
    print(f"Computer score was: {computerPoints}")
    print(f"Your score was: {playerPoints}")
    if playerPoints > computerPoints:
        print("Good job, you beat the computer!")
    elif playerPoints == computerPoints:
        print("Good effort, you tied the computer!")
    else:
        print("Nice try, the computer wins.")