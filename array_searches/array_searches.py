def binary_search(array, value):
    #assuming she sorted
    bottom = 0
    top = len(array) - 1
    return creo_mass(bottom, top,array, value)
def creo_mass(bottom, top, array, value):
    if array[bottom] is value:
        return bottom
    elif array[top] is value:
        return top
    else:
        start = (top - bottom)//2 + bottom
        if array[start] > value:
            return creo_mass(bottom, start, array, value)
        else:
            return creo_mass(start, top, array, value)







