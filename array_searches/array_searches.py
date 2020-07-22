def binary_search(array, value):
    #assuming she sorted
    bottom = 0
    top = len(array) - 1
    return creo_mass(bottom, top,array, value)

def creo_mass(bottom, top, array, value):
    if array[bottom] == value:
        return bottom
    elif array[top] == value:
        return top
    else:
        start = (top - bottom)//2 + bottom
        if start == bottom:
            return "NOT_FOUND"
        if array[start] > value:
            return creo_mass(bottom, start, array, value)
        else:
            return creo_mass(start, top, array, value)







