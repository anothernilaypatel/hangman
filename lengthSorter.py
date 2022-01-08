# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 19:50:46 2022

@author: nilay
"""
fileIn = open('finalDict.txt','r')
fileOutlen1 = open('finalDictLen1.txt', 'w')
fileOutlen2 = open('finalDictLen2.txt', 'w')
fileOutlen3 = open('finalDictLen3.txt', 'w')
fileOutlen4 = open('finalDictLen4.txt', 'w')
fileOutlen5 = open('finalDictLen5.txt', 'w')
fileOutlen6 = open('finalDictLen6.txt', 'w')
fileOutlen7 = open('finalDictLen7.txt', 'w')
fileOutlen8 = open('finalDictLen8.txt', 'w')
fileOutlen9 = open('finalDictLen9.txt', 'w')
fileOutlen10 = open('finalDictLen10.txt', 'w')
fileOutlen11 = open('finalDictLen11.txt', 'w')
fileOutlen12 = open('finalDictLen12.txt', 'w')
fileOutlen13 = open('finalDictLen13.txt', 'w')
fileOutlen14 = open('finalDictLen14.txt', 'w')
fileOutlen15 = open('finalDictLen15.txt', 'w')
fileOutlen16 = open('finalDictLen16.txt', 'w')
fileOutlen24 = open('finalDictLen24.txt', 'w')
fileOutlen25 = open('finalDictLen25.txt', 'w')
fileOutlen26 = open('finalDictLen26.txt', 'w')
fileOutlen27 = open('finalDictLen27.txt', 'w')
fileOutlen28 = open('finalDictLen28.txt', 'w')
fileOutlen17 = open('finalDictLen17.txt', 'w')
fileOutlen18 = open('finalDictLen18.txt', 'w')
fileOutlen19 = open('finalDictLen19.txt', 'w')
fileOutlen20 = open('finalDictLen20.txt', 'w')
fileOutlen21 = open('finalDictLen21.txt', 'w')
fileOutlen22 = open('finalDictLen22.txt', 'w')
fileOutlen23 = open('finalDictLen23.txt', 'w')
fileOutlen29 = open('finalDictLen29.txt', 'w')
fileOutlen30 = open('finalDictLen30.txt', 'w')

for x in range(0, 526945):
    word = fileIn.readline()
    word = word[:-1]
    
    wordLength = int(len(word))
    if wordLength == 1:
        fileOutlen1.write(word + "\n")
    if wordLength == 2:
        fileOutlen2.write(word + "\n")
    if wordLength == 3:
        fileOutlen3.write(word + "\n")
    if wordLength == 4:
        fileOutlen4.write(word + "\n")
    if wordLength == 5:
        fileOutlen5.write(word + "\n")
    if wordLength == 6:
        fileOutlen6.write(word + "\n")
    if wordLength == 7:
        fileOutlen7.write(word + "\n")
    if wordLength == 8:
        fileOutlen8.write(word + "\n")
    if wordLength == 9:
        fileOutlen9.write(word + "\n")
    if wordLength == 10:
        fileOutlen10.write(word + "\n")
    if wordLength == 11:
        fileOutlen11.write(word + "\n")
    if wordLength == 12:
        fileOutlen12.write(word + "\n")
    if wordLength == 13:
        fileOutlen13.write(word + "\n")
    if wordLength == 14:
        fileOutlen14.write(word + "\n")
    if wordLength == 15:
        fileOutlen15.write(word + "\n")
    if wordLength == 16:
        fileOutlen16.write(word + "\n")
    if wordLength == 17:
        fileOutlen17.write(word + "\n")
    if wordLength == 18:
        fileOutlen18.write(word + "\n")
    if wordLength == 19:
        fileOutlen19.write(word + "\n")
    if wordLength == 20:
        fileOutlen20.write(word + "\n")
    if wordLength == 21:
        fileOutlen21.write(word + "\n")
    if wordLength == 22:
        fileOutlen22.write(word + "\n")
    if wordLength == 23:
        fileOutlen23.write(word + "\n")
    if wordLength == 24:
        fileOutlen24.write(word + "\n")
    if wordLength == 25:
        fileOutlen25.write(word + "\n")
    if wordLength == 26:
        fileOutlen26.write(word + "\n")
    if wordLength == 27:
        fileOutlen27.write(word + "\n")
    if wordLength == 28:
        fileOutlen28.write(word + "\n")
    if wordLength == 29:
        fileOutlen29.write(word + "\n")
    if wordLength == 30:
        fileOutlen30.write(word + "\n")

fileIn.close() 
#fileOut.close()