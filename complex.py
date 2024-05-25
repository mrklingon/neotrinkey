def absC(cmp):
    rl = cmp[0]
    im = cmp[1]
    
    val = (rl**2 + im**2)**.5
    
    return(val)

def plsC(cmp1,cmp2):
    r1 = cmp1[0]
    r2 = cmp2[0]
    l1 = cmp1[1]
    l2 = cmp2[1]

    return ([r1+r2,l1+l2])

def sqrC(cmp):
    rl = cmp[0]
    im = cmp[1]

    rl1 = -1 * im**2
    im1= 2 * (rl *im)
    rl2 = rl **2
    return ([(rl1 + rl2),im1])

def mltC(cmp,n):
    cmp[0]=cmp[0]*n
    cmp[1]=cmp[1]*n
    return cmp

def mltCC(cmp1,cmp2):
    A = cmp1[0]
    C = cmp2[0]
    B = cmp1[1]
    D = cmp2[1]
    
    T = (A*C) - (B*D)
    U = (A*D) + (B*C)
    return ([T,U])

def mltI(cmp):
    return ([-cmp[1],cmp[0]])
