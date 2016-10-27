#Text file --> line --> word --> unique + sorted

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
result = list()
for line in fh:
   word = line.rstrip()
   word = word.split()
   lst.append(word)
for lis in lst:
   for item in lis:
       result.append(item)
unique = list()
[unique.append(data) for data in result if data not in unique]
  
print sorted(unique)
