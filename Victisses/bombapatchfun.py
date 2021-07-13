import random

gols_sofridos = []
op_gols = [2,3,3,2,0,1,3,2,3,3,1,3,2,3,3,2,3,3,2,3]
usar_tatica = []
op_tatica = [2,3,4,5,2,3,4,5,1,2,4,3,5,1]
contador = 0

while contador < 10:
  usar_tatica.append(random.choice(op_tatica))
  gols_sofridos.append(random.choice(op_gols))
  contador = contador + 1

print(usar_tatica)
print(gols_sofridos)
