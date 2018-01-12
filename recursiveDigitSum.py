in_list = raw_input().split()
n = in_list[0]
k = int(in_list[1])

'''
quick and better solution by using following lemma:

The Digit Sum of a Number to Base 10 is Equivalent
to Its Remainder Upon Division by 9
'''
x = (int(n)*int(k))%9 
print x if x else 9
'''
s = ""
for i in range(k):
    s += n

def super_digit(s):
    if len(s) == 1:
        return s
    else:
        ts = 0
        for i in s:
            ts += int(i)
        return super_digit(str(ts))

print super_digit(s)
'''
