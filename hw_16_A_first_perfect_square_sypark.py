def first_perfect_square(numbers):
    f_p_s = -1 
    for i in range(len(numbers)):
        if numbers[i] >= 0 :
            if ((numbers[i] ** 0.5)%1 == 0) :
                f_p_s = i
                break
    return f_p_s
