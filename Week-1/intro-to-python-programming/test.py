import numpy as np

q = np.array([1, 2, 3])
print(q)

def test(a, b):
  if(a > b):
    return "{} {}".format("oh", "yeah")
  else:
    return "{} {}".format("oh", "no")

print(test(1,2))

print(type(test))

# tuples
tup = (1, 2, 3)

(a, b, c) = tup

print(c)

# lists
li = [1, 2, 3]
li.append(4)

li_two = [5, 6, 7]
li_combo = li + li_two

print(li_combo)

print([2, 4, 8] * 3)

print(2 in [2, 4, 8])

# string

str = 'This is a string'

print(str[4:])

print(str.split(' '))


# dictionaries
dict =  {
  'bill': 'bill@gmail.com',
  'joe': 'joe@gmail.com',
  'sally': 'sally@gmail.com'
}

for name, email in dict.items():
  print(name, email)

# sets
# A set contains unique elements of which the order is not important
s = set()
s.add(1)
s.add(2)
s.remove(1)
s.add(2)
print(s)

# list comprehension
lc = [num for num in range(1, 6) if num % 2 == 0]
print(lc)

# lambda
lam = lambda x: x * 2
print(lam(2))

# map
numbers =  [0, -1, 2, 3, -4]

def square_func(n):
    return n*n
 
new_numbers = list(map(square_func, numbers))
print( new_numbers)