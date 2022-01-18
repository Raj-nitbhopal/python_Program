var = 100
if var > 90:
   print("1. True expression executed")
else:
   print("1. False expression executed")

var = 90
if var > 90:
   print("2. True expression executed")
else:
   print("2. False expression executed")
# Above code also written in one Line as
var = 100
print("3. True expression executed") if var > 90 else print("3. False expression executed")

p = 90
q = 20
if p > q:
   print("4. True expression executed")
elif q == p:
   print("4. False expression executed")
else:
   print("Nothing")

p = 2000
q = 3330
r = 600
if p > r and q > r:
   print("Both conditions are True")
else:
   print("Nothing")

p = 2000
q = 30
r = 600
if p > r or q > r:
   print("Any one expression is true")
else:
   print("Nothing")


p = 2000
q = 30
r = 600
s = 60
t = 60
if (p > r or q > r) and  (s == t):
   print("True is this")
else:
   print("Nothing")

p = 2000
q = 30
r = 600
if (p > r or q > r):
   pass
else:
   print("Nothing")
