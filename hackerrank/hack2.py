# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
T = int(input())
for _ in range(T):
    try:
        print(bool(re.compile(input())))
    except:
        print("False")

#
# You are given a string .
# Your task is to find out whether  is a valid regex or not.
#
# Input Format
#
# The first line contains integer , the number of test cases.
# The next  lines contains the string .
#
# Constraints
#
#
# Output Format
#
# Print "True" or "False" for each test case without quotes
#
# Sample Input
#
# 2
# .*\+
# .*+
# Sample Output
#
# True
# False