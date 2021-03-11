# r is the average number of individuals infected by each individual with the virus
# When one person infects others, do not forget to this person is still sick
# What we should pay attention to is that "print" should be coded without blank space or it will run under the "for" command
n=84
r=1.2
i=1
i+=1
for i in range(1,6):
    n=n+n*r

print("when the r rate is",r,"the total number of individualsinfected after 5 generations is",n)
