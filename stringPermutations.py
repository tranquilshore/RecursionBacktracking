'''
taking care of duplicates as well as lexicographic order
Time complexity:  O(n*n!)
'''
import itertools

def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l

ans = perm1(list("aabc"))
ans.sort()

print len(list(ans for ans,_ in itertools.groupby(ans)))

