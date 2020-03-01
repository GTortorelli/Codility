# Odd Ocucurrences in Array
# solução numero 1 ----------------------------------------------------
def solution(array):

    len_array = len(array)

    for i in range(0, len_array):
        # Contador que irá dizer quantos pares de numeros existem
        contador_pares = 0
        for j in range(0, len_array):
            if array[i] == array[j]:
                contador_pares += 1

        # Aqui é ralizada uma verificação: Caso o numero tenha um par, o programa continua, caso contrário, é retornado o numero sem par
        if contador_pares  % 2 != 0:
            return array[i]

# Como a solução numero 1 não passou no codility, penseie m outra usando verificação bit a bit 
def solution3(array):
    # Resultado por default recebe 0
    resultado = 0
    for i in array:
        # realizando uma verificação XOR => resultado XOR (elemento do array) e armazenando no resultado
        # o resultado so vai receber o numero cujos bits sejam diferentes, ou seja, o único numero que não tem par
        resultado = resultado ^ i 
    
    return resultado

print(solution1([1, 2, 1, 2, 3]))
print(solution2([1, 2, 1, 2, 3]))


