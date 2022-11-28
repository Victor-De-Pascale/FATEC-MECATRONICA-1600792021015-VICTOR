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
  xyz_numero_sorteado = random.randrange(1, 25)
  if lista_permaban.count(xyz_numero_sorteado) == 0:
    lista_permaban.append(xyz_numero_sorteado)
    op_facin.remove(xyz_numero_sorteado)
    contador = contador + 1
  
x_lista_principal = []
x_lista_dentro_de_lista = []
contador_lista = 0
contador = 0
while contador < 31:
  #reset de lista
  contador_lista = 0
  while contador_lista < (len(op_facin) + 1):
    x_lista_dentro_de_lista.append(op_facin[contador_lista])
    contador_lista = contador_lista + 1
  #reset de lista

  #deixar 15 numeros
  contador_remocao = 0
  while contador_remocao < 10:
    x_rnd_n = random.randrange(1, 25)
    if x_lista_dentro_de_lista.count(x_rnd_n) == 1:
      x_lista_dentro_de_lista.remove(x_rnd_n)
      contador_remocao = contador_remocao + 1
  #deixar 15 numeros
  
  contador = contador + 1

lista_permaban.sort()
print("Permanente: ", op_facin) #teste
print("")
print("Permaban: ", lista_permaban)
print("")
print("Item da posicao 5 da lista principal: ", op_facin[5])
print("")
print(len(op_facin))
print("")
print(len(lista_permaban))

#escolher 4 numeros aleatorios;
#  -verificar repetiçoes
#FEITO

#remover os 4 numeros da lista; 
#FEITO

#gerar listas de 15 numeros aleatorios
#  -copiar lista original, por que terá reset
#  -gerar 30 listas, verificando repetição
