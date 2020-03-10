import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #s is string of Us and Ds
    count = 0
    valley = 0
    #loop through n
    for step in range(n):
        #if U, increase count
        if (s[step]=='U'):
            count+=1
            #if count on increase reaches zero, increment valley
            if(count==0):
                valley+=1
        else:
            #decrement count
            count-=1
    return valley


 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
