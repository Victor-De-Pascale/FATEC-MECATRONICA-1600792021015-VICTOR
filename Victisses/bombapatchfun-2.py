import random

gols_sofridos_liga = []
op_gols_liga = [0,"Draw",2,1,"Draw","Lose",1,"Lose",0,2,"Draw"]
contador = 0

while contador < 20:
  gols_sofridos_liga.append(random.choice(op_gols_liga))
  contador = contador + 1
contador = 0


op_gols_champions = [0,"D3","E",0,"D4","E","D5",0]
gols_sofridos_champions = []

while contador < 20:
  gols_sofridos_champions.append(random.choice(op_gols_champions))
  contador = contador + 1
contador = 0


op_gols_copa = ["D3","D4","D5","D6"]
gols_sofridos_copa = []

while contador < 20:
  gols_sofridos_copa.append(random.choice(op_gols_copa))
  contador = contador + 1
contador = 0


usar_tatica = []
op_tatica = [3,1,5,6,7,1,3,4,5,2]

while contador < 20:
  usar_tatica.append(random.choice(op_tatica))
  contador = contador + 1


print("TATICA")
print(usar_tatica)
print("LIGA")
print(gols_sofridos_liga)
print("CHAMPIONS")
print(gols_sofridos_champions)
print("COPA")
print(gols_sofridos_copa)
