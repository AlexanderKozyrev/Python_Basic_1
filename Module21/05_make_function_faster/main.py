def calculating_math_func(data, cache={}):
    result = 1
    if data in cache:
        result = cache[data]
    else:
        for index in range(1, data + 1):
            result *= index
        cache[data] = result
    result /= data ** 3
    result = result ** 10
    return result

