def merge_unique(dicts):
    # initialize an empty dictionary to store the result
    result = {}
    # initialize a set to store the values of all dictionaries
    values = set()
    # loop through each key-value pair in the input dictionary
    for k, v in dicts.items():
        # check if the value is a list of numbers
        if isinstance(v, list) and all(isinstance(n, (int, float)) for n in v):
            # check if the value is present in any other dictionary
            if v not in values:
                # if not, add it to the result dictionary
                result.update({k: v})
            # add the value to the set
            values.add(v)
    # return the result dictionary
    return result


# test the function with some sample dictionaries
dicts = {
    "P1": [1, 2, 3],
    "P2": [4, 5, 6],
    "P3": [7, 8, 9],
    "P4": [10, 11, 12],
    "P5": [13, 14, 15],
    "P6": [16, 17, 18],
    "P7": [1, 2, 3],
    "P8": [13, 14, 15],
}

# call the function and print the result
print(merge_unique(dicts))
