#exercicio 2 - aula 5

lado_a = int(input('Digite o valor do Lado A: '))
lado_b = int(input('Digite o valor do Lado B: '))
lado_c = int(input('Digite o valor do Lado C: '))

if (lado_a > 0) and (lado_b > 0) and (lado_c > 0):
  if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    print('É um triângulo!')
  else:
    print('NÃO é um triângulo!')
else:
  print('Impossível ser triângulo')
