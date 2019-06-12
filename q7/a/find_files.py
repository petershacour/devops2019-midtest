#!/usr/bin/python3

import os
import sys


if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <directory> <word>")
    sys.exit(1)


elif not os.path.isdir(sys.argv[1]):
    print(str(sys.argv[1]) + " Is not a directory, please try again")
    sys.exit(1)



else:

    direct = sys.argv[1]
    word = sys.argv[2]

    for root, dirs, files in os.walk(direct):
        counter = 0
        for name in files:
            found = 0
           # print(name)
            file = open(os.path.join(root, name),"r")  #open the file to read
            for line in file:      #check if the word exists in any of the lines in file
                words = line.split()   #split the line to words
                if word in words:
                    found = 1      #if the word found in the line
                    counter += 1
                    print(os.path.join(root, name))	#print the file name
                break
            
            file.close()
    if counter == 0:
        print("the word: " + word + " was not found the this directory")
    



