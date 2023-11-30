def thing(a):
    b = ''
    for e in a:
        b += str(e)
    return b

result = thing([1, 1, 1, 1, 1])
print(result)