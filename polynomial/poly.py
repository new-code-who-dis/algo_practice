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

#make it variable length though? or just do adds in main for 2 at a time instead of 4
def add_poly(p1,p2):
    length = make_same_length(p1,p2)
    result = [None]*length
    for i in range(length):
        result[i] = p1[i] + p2[i]
    return result

def sub_poly(p1,p2):
    #too fucking simliar to add like is it faster to pass in an operation or should i make all the values in one list negative?
    length = make_same_length(p1,p2)
    result = [None]*length
    for i in range(length):
        result[i] = p1[i] - p2[i]
    return result

def make_same_length(p1,p2):
    length = len(p1)
    length_compare = len(p2)
    if length > length_compare:
        p2.extend([0]*(length-length_compare))
    elif length_compare > length:
        p1.extend([0]*(length_compare-length))
        length = length_compare
    return length

def mult_karatsuba_style(p1, p2):
    p1_derivatives = calc_derivative_parts(p1)
    p2_derviatives = calc_derivative_parts(p2)

    # (d1*e1)x^4 + ( (d1+d0)(e1+e0) - (d1*e1) - (d0*e0) )x^2 + (d0*e0)
    all_ds_add = add_poly(p1_derivatives[1], p1_derivatives[0]) 
    all_es_add = add_poly(p2_derviatives[1], p2_derviatives[0])
    adds_mult = mult_poly(all_ds_add, all_es_add)

    d1e1_mult = mult_poly(p1_derivatives[1], p2_derviatives[1])
    
    d0e0_mult = mult_poly(p1_derivatives[0], p2_derviatives[0])
    mults_add = add_poly(d1e1_mult, d0e0_mult)
    inner_sub = sub_poly(adds_mult, mults_add)

    increase_power(4,d1e1_mult)#why though?
    increase_power(2,inner_sub)#same like why isn't it just 1 x?

    almost_over_this_shit = add_poly(d1e1_mult, d0e0_mult)
    very_done = add_poly(almost_over_this_shit, inner_sub)

    return very_done

def calc_derivative_parts(p):
    if len(p)%2 > 0:
        p.append(0)
    length = len(p)
    half = length//2
    d0 = calc_derivatives(p,0,half)
    d1 = calc_derivatives(p,half,length)
    parts = [d0,d1]
    return parts

def increase_power(indices, poly):
    for i in range(indices):
        poly.insert(0,0)

def even_out_list_length(input, difference):
    result = [0]*difference
    l = input.extend(result)
    return l

def calc_derivatives(poly, start, stop):
    #so dont i have to go through the cycle again if we arent at 1 being the higest power?
    n = len(poly)
    half = n//2
    #shitty mcshit on shit street
    if start == 0:
        disposition = half
    else:
        disposition = n

    derivatives = [None]*(half)
    for i in range(start,stop):
        power = calc_derivative_power(disposition,i,half)
        derivatives[power] = poly[i]
    return derivatives

def calc_derivative_power(disposition,index,half):
    displacement = disposition - index
    power = half - displacement
    if power < 0:
        return 0
    else:
        return power

#THOUGHTS
# Wowie no method overloading in python, feeling hurt to say the least
#







    
