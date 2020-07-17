
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

def ageDiscrimination(x):
    #ordered_ages = thinkBroke(x)
    ordered_ages = x
    count = 0 
    # i think i remember the guys at og work saying populating an object just via a reference is shady
    # but there's no need for this dictionary to exist outside of this function, its not applicable
    #yes its better to do a dictionary, yes i should do that next, no its not needed rn okur
    return age_groups(count, ordered_ages, grupos)


grupos = []
def age_groups(index, ordered_ages, groups):
    build_a_bear = [ordered_ages[index]]
    next = index + 1
    while (next < len(ordered_ages)) \
            & (ordered_ages[next] < (ordered_ages[index] + 3)):
        build_a_bear.append(ordered_ages[next])
        next += 1
    #weird after the first evaluation fails it goes straight to the return, i think this is something about self calling 
    #functions im not getting
    groups.append(build_a_bear)
    
    if next > (len(ordered_ages) - 1):
        return groups
    else:
        return age_groups(next,ordered_ages,groups) #actually change order cause we should finish the loop on the last line cause #estillo





