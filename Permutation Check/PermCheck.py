# Permutation check - Codility
# 03 - 03 - 2020

# The method must be capable to check if the array is a permutation :D


def solution(array:list):
    array = sorted(array)
    if array[0] != 1:
        return 0

    j = array[0]
    for i in array:
        if i != j:
            return 0
        j += 1

    return 1
