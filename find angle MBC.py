"""
 is a right triangle,  at .
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°
"""
import math

# taking the input from user
ab = float(input())
bc = float(input())

# finding the distance 
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm

# equalizing the sides 
b = mc
c = bm
a = bc

# where b=c
# finding the angle in radian
angel_b_radian = math.acos(a / (2*b))

# converting the radian to degree
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

# printing with degree
print(angel_b_degree,'\u00B0',sep='')
