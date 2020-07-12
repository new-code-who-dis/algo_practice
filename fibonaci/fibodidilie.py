fibbers = []
fibbers.append(0)
fibbers.append(1)

pissanoOfMod10 = 60

def calcFib(n):
    if n > 1:
        for x in range(2,n+1):
            if len(fibbers) < (x + 1):
                fibbers.append(fibbers[x-1] + fibbers[x-2]) 
    return fibbers[n]

def calcIndex(f):
    index = None
    counter = 0
    while index is None:
        currentFib = calcFib(counter)
        if f == currentFib:
            index = counter
        elif f < currentFib:
            index = "Next closest index is " + str(counter) + " which yields " + str(fibbers[counter])
        counter += 1
    return index

def calcLastDigitOfSum(index1, index2):
    sum = calcFib(index2)
    for x in range(index1,index2):
        sum += fibbers[x]
    return sum%10

def mod10 (x):
    return x%10

def calcPissanoMod10():
    pissanoMod10 = []
    for x in range(0,pissanoOfMod10):
        fibNumber = calcFib(x)
        pissanoMod10Number = mod10(fibNumber)
        pissanoMod10.append(pissanoMod10Number)
        #pissanoMod10.append(mod10(calcFib(x)))
    return pissanoMod10

def calcLastDigitOfSumPissano(index1, index2):
    sum = 0
    pissano = calcPissanoMod10()
    for x in range (index1,index2+1):
        sum += pissano[x%pissanoOfMod10]
    return mod10(sum)
    




# THOUGHTS:
#function accessing in python, not same as c# clearly brush up on c# though, i miss it
    # there's probably a way to estimate what the value is relative to the index but i don't know how
    # nested for loop come on there has to be another way
    # also time this shit, make it speedy
    # tbh its shitty to change the return type on the fly cause anything else would expect an int so split it out into another function
