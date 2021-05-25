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

#so pra checar apenas only, excluir ao final
while xyz_op == True:
  for op_item in op_jogada.keys():
    print(f"chave: {op_item} - valor: {op_jogada[op_item]}")
  xyz_op = False

#excluir ao final, comando pro player fazer sua escolha
while xyz_nome == True:
  op_player = int(input("Escolha uma opçao ae "))
  #print(op_jogada[op_player])
  xyz_nome = False

#escolha da maquina com random
op_maquina = random.choice(op_jogada)
while xyz_maquina == True:
  #print(op_maquina)
  xyz_maquina = False

#comparação
resultado = "EMPATE"
if op_player == 0:
  if op_maquina == 
