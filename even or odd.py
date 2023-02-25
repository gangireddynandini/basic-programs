f=int(input("enter a digit:"))
a=range(0,100)
d=a[0::2]
if (f in d):
    print("given number is even")
else:
    print("given number is odd")
print("program is cmpltd")