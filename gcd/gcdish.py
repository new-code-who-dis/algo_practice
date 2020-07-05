# naive function first
def calc_gcd(a,b):
    if a < b:
        x = a
        a = b
        b = x
    return gcd_euclidian(a,b)

def gcd_euclidian(a,b):
    if b == 0: 
        return a
    else:
        r = a%b
        return gcd_euclidian(b,r)
    # whats the op on multiple return statements in a function/ self calling?
    # doesn't seem very straight forward to me, also does it increase cyclomatic complexity?



def gcd_basique(a,b):
    #edge case - a = b
    d = a if a > b else b
    gcd = 0
    while gcd == 0:
        if ((a % d == 0) and (b % d == 0)): gcd = d
        # difference between and/&/&& in python?
        d -= 1
    return gcd

