table = {}

def get_indices_of_item_weights(weights, length, limit):
    
    """
    YOUR CODE HERE
    """
    ## weight of 2 which equals limit
    ## limit - weight = required pair
    ## pair in table? no? add weight to table yes? return value indices 
    for i in range(length):
        required = limit - weights[i]
        if required in table.values():
            return [i, weights.index(required)]
        else:
            table[i] = weights[i]
            i += 1
    return None

weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))