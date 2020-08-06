# Frog River One 
# Codility exercise resolution

# def solution(x:int, a:list):

#     flag = 0
#     for i in a:
#         if i == x:
#             flag += 1

#     if flag > 1: return -1


#     if a[0] == None: return -1

#     for i in range(0, len(a)):
#         if a[i] == x: return i

#     return -1

# print(solution(5, [5, 5, 2, 5, 5]))

def can_frog_jump(x: int, a: list):
    leafed_spot_list = list(set(a))
    j = 0
    for i in range(0, x):
        print(j)
        if a[i] != j:
            return False
        j += 1
    return True


def solution(distance: int, leaves_array: list):
    if can_froG_jump(distance, leaves_array):
        for i in range(0, len(leaves_array)):
            if i == x:
                return i


can_froG_jump(5, [0, 1, 4, 2, 3, 5])
# print(solution(5, [1, 4, 2, 3, 5]))