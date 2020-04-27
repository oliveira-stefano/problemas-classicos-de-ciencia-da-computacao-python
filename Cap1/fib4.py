''' 

Evitar uma recursao infinita é responsabilidade do programador, e não do compilador pu do interpretador.
No exemplo anterior o erro ocorria porque nào especificamos um caso de base. Em uma funcao recursiva
um caso de base serve como ponto de parada

'''
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    '''
    Exemplo de saida para fib4(4)
    fib4(4) -> fib4(3), fib4(2) = 3
    fib4(3) -> fib4(2), fib4(1) = 2
    fib4(2) -> fib4(1), fib4(0) = 1
    fib4(2) -> fib4(1), fib4(0) = 1
    fib4(1) ->                  = 1
    fib4(1) ->                  = 1
    fib4(1) ->                  = 1
    fib4(0) ->                  = 0
    fib4(0) ->                  = 0
    '''
    if n < 2:
        return n #caso de base
    else:
        return fib4(n - 2) + fib4(n - 1)

if __name__ == "__main__":
    print(fib4(300))




    