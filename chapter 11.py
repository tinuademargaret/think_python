# ex 11.1




# ex 11.2


def histogram(s):
    d = dict()
    for c in s:
        v = d.get(c, 0)
        d[c] = v + 1
    return d


print(histogram('hipopotamaus'))


# ex 11.3
def print_hist(h):
    key = h.keys()
    key = list(key)
    key.sort()
    print(key)
    for k in key:
        print(k, h[k])


print_hist(histogram('hipopotamaus'))


# ex11.4

def reverse_lookup(d, v):
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys


reverse_lookup()