a=260602
b=190784
c=100321
d=c-a
e=b-a
if d<e:
    print("d<e")
elif d>e:
    print("d>e")
else:
    print("d==e")
x=True
y=False
z=(x and not y)or(y and not x)
print(z)
w=(x!=y)
print(w)
