"""
Created on Sat Jan  1 18:16:09 2022

@author: nilay
"""
fileIn = open('test.txt','r')
fileOut = open('finalDict.txt', 'w')

for x in range(0, 675846):
    word = fileIn.readline()
    word = word[:-1]
    
    hasApostrophe = False
    for y in range(0, int(len(word))):
        if word[y] == "'":
            hasApostrophe = True
            break
    
    if hasApostrophe == False:
        fileOut.write(word + "\n")
    
fileIn.close() 
fileOut.close()