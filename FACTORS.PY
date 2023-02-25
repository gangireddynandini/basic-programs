a=int(input("enter a number"))
print("factors of {} is".format(a))
if(a<=0):
    print("invalid")
else:
    for i in range(1,(a//2)+1) :
        if(a%i==0):
            print("{}".format(i))10

        #else:
            #print("{} not a factor".format(i))

