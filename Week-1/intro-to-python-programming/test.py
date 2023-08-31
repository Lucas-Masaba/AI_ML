def test(a, b):
  if(a > b):
    return "{} {}".format("oh", "yeah")
  else:
    return "{} {}".format("oh", "no")

print(test(1,2))

print(type(test))

# tuples
x = (1, 2, 3)

(a, b, c) = x

print(c)

