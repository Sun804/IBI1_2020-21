#because of the first two integers are given, the range of i should be considered
a=1
b=1
i=1
i+=1
print(a)
print(b)
for i in range(0,11):
    a,b=b,a+b
    print(b)
