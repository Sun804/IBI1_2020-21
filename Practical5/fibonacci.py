#because of the first two integers are given, the range of i should be considered
a=1
b=1
i=1
i+=1
for i in range(1,12):
    a,b=b,a+b
    print(b)
