#EX026 Faça um programa que leia uma frase pelo teclado e mostre:

#Quantas vezes apararece aletra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

#Exercicio resolvido pelo Prof. Gustavo.

#upper coloca toda a frase em maiusco e strip, remove todos os espaços que não são necessário.
frase = str(input('Digite uma frase: ')).upper().strip()

# Conta quantas vezes apaarece a letra A na frase.
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

# Find busca pelo inicio da frase, qual a primeira letra A, assim apontando sua posição. +1 reajusta a posição do indice, já que por padra o indice sempre começa em 0.
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))

# RFind busca pelo inicio do lado direito (fim) da frase, qual a ultima letra A, assim apontando sua posição. +1 reajusta a posição do indice, já que por padra o indice sempre começa em 0.

print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))