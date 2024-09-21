def gcd(m,n): #euclids algorithm which takes more time to execute for larger numbers
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return (n)
    else :
        return(gcd(n,m%n))
    
#while version of euclids more efficient
    def gcd(m,n):
        if m<n:
            (m,n)=(n,m)
        while (m%n)!=0:
            (m,n)=(n,m%n)
        return(n)
    
