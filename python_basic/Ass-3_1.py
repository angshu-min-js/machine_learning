#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter rate per hour: ")
r=float(rate)
gp=1.0
if h<=40.0:
 gp=h*r
elif (h>40.0):
 gp=((1.5*(h-40.0)*r)+(40.0*r))
print gp