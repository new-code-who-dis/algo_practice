
def arrange_dat_coin(x):
    # i think converting from int to str to int again is actually shitay
    # wanna play with only using int
    bigCoin = x
    if x < 11:
        digits = splitDigits(x)
        thinkPension(digits)
        
    return bigCoin

def splitDigits(x):
    digits = []
        while x > 0:
            last = x%10
            digits.append(last)
            x = (x - last)/10
    return digits

def thinkPension(x):
    # get number of digits like base like if len is 3 you want 100 to start with and then just multiple
    bigBank = len(x)

