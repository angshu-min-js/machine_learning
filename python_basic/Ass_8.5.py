fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
word=list()
for line in fh:
    if not line.startswith("From "): continue
    word=line.rstrip()
    count=count+1
    word=word.split()
    print word[1]

print "There were", count, "lines in the file with From as the first word"
