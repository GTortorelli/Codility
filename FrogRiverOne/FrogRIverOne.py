# Frog River One 
# Codility exercise resolution

# def solution(X:int, A:list):

#     flag = 0
#     for i in A:
#         if i == X:
#             flag += 1

#     if flag > 1: return -1


#     if A[0] == None: return -1 

#     for i in range(0, len(A)):
#         if A[i] == X: return i

#     return -1

# print(solution(5, [5, 5, 2, 5, 5]))

def can_froG_jump(X:int, A:list):
    
    leafed_spot_list = list( set(A) )

    j = 0
    for i in range(0, X):
        print(j)
        if A[i] != j: return False
        j += 1

    return True

        
def solution(distance:int, leafes_array:list):

    if can_froG_jump(distance, leafes_array):
        for i in range(0, len(leafes_array)):
            if i == X: return i


can_froG_jump(5, [0, 1, 4, 2, 3, 5])
# print(solution(5, [1, 4, 2, 3, 5]))