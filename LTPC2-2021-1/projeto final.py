import random

op_jogada = {}
op_jogada[1] = "PEDRA"
op_jogada[2] = "PAPEL"
op_jogada[3] = "TESOURA"
op_jogada[4] = "LAGARTO"
op_jogada[5] = "SPOCK"

#exluir td isso aqui
xyz_nome = False
xyz_op = False
#ate aqui

#so pra checar apenas only, excluir ao final
while xyz_op == True:
  for op_item in op_jogada.keys():
    print(f"chave: {op_item} - valor: {op_jogada[op_item]}")
  xyz_op = False

#excluir ao final
while xyz_nome == True:
  mostrar_op = int(input("Escolha uma opçao ae "))
  print(op_jogada[mostrar_op])
  xyz_nome = False

nome_player = input("Digite seu nome ") #variavel nome aqui


