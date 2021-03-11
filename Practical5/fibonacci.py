#Because of the first two integers are given, the range of i should be considered
#Under "for" command, the first two integers are not included. So it is important to print them in the beginning.
a=1
b=1
i=1
i+=1
print(a)
print(b)
for i in range(0,11):
    a,b=b,a+b
    print(b)
