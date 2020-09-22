#exercicio 1 - aula 5

A = int(input('Digite o valor do A: '))
B = int(input('Digite o valor do B: '))
C = int(input('Digite o valor do C: '))

if A >= B and A >= C:
  maior = A
elif B >= A and B >= C:
  maior = B
else:
  maior = C

if A <= B and A <= C:
  menor = A
elif B <= A and B <= C:
  menor = B
else:
  menor = C

print("Maior valor:", maior)
print('Menor valor:', menor)

media = (A + B + C) / 3
print('Valor médio:', media)
