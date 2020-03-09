#To run the script: "python permutation.py"

#The script is written in Python 2.7

#Suppose we have a set S={1,2,3,...,n}. This set has n! permutations
#For example suppose we have the set S={1,2,3}, which has the following
#3! permutations: (123,132,213,231,321,312). We want to find a number
#which contains all the permutations. In our example, one such number
#is 123 132 213 231 312 321 with 18 digits. One other such number is
#12321 13231 21312 with 15 digits(contains all the permutations but
#has less digits). Another one is 123121321 with 9 digits.

#This program takes input from user and gives a number which contains
#all the possible permutations but has minimum digits as well.

#Take input from the user
n = input("Please, give an integer number:")
print "Given number:", n

#Find all the permutations of the given number
from itertools import permutations
l = list(permutations(range(1, n+1)))

#Create the final number
final=0
for i in range(n):
    final=int(str(final)+str(l[0][i]))


#Remove this element from the list
l.pop(0)

while len(l)>1: #until all the numbers are represented to the final
    #Take the last n-1 digits
    check=abs((final) % (10**(n-1)))
    s=str(check)


    pos=-1 #position of list where the number was found
    num=n-1 #how many digits are the same
    found=(0,0,0) #the tuple that was found
    flag=0 #0 not found, 1 was found
    while flag==0 and len(s)>=2:

        for j in range(len(l)): #for every element of the list
            i=0
            while i<len(s) and int(s[i]) == l[j][i]: #for every element of the tuple
                i=i+1
                if i==len(s):
                    flag=1
                    found=l[j]
                    pos=j


            if flag==1: break;

        #next subgroup
        length_check=len(str(check))
        check=abs((final) % (10**(length_check-1)))
        s=str(check)
        num=num-1


    if flag==1:
        for i in range(num+1,n):
            final=int(str(final)+str(found[i]))

        l.pop(pos)
    else:
        for i in range(n):
            final=int(str(final)+str(l[0][i]))
        l.pop(0)

print "Final number:", final
num_of_digits=len(str(final))
print "Number of digits", num_of_digits
