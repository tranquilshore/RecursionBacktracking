def sum_(n):
    if n == 1:
        return n
    else:
        return n+sum_(n-1)
print sum_(5)

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
print fact(5)

def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)

print mult(19,19) 

#gcd of two numbers also divides their difference
def gcd(a,b):
    if a == 0 or b == 0:
        return False
    if a == b:
        return a
    if a > b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

print gcd(6,4)

#to reverse a sentance
def reverse(s,i):
    if i == 0:
        return s[i]
    else:
        return s[i]+" "+reverse(s,i-1)
    
word = "hi how are you good morning"
s = word.split()
print reverse(s,len(s)-1)

#decimal to binary
def dtob(n):
    if n == 0:
        return ""
    else:
        return dtob(int(n/2)) + str(n%2)
print dtob(19)






