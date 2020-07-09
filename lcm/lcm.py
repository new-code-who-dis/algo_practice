import gcd

def calc_lcm(a,b):
    x = a*b
    return x/gcd.gcdish.gcd_euclidian(a,b)

def calc_lcd(a,b):
    return calc_lcd_func(a,b,1)

def calc_lcd_func(a,b,x):
    # will refactor gcd method after, just want to get the logic down first
    #but maybe its better to have this repeated code cause otherwise it would be calculating x for no reason if it was using gcd
    if b == 0: 
        return x
    else:
        r = a%b
        x = a/b - r
        return calc_lcd_func(b,r,x)

    

