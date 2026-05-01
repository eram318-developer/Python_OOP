def merge_dictionaries(**kwargs):
    mergeDict ={}
    
    for key in kwargs:
        current_dict = kwargs[key]
        
        for k in current_dict:
            mergeDict[k] = current_dict[k]
    
    return mergeDict


print(merge_dictionaries(a={'x': 1, 'y': 2}, b={'z': 3}))
# Output: {'x': 1, 'y': 2, 'z': 3}
print(merge_dictionaries(x={'a': 10}, y={'b': 20}, z={'c': 30}))
# Output: {'a': 10, 'b': 20, 'c': 30}