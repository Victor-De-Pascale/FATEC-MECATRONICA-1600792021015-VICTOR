import random
import os

op_facin = []
contador = 1
while contador < 26:
  op_facin.append(contador)
  contador = contador + 1

lista_permaban = []
contador = 0
while contador < 4:
  xyz_numero_sorteado = random.randrange(1, 26)
  if lista_permaban.count(xyz_numero_sorteado) == 0 and xyz_numero_sorteado != 26:
    lista_permaban.append(xyz_numero_sorteado)
    op_facin.remove(xyz_numero_sorteado)
    contador = contador + 1

lista_permaban.sort()
print("Números excluídos: ", lista_permaban)
print("")
print("Opções disponíveis: ", op_facin) #teste
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

  print(f"CARTELA nº: {(contador + 1)}")
  print(x_lista_dentro_de_lista)
  print("")
  #adicionar na lista principal
  x_lista_dentro_de_lista.clear()
  contador = contador + 1

#print("Item da posicao 5 da lista principal: ", op_facin[5])
#print("")
#print(len(lista_permaban))
