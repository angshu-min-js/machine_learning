count=0
total=0
while True:
 inp =raw_input('Enter a number: ')
 if(inp=='done'): break
 try:
  num=float(inp)
 except:
  print 'Invalid Input'
  continue
 count=count+1
 total+=num
 print num
 
print 'Done', count, total, 'Average: ', total/count