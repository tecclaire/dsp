# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequences of values/elements. The most important difference is tuples are immutable, and tuples are used as keys in dictionaries, since only immutable elements can be used as keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set behaves like a collection of dictionary keys with no values. Lists are ordered collections of elements while sets are unordered collections of unique elements. Ex. [1,2,2,3] vs. set {[1,2,2,3]} is just set {1,2,3}.

Sets are faster for finding an element since its values are hashable. When lists have to go sequentially to find out if the value exists. Sets have a hash function that directly jumps and locates the bucket.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> While normal functions are defined using the def keyword, anonymous functions are defined using the lambda keyword. Lambda is userful to define functions inline, so it's good to be used as arguments for a higher-order function. 
Ex.Use lambda to sort a list of tuples by the second value each element has.
tuples = [(1,2,3),(3,1,5),(2,0,7)]
sorted(tuples, key=lambda tup: tup[1])
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool for transforming one list (any iterable actually) into another list. During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed. List comprehensions can be written as for loops but are usually faster than the equivalent for loops.

Ex. Equivalents with 'map':
squares = map(lambda x: x**2, range(10))
while in list comprehension:
squares = [x**2 for x in range(10)]

Equivalents with 'filter':
filsquares = filter(lambda x: x > 5 and x < 50, squares)
while in list comprehension:
filsquares = [x**2 for x in range(10) if x**2 > 5 and x**2 < 50 ]


---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





