def num_perfect_squares(numbers):
    n_p_s = 0 
    for i in range(len(numbers)):
        if numbers[i] >= 0 :
            if ((numbers[i] ** 0.5)%1 == 0) :
                n_p_s += 1
    return n_p_s
