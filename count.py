#Program to find the command-line-arguments-to-count-word
#Developed by: S.Jeba Solomon Raj
#RegisterNumber: 23001618

import sys
f=open(sys.argv[1],'r')
x=f.read().split()
word=(len(x))
print("Number of words:",word)