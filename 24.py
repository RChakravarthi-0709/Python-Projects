import datetime as dt

gameWords = []
playerPoints = 0
computerPoints = 0
moreRounds = True
loss = False

gameLang = input("What language would you like? ").lower()  #en for english, sp for spanish
if gameLang == "es":
    filename = "strings_es.txt"
else:
    filename = "strings_en.txt"
s1 = open(filename)
gameStrings = s1.read().splitlines()
f1 = open(gameStrings[0], "r")
allWords = f1.read().splitlines()
numEntries = len(allWords)
computerWord = ""
word = input(gameStrings[1])
word.strip()
loss = True if word.lower() not in allWords else False
if not loss:
    wordPoints = len(word)
    playerPoints += wordPoints
    gameWords.append(word)
    necessaryLetter = word[-1]
    while computerWord == "":
        for i in range(numEntries):
            if allWords[i][0] == necessaryLetter:
                computerWord = allWords[i].lower()
    gameWords.append(computerWord)
    wordPoints = len(computerWord)
    computerPoints += wordPoints
    print(f"{word} - {computerWord} ({len(word)} - {len(computerWord)})")
    j = 2
while not loss and j <= 4:
    timerStart = dt.datetime.now().second
    valid = False
    necessaryLetter = computerWord[-1]
    while not valid:
        word = input()
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
    wordPoints = len(word)
    playerPoints += wordPoints
    gameWords.append(word)
    necessaryLetter = word[-1]
    while computerWord == "":
        for i in range(numEntries):
            if allWords[i][0] == necessaryLetter and allWords[i] not in gameWords:
                computerWord = allWords[i].lower()
    gameWords.append(computerWord)
    wordPoints = len(computerWord)
    computerPoints += wordPoints
    print(f"{word} - {computerWord} ({len(word)} - {len(computerWord)})")
    j += 1
if loss:
    print(gameStrings[2])
    print(gameStrings[3], computerPoints)
    print(gameStrings[4], playerPoints)
else:
    print(gameStrings[3], computerPoints)
    print(gameStrings[4], playerPoints)
    if playerPoints > computerPoints:
        print(gameStrings[5])
    elif playerPoints == computerPoints:
        print(gameStrings[6])
    else:
        print(gameStrings[7])