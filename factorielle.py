def factorielle (n):
    if n == 0:
        return 1
    else:
        return n*factorielle (n-1)
# ///////////////////////////////////////////
def factorielle1(n):
    p=1
    if n==0:
        return 1
    for i in range(1,n+1):
        p=p*i
    return p
# ////////////////////////////////////////
if __name__ =="__main__":
    a = factorielle1 (5)
    print (a)