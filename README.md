## Python
### Class

```
def gcd(m, n):  #Define global function gcd
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

class Fraction:

    def __init__(self, num, den): #contructor
        self.num = num #self = this
        self.den = den

    def __str__(self): #Object to String conversion, __str__ built in function
        return str(self.num) + "/" + str(self.den)

    def __add__(self, x): #Add
        new_num = self.num*x.den + self.den*x.num
        new_den = self.den * x.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common,  new_den // common)

		my_f = Fraction(3, 5)
print my_f
print my_f + Fraction(8, 5)
```

################################################################################

### Algorithm Analysis

```
import time

def sum_of_n1(n):
    start = time.time()
    sum = 0
    for i  in range(0, n):
        sum = sum + i
    end = time.time()
    return sum, end-start
print "Iterative:", sum_of_n1(5000000)

def sum_of_n2(n):
    start = time.time()
    sum = (n*(n+1))/2
    end = time.time()
    return sum, end-start
print "Algorithm (Summation Eqn):", sum_of_n2(5000000)

#Iterative: (12499997500000L, 0.9650001525878906)
#Algorithm: (Summation Eqn) (12500002500000L, 0.0)
#Iterative solutions takes more time and less accurate
```
#### Big-O Notation
##### The order of magnitude function describes the part of T(n) that increases the
##### fastest as the value of n increases. Order of magnitude is often called Big-O
##### notation (for "order") and written as O(F(n)).  It provides a useful
##### approximation to the actual number of steps in the computation.

```
a = 5
b = 6
c = 10 # 3 assignment
for i in range(n):
    for j in range(n): # n^2 iteration
        x = i * i
        y = j * j
        z = i * j # 3 assignment
for k in range(n): # n
    w = a * k + 45
    v = b * b # 2
d = 33 # 1

# So, T(n) = 3 + 3n^2 + 2n + 1 =  4 + 3n^2 + 2n : O(n^2) --> Big-O, Quadratic (n^2)
```
##### List: append: O(1), concatenation: O(k)

```
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print ("append ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

# ('concat ', 6.391950280176704, 'milliseconds')
# ('append ', 0.1982510243736293, 'milliseconds')
# ('comprehension ', 0.09311756341678024, 'milliseconds')
# ('list range ', 0.03239667522277667, 'milliseconds')
```

```
import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange (%d) in x"%i,
    "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" %(i, lst_time, d_time))


10000,      0.139,      0.002
30000,      0.401,      0.002
50000,      0.742,      0.002
70000,      1.144,      0.002
90000,      1.426,      0.002
110000,      1.816,      0.002
130000,      2.106,      0.002
150000,      2.425,      0.002
170000,      2.815,      0.002
190000,      3.268,      0.002
210000,      3.989,      0.002
230000,      3.714,      0.002
250000,      4.359,      0.002
270000,      4.543,      0.002
290000,      4.642,      0.003
310000,      5.016,      0.002
330000,      5.465,      0.003
350000,      5.577,      0.003
370000,      5.818,      0.002
```
### List is O(n) and Dictionary is O(1)



### Data Structures

#### Stack: Addition & removal at top. LIFO
#### Queue: Addition & removal different ends. FIFO.
#### Dequeue: Double-ended queue. Hybrid. Both end-start
#### Linked List: The basic building block for the linked list implementation is the node.
#### Unordered List: Collection of nodes

```
import turtle

my_turtle = turtle.Turtle()
my_wind = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turle.right(90)
        draw_spiral(my_turle, line_len = 5)

draw_spiral(my_turtle, 100)
my_win.exitonlclick()
```
---------------------------------------------------------------------------------------------------------------
############## PS: I was usually using a VM and didn't push the code most of the time so I made a git rebase script :D for this repo