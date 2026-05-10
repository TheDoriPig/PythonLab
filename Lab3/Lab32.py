d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], [True, [1, -1]]], 7.89]
def exp(ag):
    res = []
    for item in ag:
        if isinstance(item, list):
            res.extend(exp(item))
        else:
            res.append(item)
    return res
flatd = exp(d)
print(flatd)