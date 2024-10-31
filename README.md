# README - Cálculo de Divisores de um Número Inteiro

## Descrição

O objetivo deste programa é calcular e imprimir todos os divisores positivos de um número inteiro \( N \). O programa deve ler o número e, em seguida, listar todos os seus divisores em ordem crescente.

## Entrada

- A entrada contém um único número inteiro \( N \) (\( N > 0 \)).

## Saída

- A saída consiste em imprimir cada divisor positivo de \( N \) em uma linha separada.

## Exemplo de Uso

### Entrada
```
6
```

### Saída
```
1
2
3
6
```

### Explicação
- Os divisores positivos de 6 são 1, 2, 3 e 6. O programa imprime cada divisor em uma linha separada.

## Algoritmo

O algoritmo para encontrar os divisores de \( N \) segue os seguintes passos:

1. Ler o número inteiro \( N \).
2. Iterar de 1 até \( N \):
   - Para cada número \( i \):
     - Verificar se \( N \) é divisível por \( i \) (ou seja, \( N \mod i = 0 \)).
     - Se for, imprimir \( i \) como um divisor.

## Implementação

O código foi implementado em Python e está estruturado da seguinte maneira:

```python
# Leitura do número inteiro
N = int(input())

# Cálculo e impressão dos divisores
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
```

## Testes

O programa foi testado com os seguintes exemplos:

| Entrada | Saída        |
|---------|--------------|
| 6       | 1            |
|         | 2            |
|         | 3            |
|         | 6            |

## Considerações Finais

O programa é eficiente para a faixa de entrada típica e calcula os divisores de um número inteiro em tempo linear \( O(N) \). Esta solução é ideal para situações em que se requer a análise de divisores em contextos matemáticos ou de programação competitiva.
