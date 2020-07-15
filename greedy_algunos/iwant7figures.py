
def arrange_dat_coin(x):
    # i think converting from int to str to int again is actually shitay
    # wanna play with only using int
    bigCoin = x
    if x > 11:
        digits = splitDigits(x)
        return thinkPension(digits)
        
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
    salary = 0
    cx = x
    for idx, val in enumerate(x):
        biggest = val
        biggestidx = idx
        for cidx, cval in enumerate(cx):
            if biggest < cval:
                biggestidx = cidx
        biggest = x[biggestidx]
        cx[biggestidx] = 0
        x[biggestidx] = 0
        salary += biggest * pow(10, (len(x)-idx-1))
    return salary

def thinkBroke(x):
    salary = 0
    cx = x
    broke = [None]*len(x)
    for idx, val in enumerate(x):
        biggest = val
        biggestidx = idx
        for cidx, cval in enumerate(cx):
            if biggest < cval:
                biggestidx = cidx
        biggest = x[biggestidx]
        cx[biggestidx] = 0
        x[biggestidx] = 0
        broke[len(x) - idx -1] = biggest 
    return broke






