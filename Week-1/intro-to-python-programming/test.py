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