'''
Problem: all possible ways to express X as a sum of distinct Nth powers

Analysis:

must be careful not to double count equivalent expressions for eg. 10^2 + 9^2 same as 9^2 + 10^2
to ensure that the list of numbers we're generating is always in sorted order, i.e., increasing.

eg. X= 29, N=2
Try 1 first. Our expression currently looks like 1^2 = 1. The next number must be >= 2.
    Try 2. Now it looks like 1^2 + 2^2 = 5. The next number must be >=3.
        Try 3. Now, we have 1^2 + 2^2 + 3^2 = 14.
            Try 4. We have 1^2 + 2^2 + 3^2 + 4^2 = 30. Backtrack, since it exceeds 29.
        Try 4. We have 1^2 + 2^2 + 4^2 = 21.
            Try 5. We have 1^2 + 2^2 + 4^2 + 5^2 = 46. Backtrack.
        Try 5. We have 1^2 + 2^2 + 5^2 = 30. Backtrack.
    Try 3. We have 1^2 + 3^2 = 10.
        ..........like this will go on untill the last backtrack where the enumeration ends.

couple of things to notice:

1. Each term has to be strictly greater than the previous term, so we always start checking from the previous number plus one.
 (At the very beginning, we start at 1.)
2. We backtrack if the sum of the current expression exceeds X, since adding more terms will just increase the sum even further.
3. We only go deeper if the current sum so far is strictly smaller than X.
4. On the (rare) occasion that we get a sum of exactly X, it means we've found a solution!
 This also means that we should backtrack (since adding more terms will just increase the sum).

'''
#code
def power_expressions(x,n,vals):
    s = sum(v**n for v in vals)
    if s == x:
        return 1
    else:
        answer = 0
        #to compute smallest possible next value
        v = vals[-1] + 1 if vals else 1
        while s+v**n <= x:
            #go deeper
            answer += power_expressions(x,n,vals+[v])
            #increment to get the next v
            v += 1
        return answer

print power_expressions(29,2,[])
        