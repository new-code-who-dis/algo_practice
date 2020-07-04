fibbers = []
fibbers.append(0)
fibbers.append(1)

def calcFib(n):
    if n > 1:
        for x in range(2,n+1):
            fibbers.append(fibbers[x-1] + fibbers[x-2]) 
    return fibbers[n]

def calcIndex(f):
    for x in range (100):
        currentFib = calcTheFib(x)
        if f == currentFib:
            return x
        elif f < currentFib:
            return 1234 #"First closest index was " + str(x)

# THOUGHTS:
#function accessing in python, not same as c# clearly brush up on c# though, i miss it
    # there's probably a way to estimate what the value is relative to the index but i don't know how
    # nested for loop come on there has to be another way
    # i dont like returning twice to be honest and that range 100 come on
        # though i swear i was warned against it Im really seeing a while loop working here this will be the next commit fo sho
    # how do i return something thats like not an integer type, how does type casting working in python
    # also time this shit, make it speedy
