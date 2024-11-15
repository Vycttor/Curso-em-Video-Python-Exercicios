#Ex.42 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#-Equilátero: todos os lados iguais.
#-Isósceloes: dois lados iguais.
#-Escalenos: Todos os lados diferente.


#Programa feito pelo Prof. Gustavo Guanabara, dia 04/11/2024.

print("-="*20)
print('Analisador de Triângulo')
print("-="*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO! ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')