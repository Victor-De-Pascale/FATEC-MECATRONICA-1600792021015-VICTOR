import random

op_jogada = {}
op_jogada[0] = "PEDRA"
op_jogada[1] = "PAPEL"
op_jogada[2] = "TESOURA"
op_jogada[3] = "LAGARTO"
op_jogada[4] = "SPOCK"

def vamosJogar():
  player_joga = int(input("Escolha sua jogada: "))
  maquina_joga = random.randint(0, 4)
  return player_joga, maquina_joga

op_player, op_maquina = vamosJogar()

resultado = "EMPATE"
if op_player == 0: #PEDRA
  if (op_maquina == 1) or (op_maquina == 4):
    resultado = "DERROTA"
  elif (op_maquina == 2) or (op_maquina == 3):
    resultado = "VITORIA"

elif op_player == 1: #PAPEL
  if (op_maquina == 2) or (op_maquina == 3):
    resultado = "DERROTA"
  elif (op_maquina == 0) or (op_maquina == 4):
    resultado = "VITORIA"

elif op_player == 2: #TESOURA
  if (op_maquina == 0) or (op_maquina == 4):
    resultado = "DERROTA"
  elif (op_maquina == 1) or (op_maquina == 3):
    resultado = "VITORIA"

elif op_player == 3: #LAGARTO
  if (op_maquina == 0) or (op_maquina == 2):
    resultado = "DERROTA"
  elif (op_maquina == 1) or (op_maquina == 4):
    resultado = "VITORIA"

elif op_player == 4: #SPOCK
  if (op_maquina == 1) or (op_maquina == 3):
    resultado = "DERROTA"
  elif (op_maquina == 0) or (op_maquina == 2):
    resultado = "VITORIA"

print("")
print(resultado)
print(f"Seu adversário escolheu {op_jogada[op_maquina]}...")
print(f"Voce escolheu {op_jogada[op_player]}...")
