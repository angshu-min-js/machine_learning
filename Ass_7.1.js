# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for words in fh:
    print (words.rstrip()).upper()
