# Exercício 1: Fatorial de um número
def fatorial(n):
    return 1 if n <= 1 else n * fatorial(n - 1)

# Exercício 2: Verificar se um número é primo
def eh_primo(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

# Exercício 3: Encontrar o maior elemento em uma lista
def maior_elemento(lista):
    return max(lista)