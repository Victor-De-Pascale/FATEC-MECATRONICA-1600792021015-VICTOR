import random

op_jogada = {}
op_jogada[0] = "PEDRA"
op_jogada[1] = "PAPEL"
op_jogada[2] = "TESOURA"
op_jogada[3] = "LAGARTO"
op_jogada[4] = "SPOCK"

#exluir td isso aqui
xyz_nome = True
xyz_op = False
xyz_maquina = True
#ate aqui

#excluir ao final, comando pro player fazer sua escolha
op_player = int(input("Escolha uma opçao ae "))

#escolha da maquina com random
op_maquina = random.choice(op_jogada)

#comparação
resultado = "EMPATE"
if op_player == 0: #PEDRA
  if (op_maquina == "PAPEL") or (op_maquina == "SPOCK"):
    resultado = "DERROTA"
  elif (op_maquina == "TESOURA") or (op_maquina == "LAGARTO"):
    resultado = "VITORIA"

elif op_player == 1: #PAPEL
  if (op_maquina == "TESOURA") or (op_maquina == "LAGARTO"):
    resultado = "DERROTA"
  elif (op_maquina == "PEDRA") or (op_maquina == "SPOCK"):
    resultado = "VITORIA"

elif op_player == 2: #TESOURA
  if (op_maquina == "PEDRA") or (op_maquina == "SPOCK"):
    resultado = "DERROTA"
  elif (op_maquina == "PAPEL") or (op_maquina == "LAGARTO"):
    resultado = "VITORIA"

elif op_player == 3: #LAGARTO
  if (op_maquina == "PEDRA") or (op_maquina == "TESOURA"):
    resultado = "DERROTA"
  elif (op_maquina == "PAPEL") or (op_maquina == "SPOCK"):
    resultado = "VITORIA"

elif op_player == 4: #SPOCK
  if (op_maquina == "PAPEL") or (op_maquina == "LAGARTO"):
    resultado = "DERROTA"
  elif (op_maquina == "PEDRA") or (op_maquina == "TESOURA"):
    resultado = "VITORIA"

print("")
print(resultado)
print(f"Seu adversário escolheu {op_maquina}...")
print(f"Voce escolheu {op_jogada[op_player]}...")
