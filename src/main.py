def find_text(haystack, needle):
    symbols = set()
    length = len(haystack)
    length1 = len(needle)
    words = {}
    index = []

    for i in range(length - 2, -1, -1):
        if haystack[i] not in symbols:
            words[haystack[i]] = length - i - 1
            symbols.add(haystack[i])

    if haystack[length - 1] not in symbols:
        words[haystack[length - 1]] = length

    words['*'] = length

    if length1 >= length:
        i = length - 1
        find = 0
        while i < length1:
            k = 0
            for j in range(length - 1, -1, -1):
                if needle[i - k] != haystack[j]:
                    if j == length - 1:
                        find = words[needle[i]] if words.get(needle[i], False) else words['*']
                    else:
                        find = words[haystack[j]]
                    i += find
                    break
                k += 1
            if j == 0:
                index.append(i - k + 1)
                i += find

    return index

