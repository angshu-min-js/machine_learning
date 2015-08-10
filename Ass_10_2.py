#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
lines=text.split("\n");
counts = dict()
lst = list()

for word in lines:
   if word.startswith('From ') and not word.startswith('From:'):
        str = word.find(':')
        hour = word[str-2:str]
        counts[hour] = counts.get(hour,0) + 1
        
x=[]        
    
for key, val in counts.items():
    lst.append((key,val))
lst.sort()
for val,key in lst:
   if val not in x:
       print val,key
       x.append(val)
