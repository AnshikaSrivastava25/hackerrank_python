"""_summary_
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
if 1<= n <=100:                  #constraint
 if n % 2 != 0:                  #If n is odd,
    print ('Weird')              #print weird
 elif n % 2 == 0:                #If n is even
     if 2 <= n <= 5 :            #and in the inclusive range of 2 to 5,
        print ('Not Weird')      #print Not Weird
     elif 6 <= n <= 20 :         #or in the inclusive range of 6 to 20,
        print('Weird')           #print Weird
     else:                       #If n is even and greater than 20,
         print ('Not Weird')                 
