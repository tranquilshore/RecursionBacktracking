import sys
sys.setrecursionlimit(4000)
n = int(raw_input())

def passwordCracker(password,keys,res):
    if len(password) == 0:
        return True

    if password in memo:
        return False

    for key in keys:
        if password[:len(key)] == key:
            res.append(key)
            memo[password] = True

            if passwordCracker(password[len(key):],keys,res):
                return True

            del res[-1]
    
    return False


for i in range(n):
    keys_len = int(raw_input())
    keys = raw_input().split()
    password = raw_input() 
    memo = {}
    res = []
    passwordCracker(password,keys,res)

    if len(res) > 0:
        print " ".join(res)
    else:
        print "WRONG PASSWORD"
