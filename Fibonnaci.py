'''1. Elabore  um  programa  em  linguagem Python  que leia  um número inteiro N e, em seguida, mostre na tela os N primeiros termos da sequência  de  Fibonacci.
Faça  o  programa  de  modo  que  o valor  de  N seja no mínimo 2.A  sequência  de  Fibonacci  éuma  sequência  de  números  inteiros que têmas seguintes regras de formação: 
os dois primeiros termos são 0  e  1;  do  terceiro  termo  em  diante  cada  termo é a  soma  dos  dois anteriores. '''
#Exemplo: Se N = 10, então: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


lista = [0, 1]

n = int(input("Digite um número para a Fibonnaci: "))

for i in range(n):
    result = (lista[i] + lista[i+1]) #basicamente = indice 0 (i) + indice 1 (i + 1 = 0 + 1 = 1)  >>>>>> lista[0 + 1 = 1] = [0, 1, 1]
    lista.append(result)
print(lista)