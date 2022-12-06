import os

xyz_resultado = []
xyz_n = 0
while xyz_n < 15:
  os.system("clear")
  print(xyz_resultado)
  print("")
  xyz_item = int(input("Digite o proximo numero: "))
  print("")
  if xyz_resultado.count(xyz_item) == 0:
    xyz_resultado.append(xyz_item)
    xyz_n = xyz_n + 1

os.system("clear")

xyz_lista = []
xyz_acertos = 0
xyz_cont = 0
while xyz_cont < 15:
  if xyz_lista.count(xyz_resultado[xyz_cont]) == 1:
    xyz_acertos = xyz_acertos + 1
  xyz_cont = xyz_cont + 1

print(xyz_resultado)
print("")
print(xyz_lista)
print("")
print(f"ACERTOS: {xyz_acertos}")
