#finding a number is big or small
a=input("enter a value:")
b=input("enter b value")
c=input("enter a value:")
big=a if (b<a>c) else b if (a<b>c) else c if a<c>b else "both values are equal"
small=a if (b>a<c) else b if (a>b<c) else c if (b<a>c) else "both values are equal"
print("big value of {},{},{} is ={}".format(a,b,c,big))
print("small value of {},{},{} is={}".format(a,b,c,small))

