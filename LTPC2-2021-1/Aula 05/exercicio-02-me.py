import random

xyz_numero_sorteado = random.randrange(0, 100)
xyz_contador = 0
xyz_continuar = True
xyz_chutes = []

print(xyz_numero_sorteado)

while xyz_continuar:
  
  xyz_intervalo = True
  while xyz_intervalo:
    xyz_valor_digitado = int(input("Chuta um numero ae: ")) 
    if ((xyz_valor_digitado >= 0) and (xyz_valor_digitado <= 100)):
      xyz_intervalo = False
    else:
      print("um numero entre 0 e 100!!")

  xyz_chutes.append(xyz_valor_digitado)
  xyz_contador = xyz_contador + 1

  if xyz_valor_digitado == xyz_numero_sorteado:
    print("Voce acertou!!")
    xyz_continuar = False
  elif xyz_valor_digitado < xyz_numero_sorteado:
    print(f"é maior que {xyz_valor_digitado}!!")
  else:
    print(f"é menor que {xyz_valor_digitado}!!")
  
  print(f"Chances: {10 - xyz_contador}")

  if xyz_contador == 10:
    print("Acabaram suas chances...")
    print(f"O numero correto é {xyz_numero_sorteado}")
    print(f"Suas chances foram {xyz_chutes}")
    xyz_continuar = False

