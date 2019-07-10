def second_largest(values):
    max_v = values[0]
    max_i = 0
    
    for i in range(len(values)):
        if max_v < values[i] :
            max_v = values[i]
            max_i = i

    new_values = values[:max_i]+values[max_i+1:]

    max_v = new_values[0]
    
    for i in range(len(new_values)):
        if max_v < new_values[i] : max_v = new_values[i]

    return max_v
    
