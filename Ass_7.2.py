# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
c=0
average=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    num = float((line[pos+1:]).strip())
    average+=num
    c+=1
    
    
print "Average spam confidence:", average/c
