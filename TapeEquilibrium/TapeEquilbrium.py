# Tape Equilibrium :D

def sum_elements(array, startint_pos, ending_pos=0):
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

print(solution())