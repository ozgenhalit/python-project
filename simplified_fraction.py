def div():
    n,m= input("enter a fraction : ").split("/")
    n=int(n)
    m =int(m)
    n_divisor = set(i for i in range(1,n+1) if n%i == 0)
    m_divisor = set(i for i in range(1,m+1) if m%i == 0)
    conc = list(n_divisor.intersection(m_divisor))
    conc.sort()
    if  conc != list():
        return (str(n/conc[-1]).strip(".0") + "/" + str(m/conc[-1]).strip(".0"))
    elif m == 1 :
        print(n)
    else:
        return (str(n)+"/"+str(m))
div()
