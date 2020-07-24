def mult_poly(p1, p2):
    results = {}
    for idx, val in enumerate(p1):
        for idx2, valu2 in enumerate(p2):
            key = idx + idx2
            result = val*valu2
            if key in results:
                results[key] = results[key] + result # damn it really did seem like i didn't need the if here cause if the key doesn't exist an new entry is created
            else:
                results[key] = result
    return results
