a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example
if a > b: print("a is greater than b")

#Example
a = 2
b = 330
print("A") if a > b else print("B")

#Example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#AND Keyword
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
