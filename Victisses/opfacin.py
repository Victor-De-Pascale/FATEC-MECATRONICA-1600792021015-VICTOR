xyz_lista = []
xyz_minilista = []
contador = 0
while contador < 15:
  xyz_minilista = op_facin
  contador_lista = 0
  while contador_lista < (len(op_facin) + 1):
    xyz_minilista.append(op_facin[contador_lista])
  xyz_numero_sorteado = random.randrange(1, 25)
  if xyz_minilista.count(xyz_numero_sorteado) == 1:
    xyz_minilista.remove(xyz_numero_sorteado)
    contador = contador + 1
