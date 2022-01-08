# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:18:57 2022



@author: nilay
"""
#TO DO
#test for user input better so it doesn't crash with a misinput


#INTRODUCTION
print("==================================================================================================================")
print("WELCOME TO PYTHON HANGMAN")
print("This program was created by Nilay Patel")
print("The concept of this program is from jan Misali on YouTube: https://www.youtube.com/watch?v=le5uGqHKll8&t=318s.")
print("He came up with an astonishing algorithm, and I used a very similar algorithm to make it into a Python bot.")
print("The shell of this program can be found at: https://scratch.mit.edu/projects/618296886/. This was made as a")
print("concept for class.")
print()
print("DISCLAIMER: The imported dictionary I used may not have every word in the English language. If this program does")
print("not guess the word you were thinking of, then it is an issue with the dictionary itself, not the program.")
print("DISCLAIMER: Words with apostrophes or hyphens have been omitted from this list.")
print("DISCLAIMER: I wrote small programs to turn a 600k dictionary into several, mini dictionaries.")
print()
print("Please enjoy!")
print("==================================================================================================================")

#DEFINE GLOBAL VARIABLES
global remainingWords
remainingWords = []
global alphabetCount
alphabetCount = []
global alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
global storedName
storedName = ""
global guessedLetters
guessedLetters = ""

#FUNCTIONS
def removeWordsWith(letter):
    global remainingWords
    global alphabetCount
    global alphabet
    global storedName
    global guessedLetters
    
    removeCount = 0
    while (removeCount < len(remainingWords)):
        if (letter in remainingWords[removeCount]):
            remainingWords.pop(removeCount)
        else:
            removeCount += 1     
    if len(remainingWords) == 0:
        print("One of us had to have made a mistake...")
    elif len(remainingWords) == 1:
        guessedRight = input("Is your word " + remainingWords[0] + " (Y/N): ")
        if guessedRight == "Y":
            print("Thank you for playing!")
        elif guessedRight == "N":
            print("Aww man. Still, thank you for playing!")
    else:
        guessLetter()
        
def removeWordsWithout(letter, nameStored):
    global remainingWords
    global alphabetCount
    global alphabet
    global storedName
    global guessedLetters
    
    removeCount = 0
    
    while (removeCount < len(remainingWords)):
        currentWord = remainingWords[removeCount]
        matchStored = True
        for x in range(0, len(nameStored)):
            if ((nameStored[x] != currentWord[x]) and (nameStored[x] != "-")):
                matchStored = False
        if (matchStored == False):
            remainingWords.pop(removeCount)
        else:
            removeCount += 1
        
    removeCount = 0
    while (removeCount < len(remainingWords)):
        currentWord = remainingWords[removeCount]
        matchStored = True
        for x in range(0, len(nameStored)):
            if ((nameStored[x] == "-") and (currentWord[x] == letter)):
                matchStored = False
        if (matchStored == False):
            remainingWords.pop(removeCount)
        else:
            removeCount += 1
        
    if len(remainingWords) == 0:
        print("One of us had to have made a mistake...")
    elif len(remainingWords) == 1:
        guessedRight = input("Is your word " + remainingWords[0] + " (Y/N): ")
        if guessedRight == "Y":
            print("Thank you for playing!")
        elif guessedRight == "N":
            print("Aww man. Still, thank you for playing!")
    else:
        guessLetter()
        

def guessLetter():
    global remainingWords
    global alphabetCount
    global alphabet
    global storedName
    global guessedLetters
    
    #Reset the occurances of letters in the remaining words
    alphabetCount = []
    for x in range(0, 26):
        alphabetCount.append(0)
    
    #for each word, check occurances of each letters
    for x in range(0, len(remainingWords)):
        for y in range(0, 26):
            if (alphabet[y] in remainingWords[x]):
                alphabetCount[y] += 1
                
    #find the letter with the most occurances
    highestValue = 0
    highestLetter = ""
    for x in range(0, 26):  
        if ((alphabetCount[x] > highestValue) and not(alphabet[x] in guessedLetters)):
            highestValue = alphabetCount[x]
            highestLetter = alphabet[x]
    
    guessedLetters += highestLetter
    if (len(remainingWords) <= 20):
        print(remainingWords)
    else:
        print(len(remainingWords))
    guess = input("Hmmm...does your word have the letter " + highestLetter + " (Y/N)? ")
    if (guess == "Y"):
        position = input("At what positions can the letter " + highestLetter + " be found (1st letter = 1) (Type STOP to stop)? ")
        while not(position == "STOP"):
            tempStoredName = ""
            for x in range (0, len(storedName)):
                if (x == int(position) - 1):
                    tempStoredName += highestLetter
                else:
                    tempStoredName += storedName[x]
            storedName = tempStoredName
            position = input("At what positions can the letter " + highestLetter + " be found (1st letter = 1) (Type STOP to stop)? ")
        removeWordsWithout(highestLetter, storedName)
    elif guess == "N":
        removeWordsWith(highestLetter)
#BODY
#Introduce the game and take the length of the word to create the storedWord
print("Hello there! My name is HangManBoy 1.0, and I would like to challenge you to a game of hangman! First, pick a word with a length between 1 and 26 letters!")
letterCount = input("Enter letter count here: ")
fileName = "finalDictLen" + str(letterCount) + "v2.txt"
fileIn = open(fileName, 'r')

#Go through the text file and strip away the escape characters
remainingWords = fileIn.readlines()
for x in range(0, len(remainingWords)):
    readWord = remainingWords[x]
    remainingWords[x] = readWord[:-1]
    
#Make stored name variable
for x in range(0, int(letterCount)):
    storedName += "-"
    
#Check to see how many words remain,
if len(remainingWords) == 0:
    print("One of us had to have made a mistake...")
elif len(remainingWords) == 1:
    guessedRight = input("Is your word " + remainingWords[0] + " (Y/N): ")
    if guessedRight == "Y":
        print("Thank you for playing!")
    elif guessedRight == "N":
        print("Aww man. Still, thank you for playing!")
else:
    guessLetter()