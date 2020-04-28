"""Given a non negative integer A, print all the pairs of integers(a,b) such that
a and b are positive integers
a<=b and
a^2 + b^2 = A
0 <= A
A<=1000"""
A=input("Enter a non negative integer")
s=int(A)
if s<=1000 and s>=0:
    for b in range(s):
        for a in range(s):
            if a<=b:
                c=a*a+b*b
                if s==c:
                    print(a,",",b)
