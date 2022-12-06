import random
import os

op_facin = []
contador = 1
while contador < 26:
  op_facin.append(contador)
  contador = contador + 1

xyz_resultado = []
xyz_n = 0
while xyz_n < 15:
  print(xyz_resultado)
  print("")
  xyz_item = int(input("Digite o proximo numero: "))
  print("")
  if xyz_resultado.count(xyz_item) == 0:
    xyz_resultado.append(xyz_item)
    xyz_n = xyz_n + 1
  else:
    print("numero ja esta na lista")
  os.system("clear")


os.system("clear")

lista_permaban = []
contador = 0
while contador < 4:
  xyz_numero_sorteado = random.randrange(1, 26)
  if lista_permaban.count(xyz_numero_sorteado) == 0 and xyz_numero_sorteado != 26:
    lista_permaban.append(xyz_numero_sorteado)
    op_facin.remove(xyz_numero_sorteado)
    contador = contador + 1

lista_permaban.sort()
xyz_resultado.sort()
print("Números excluídos: ", lista_permaban)
print("")
print("Opções disponíveis: ", op_facin) #teste
print("")
print("Resultado: ", xyz_resultado)
print("")
                                         
x_lista_principal = []
x_lista_dentro_de_lista = []
contador = 0
while contador < 30:
  #reset de lista
  contador_lista = 0
  while contador_lista < (len(op_facin)):
    x_lista_dentro_de_lista.append(op_facin[contador_lista])
    contador_lista = contador_lista + 1
  #reset de lista

  #deixar 15 numeros
  contador_remocao = 1
  while contador_remocao < 7:
    x_rnd_n = random.randrange(1, 26)
    if x_lista_dentro_de_lista.count(x_rnd_n) == 1:
      x_lista_dentro_de_lista.remove(x_rnd_n)
      contador_remocao = contador_remocao + 1
  #deixar 15 numeros
  #fruits.count('apple') , fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
  xyz_varredura = 0
  xyz_acertos = 0
  while xyz_varredura < 15:
    if x_lista_dentro_de_lista.count(xyz_resultado[xyz_varredura]) == 1:
      xyz_acertos = xyz_acertos + 1
    xyz_varredura = xyz_varredura + 1

  print(f"CARTELA nº: {(contador + 1)}")
  print(x_lista_dentro_de_lista)
  print(f"ACERTOS: {xyz_acertos}")
  print("")
  #adicionar na lista principal
  x_lista_dentro_de_lista.clear()
  contador = contador + 1

#print("Item da posicao 5 da lista principal: ", op_facin[5])
#print("")
#print(len(lista_permaban))
