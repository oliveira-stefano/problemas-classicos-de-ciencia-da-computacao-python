''' 

A memoizacao eh a tecnica segundo a qual armazenamos os resultados de tarefas computacionais quando estas
estao concluidas, de modo que quando precisarmos  novamente desses resultados, sera possivel consulta-los, em vez de calcula-los uma segunda vez ou pela n-nesimma vez

'''

from typing import Dict

memo: Dict[int, int] = {0:0, 1:1}
def fib3(n: int) -> int:
    '''
    Uma chamada de fib3(20) resultara em apenas 39 chamadas em oposicao as 21mil de fib2
    '''
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n- 2)
    return memo[n]

if __name__ == "__main__":
    print(fib3(50))




    