def gcd(m,n):# naive approach 
    fm= []
    for i in range (1, m+1):
        if (m%i)==0:
            fm.append(i)
    fn=[]
    for j in range (1, n+1):
        if (n%i)==0:
            fm.append(j)

    cf =[]
    for f in fm:
        if f in fn:
            cf.append(f)

    return(cf[-1])

