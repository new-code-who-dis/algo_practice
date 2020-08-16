def mult_poly(p1, p2):
    results = [None]*(len(p1) + len(p2)-1)
    for idx, val in enumerate(p1):
        for idx2, valu2 in enumerate(p2):
            key = idx + idx2
            result = val*valu2
            if results[key] is not None:
                results[key] = results[key] + result 
            else:
                results[key] = result
    return results

def add_poly(p1,p2,p3,p4):
    result = [None]*len(p1)
    for i,val in p1:
        result[i] = p1[i] + p2[i] + p3[i] + p4[i]
    return result
#make it variable length though? or just do adds in main for 2 at a time instead of 4
def add_poly(p1,p2):
    result = [None]*len(p1)
    for i,val in p1:
        result[i] = p1[i] + p2[i]
    return result

def sub_poly(p1,p2):
    result = [None]*len(p1)
    for i,val in p1:
        result[i] = p1[i] - p2[i]
    return result
 
def mult_karatsuba_style(p1, p2):
    #deal with edge case where poly length is odd
    p1_half = len(p1)//2
    p1_d0 = calc_derivatives(p1,0,p1_half-1)
    p1_d1 = calc_derivatives(p1,p1_half,(len(p1)-1))

    p2_half = len(p2)//2
    p2_e0 = calc_derivatives(p2,0,p2_half-1)
    p2_e1 = calc_derivatives(p2,p2_half,(len(p2)-1))

    # (d1*e1)x^2 + ( (d1+d0)+(e1+e0) - (d1*e1) - (d0*e0) )x + (d0*e0)
    d1e1_mult = mult_poly(p1_d1, p2_e1)
    d0e0_mult = mult_poly(p1_d0, p2_e0)

    all_add = add_poly(p1_d1, p1_d0, p2_e0, p2_e1)
    mults_add = add_poly(d1e1_mult, d0e0_mult)
    #maybe instead of another function i could just make all the values in a list negative
    #  and reuse the add method
    inner_sub = sub_poly(all_add, mults_add)
    return d0e0_mult  

def calc_derivatives(poly, start, stop):
    #so dont i have to go through the cycle again if we arent at 1 being the higest power?
    n = len(poly)
    derivatives = [None]*(n//2)
    for i in range(start,stop):
        power = calc_derivative_power(n,i)
        derivatives[power] = poly[i]
    return derivatives

def calc_derivative_power(index,n):
    displacement = n - index
    power = n//2 - displacement
    if power < 0:
        return 0
    else:
        return power






    
