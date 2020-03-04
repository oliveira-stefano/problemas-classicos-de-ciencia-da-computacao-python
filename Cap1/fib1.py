''' 
Na matemática, a Sucessão de Fibonacci (também Sequência de Fibonacci), é uma sequência de números inteiros,
começando normalmente por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores.
A sequência recebeu o nome do matemático italiano Leonardo de Pisa, mais conhecido por Fibonacci, que descreveu,
no ano de 1202, o crescimento de uma população de coelhos, a partir desta.
'''
def fib1(n: int) -> int:    
    '''
    O problema é o fato de fib1() executar indefinidamente, sem devolver um resultado definitivo
    '''
    return fib1(n - 1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(15))