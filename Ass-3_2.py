#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score=raw_input("Enter Score: ")

try:
    s=float(score)
except:
    s=-1
if(s>=.9):
 print "A"
if((s>=.8)and(s<.9)):
 print "B"
if(s>=.7)and(s<.8):
 print "C"
if(s>=.6)and(s<.7):
 print "D"
if(s<.6)and(s>.1):
 print "F"
elif(s==-1):
 print "Error"