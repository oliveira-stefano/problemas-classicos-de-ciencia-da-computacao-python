''' 

Evitar uma recursao infinita é responsabilidade do programador, e não do compilador pu do interpretador.
No exemplo anterior o erro ocorria porque nào especificamos um caso de base. Em uma funcao recursiva
um caso de base serve como ponto de parada

'''
def fib2(n: int) -> int:
    '''
    Exemplo de saida para fib2(4)
    fib2(4) -> fib2(3), fib2(2) = 3
    fib2(3) -> fib2(2), fib2(1) = 2
    fib2(2) -> fib2(1), fib2(0) = 1
    fib2(2) -> fib2(1), fib2(0) = 1
    fib2(1) ->                  = 1
    fib2(1) ->                  = 1
    fib2(1) ->                  = 1
    fib2(0) ->                  = 0
    fib2(0) ->                  = 0
    '''
    if n < 2:
        return n #caso de base
    else:
        return fib2(n - 2) + fib2(n - 1)

if __name__ == "__main__":
    print(fib2(4))




    