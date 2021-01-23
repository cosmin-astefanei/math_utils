def isprime(n):

    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n>3:
        k=0
        for i in range(2,int(n**(1/2))+1):
            if n%i==0:
                k+=1
        if k==0:
            return True
        else:
            return False
