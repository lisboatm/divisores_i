# Leitura do número inteiro
N = int(input())

# Cálculo e impressão dos divisores
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
