# Tape Equilibrium :D

# Solution number 1 ( 55% ) --------------------------------------- #
# ======= SWEAR WORDS WARNING !! IF YOURE TOO SENSITIVE, PLEASE JUMP TO LINE 8!! ======= #
# This fucking solution works perfectly, unless youre a complete idiot that wants to use an array with a FUCKING 100 000 POSITIONS
# Maykon, if you're reading this, im sorry

def sum_elements(array, startint_pos, ending_pos=0):
    '''Method to sum the array'''
    if ending_pos == 0: ending_pos = len(array)

    aux = 0
    for i in range(startint_pos, ending_pos):
        aux = array[i] + aux

    return aux


def solution(array):
    list_results = []

    for i in range(1, len(array)):
        result = abs(sum_elements(array, 0, i) - sum_elements(array, i))
        list_results.append(result)
        
    return min(list_results)



# Solution number 2 ( 100% ) --------------------------------------- #

def solution(array):          
    sum_elements = sum(array)
    minimun = float('inf')
    left_sum = 0

    for i in array[:-1]:

        left_sum += i
        minimun = min(abs(sum_elements - 2 * left_sum), minimun)

    return minimun
