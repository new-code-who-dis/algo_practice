def mult_poly(p1, p2):
    results = [None]*(len(p1) + len(p2)-1)
    for idx, val in enumerate(p1):
        for idx2, valu2 in enumerate(p2):
            key = idx + idx2
            result = val*valu2
            if results[key] is not None:
                results[key] = results[key] + result # damn it really did seem like i didn't need the if here cause if the key doesn't exist an new entry is created
            else:
                results[key] = result
    return results
def mult_karatsuba_style(p1, p2):
    #dafuq this is supposed to be recursive, why am i not doing that
    p1_values_for_formula = calc_formula_values(p1)
    p2_values_for_formula = calc_formula_values(p2)

    #ok you about to lose it all when you go back to your iterative approach little one
    #but like we've gotten to the point where its at x^1 so not that bad right?
    concat_for_print = {"p1":p1_values_for_formula, "p2":p2_values_for_formula }
    return concat_for_print


    return p1_values_for_formula

def calc_formula_values(x):
    half = len(x)//2

    first_half = x[0:half]
    second_half = x[half:]
    
    first_half_dict = create_d_vaules(first_half, half)
    second_half_dict = create_d_vaules(second_half, half)
    
    dz = {0: first_half_dict, 1: second_half_dict}
    return dz

def create_d_vaules(half_array, half):
    length = half
    d_values = {}
    for val in half_array: # wondering if the index of the element will always correspond to x indices, yes huh? ok think through it after getting this working
        d_values[half - length] = val
        length -= 1
    return d_values






    
