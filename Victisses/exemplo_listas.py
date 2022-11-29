import random

xyz_lista = []
cont = 0

while cont < 6:
  xyz_n = random.randrange(1, 25)
  xyz_lista.insert(cont, xyz_n)
  cont = cont + 1
  print(xyz_n)
  print("")

print(xyz_lista)
