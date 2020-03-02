# Frog jump
# Função recebe a posição inicial, a posiçãoq que o sapo quer chegar e a distância de seus pulos.
# a função retorna a quantidade de pulos que o sapo precisa dar para sair da posição inicial e chegar no destino
def solution(starting_position, goal_position, jump_distance):
    if(starting_position >= goal_position): return 0

    result = (goal_position - starting_position) / jump_distance

    if result % 1 !=0:
        result = result + 1

    return int(result)

print(solution(1, 5, 2))