# Perm. Missing Element
# O método recebe um vetor com numeros em ordem crescente, posicionados aleatoriamente
# Um dos elementos está faltando na ordem
# O método acha e retorna o número que falta.
def solution(array:list):

    array = sorted(array)

    if(not(array)): return 1
    if(array[0] != 1): return 1
    
    j = array[0]

    for i in array:
        if (i != j): return (j)
        j += 1

    return array[-1] + 1

print(solution([4]))
print(solution([2, 3, 1, 5]))