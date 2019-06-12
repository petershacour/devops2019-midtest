#!/usr/bin/python3

import sys
import os


if len(sys.argv) !=2:
    print("Bad usage: need one argument")
    sys.exit(1)

elif type(sys.argv[1]) !=str:
    print("Your input is not a string")
    sys.exit(1)

else:

    char_occur={}  #define empty dict
    st = sys.argv[1] 
    for c in st:  #for each char in the string, add it to the dict with the value of it's first index
        char_occur[c] = st.index(c)
    print(char_occur)
