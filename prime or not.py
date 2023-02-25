n=int(input("enter a number:"))
if(n<2):
    print("invalid")
else:
    dec="prime"
    for i in range(2,n):
        if(n%i==0):
            dec="notprime"
            break
    if(dec=="prime"):
        print("{} is a prime".format(n))
    else:
        print("{} is a  not prime".format(n))
print("thnx")