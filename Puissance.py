def puissance_recurssive (x,n):
    if n==0:
        return 1
    else:
        return x*puissance_recurssive(x,n-1)
#/////////////////////////////////////////////////
def puissance2 (x,n):
    p=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            p=p*x
    return p

#/////////////////////////////////////////////////
def puissance3(x,n):
    p = 1
    while n>0:
        if n%2==1:
            p *= x
        x *= x
        n //= 2
    return p

def puissancek(x,n,p=1):
    if n == 0:
        return p
    elif n % 2 == 0:
        return puissancek(x*x ,n//2 , p)
    else:
        return puissancek(x*x,n//2,p*x)

if __name__ =="__main__":
    print(puissancek(2,3))
