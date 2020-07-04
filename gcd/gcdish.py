# naive function first
def calc_gcd(a,b):
    return gcd_basique(a,b)

def gcd_basique(a,b):
    #edge case - a = b
    d = a if a > b else b
    gcd = 0
    while gcd == 0:
        if ((a % d == 0) and (b % d == 0)): gcd = d
        # difference between and/&/&& in python?
        d -= 1
    return gcd

