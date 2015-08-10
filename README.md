# Python_Beginning

*References: (https://drive.google.com/drive/folders/0B7X1ycQalUnyal9yeUx3VW81VDg)*
#####Basics
```
for i in [5, 4, 3, 2, 1] :
print i
print 'Blastoff!'

Output:
5
4
3
2
1
Blastoff!
```
```
Use of None: variable = None
if variable is None :
variable = value

for letter in 'banana:
 print letter

s = 'Monty Python'
print s[0:4]

>>Mont

print s[6:7]
>>P

print s[6:20]
>>Python

dir("String") // Gives the in-build function list for string

fruit = 'banana'

'n' in fruit

>>True
```
####List: A linear collection of values that stay in order
####Dictionary: A “bag” of values, each with its own label

**Dictionaries have different names in different languages:**
*Associative Arrays - Perl / PHP
*Properties or Map or HashMap - Java
*Property Bag - C# / .Net

```
dictionary = { 'chuck' : 1 , 'fred' : 42','jan': 100}
for aaa,bbb in dictionary.items() :
print aaa, bbb

jan 100
chuck 1
fred 42

counts[word] = counts.get(word,0) + 1
```

####Tuple: They are non changeable list

#######Difference between list and tuple:
```
*Tuples are immutable just like strings. 
*There is also a semantic distinction that should guide their usage. 
*Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. 
*Tuples have structure, lists have order.
*Tuples: count & index
*Tuples are more efficient, used when the list isn't changing and temporary
```

```
>>> (x, y) = (4, 'fred') //tuple has '( )'
>>> print y
fred
>>> (a, b) = (99, 98) //a, b = (99, 98) can be used without the parenthesis
>>> print a
99
```
*The items() method in dictionaries returns a list of (key, value) tuples
```
for (k,v) in d.items(): 
print k, v
```


