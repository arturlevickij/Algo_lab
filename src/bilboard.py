def bilboard(k, t, l):
    if len(l) % k != 0:
        itr = len(l) % k
    else:
        itr = len(l) // k
    paints = [0] * itr
    suma = []
    for i, el in enumerate(l):
        if i % itr == 0 and i != 0:
            suma.append(sum(paints))
            paints = [0] * itr
        paints[i % itr] = t * el
        if i + 1 == len(l):
            suma.append(sum(paints))
    min_time = max(suma)
    return min_time


lis = [1]*100
lis[99] = 30
print(bilboard(5, 1, lis))
