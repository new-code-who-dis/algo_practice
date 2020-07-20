
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
    #yes its better to do a dictionary, yes i should do that next, no its not needed rn okur
    grupos = []
    return age_groups(count, ordered_ages, grupos)

def age_groups(index, ordered_ages, groups):
    build_a_bear = [ordered_ages[index]]
    next = index + 1
    if next > (len(ordered_ages) - 1):
        #traaassssssssssshhhhhhhhhh
        groups.append(build_a_bear)
        return groups
    while ordered_ages[next] < (ordered_ages[index] + 3):
        build_a_bear.append(ordered_ages[next])
        next += 1

    groups.append(build_a_bear)
    return age_groups(next,ordered_ages,groups) #actually change order cause we should finish the loop on the last line cause #estillo

def smartSteal(limit, values):
    values_per_unit = {}
    for key,item in values.items():
        val_per_unit = item["value"]/item["weight"] # wow this should just be a class
        values_per_unit[key] = val_per_unit
    smallest = smallestOfDict(values_per_unit)
    the_bag = {}
    extra_space = limit
    while extra_space > (values[smallest]["weight"] - 1):
        biggest = biggestOfDict(values_per_unit)
        del values_per_unit[biggest]
        bigest_weight = values[biggest]["weight"]
        num_of_units = extra_space//bigest_weight # and i oop, just made it a baby's problem but whateva if I dont create crap what will i have to improve on?!
        wieght_of_units = num_of_units * values[biggest]["weight"]
        
        extra_space -= wieght_of_units
        the_bag[biggest] = num_of_units

    return the_bag

def biggestOfDict(values):
    biggest_value = 0
    biggest_key = None
    for key,item in values.items():
        if item > biggest_value:
            biggest_value = item
            biggest_key = key
    return biggest_key

def smallestOfDict(values): #fuck its the exact same thing kinda, is there a way to pass in an operation maybe?
    smallest_key = next(iter(values))
    smallest_value = values[smallest_key]
    
    for key,item in values.items():
        if item < smallest_value:
            smallest_value = item
            smallest_key = key
    return smallest_key



