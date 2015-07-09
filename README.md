# Python_Beginning
Basics

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

dir("String") ---- Gives the in-build function list for string

fruit = 'banana'

'n' in fruit

>>True

#List: A linear collection of values that stay in order
#Dictionary: A “bag” of values, each with its own label

Dictionaries have different names in different languages
> Associative Arrays - Perl / PHP
> Properties or Map or HashMap - Java
> Property Bag - C# / .Net


dictionary = { 'chuck' : 1 , 'fred' : 42','jan': 100}
for aaa,bbb in dictionary.items() :
print aaa, bbb

jan 100
chuck 1
fred 42

counts[word] = counts.get(word,0) + 1
