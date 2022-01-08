# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:42:57 2022

@author: nilay
"""
for x in range(1, 27):
    words = []
    
    fileIn = open("finalDictLen" + str(x) + ".txt", "r")
    wordCount = len(fileIn.readlines())
    fileIn.close()
    
    fileOut = open("finalDictLen" + str(x) + "v2.txt", "w")
    
    fileIn = open("finalDictLen" + str(x) + ".txt", "r")
    for y in range(0, wordCount):
        line = fileIn.readline()
        line = line[:-1]
        line = line.lower()
        if not(line in words):
            words.append(line)
            fileOut.write(line + "\n")