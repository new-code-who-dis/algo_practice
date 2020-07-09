# naive function first
def calc_gcd(a,b):
    if a < b:
        a,b = b,a
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

# although i get that 3 variable method of swapping is like a staple in the house of code, 
# i dont know i wanna play with new syntax , i almost think the tuple way is easier for a pleb
# to understand and the argument here was fun to read so i wanna keep a piece with me
# https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python