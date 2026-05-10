lst = [1, 2, [True, False, ["a", "ra"]], 3]
flat_list = []

for item in lst:
    if isinstance(item, list):
        for sub_item in item:
            if isinstance(sub_item, list):
                for deep_item in sub_item:
                    flat_list.append(deep_item)
            else:
                flat_list.append(sub_item)
    else:
        flat_list.append(item)

print(flat_list)
