'''
1) Observe o trecho de código abaixo:
int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça

{
K = K + 1;
SOMA = SOMA + K;
}
imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
'''

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

'''
2- Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''
# Função para verificar se um número pertence à sequência de Fibonacci


def pertence_fibonacci(num):
    # Inicializa os dois primeiros números da sequência
    fib1, fib2 = 0, 1

    # Itera pela sequência de Fibonacci até o número informado ou até ultrapassá-lo
    while fib2 <= num:
        if fib2 == num:
            return True  # Número pertence à sequência de Fibonacci
        fib1, fib2 = fib2, fib1 + fib2  # Atualiza os valores da sequência
    return False  # Número não pertence à sequência de Fibonacci


# Recebe o número informado pelo usuário
num = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci e exibe a mensagem correspondente
if pertence_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

'''
3- Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
'''
'''
a) A lógica é adicionar 2 ao número anterior. O próximo elemento é 9.
b) A lógica é multiplicar por 2 o número anterior. O próximo elemento é 128.
c) A lógica é elevar ao quadrado o índice do número na sequência. O próximo elemento é 49.
d) A lógica é elevar ao quadrado o índice do número na sequência e somar 12. O próximo elemento é 100.
e) A lógica é somar os dois números anteriores para obter o próximo número. O próximo elemento é 13.
f) A lógica é somar 2 ao primeiro número, 2 ao segundo, 4 ao terceiro, 1 ao quarto, 1 ao quinto e 1 ao sexto. O próximo elemento é 20.
'''

'''A'''
for i in range(1, 6):
    print(2*i - 1)
'''B'''
x = 2
for i in range(1, 8):
    print(x)
    x *= 2
'''C'''
for i in range(8):
    print(i**2)
'''D'''
for i in range(1, 6):
    print((2*i)**2)
'''E'''
a, b = 1, 1
for i in range(7):
    print(a)
    a, b = b, a+b
'''F'''
numeros = [2, 10, 12, 16, 17, 18, 19]
proximo = numeros[-1] + 1
numeros.append(proximo)
print(numeros)

'''
4- Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?
IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

'''
# Distância entre Ribeirão Preto e Franca (km)
distancia = 100

# Velocidade do carro (km/h)
velocidade_carro = 110

# Velocidade do caminhão (km/h)
velocidade_caminhao = 80

# Tempo extra do caminhão em cada pedágio (minutos)
tempo_extra_caminhao = 5

# Tempo total extra do caminhão (horas)
tempo_total_extra_caminhao = tempo_extra_caminhao / 60 * 2

# Tempo que o carro leva para percorrer a distância entre as cidades (horas)
tempo_carro = distancia / velocidade_carro

# Tempo que o caminhão leva para percorrer a distância entre as cidades (horas)
tempo_caminhao = distancia / velocidade_caminhao + tempo_total_extra_caminhao

# Verifica qual veículo está mais próximo de Ribeirão Preto
if tempo_carro < tempo_caminhao:
    print("O carro está mais próximo de Ribeirão Preto")
else:
    print("O caminhão está mais próximo de Ribeirão Preto")

'''
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

'''
# Exemplo de string
s = "hello world"

# Inicializa a string invertida
s_invertida = ""

# Percorre a string de trás para frente e adiciona cada caractere na string invertida
for i in range(len(s)-1, -1, -1):
    s_invertida += s[i]

# Imprime a string invertida
print(s_invertida)

'''OU'''
string = "hello world"
string_invertida = string[::-1]
print(string_invertida)
