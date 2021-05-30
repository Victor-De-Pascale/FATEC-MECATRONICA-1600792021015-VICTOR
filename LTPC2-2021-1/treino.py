import random
import os

op_jogada = {}
op_jogada[0] = "PEDRA"
op_jogada[1] = "PAPEL"
op_jogada[2] = "TESOURA"
op_jogada[3] = "LAGARTO"
op_jogada[4] = "SPOCK"

hist_player = []
hist_maquina = []
hist_confronto = {}

conta_rodadas = 0
rodajogo = True

def vamosJogar(op_item):
  print("")
  playerburro = True
  while playerburro == True:
    player_joga = int(input("Escolha sua jogada: "))
    if ((player_joga < 0) or (player_joga > 4)):
      os.system("clear")
      print("ESCOLHA UMA DAS OPÇÕES KRL")
      for item in op_item.keys():
        print(f"OPÇÃO {op_item[item]} - VALOR {item}")
    else:
      playerburro = False
  maquina_joga = random.randint(0, 4)
  return player_joga, maquina_joga

def montarHistorico(contador, resultado, c_player, c_maquina, c_jogada, listaplayer, listamaquina, chavehistorico):
  listaplayer.append(c_jogada[c_player])
  listamaquina.append(c_jogada[c_maquina])
  chavehistorico[f"JOGO {contador}"] = f"{resultado}"
  return listaplayer, listamaquina, chavehistorico

def menuMain():
  os.system("clear")
  print("BEM VINDO AO EXPERT JOKENPO!")
  print("ESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR")
  print("[1] JOGAR")
  print("[2] MOSTRAR HISTORICO")
  print("[0] SAIR")

def mostrarResultado(resultado, c_player, c_maquina, c_jogada):
  os.system("clear")
  print(resultado)
  print(f"Seu adversário escolheu {c_jogada[c_maquina]}...")
  print(f"Voce escolheu {c_jogada[c_player]}...")
  input("")

def mostrarHistorico(listaplayer, listamaquina, chavehistorico):
  print(listaplayer)
  print(listamaquina)
  print(chavehistorico)
  input("")
  
def verificaJogada(op_player, op_maquina, cont):
  resultado = "EMPATE"
  cont = cont + 1

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

  return resultado, cont

while rodajogo == True:
  menuMain()
  print("")
  op_menu = int(input("Sua opção: "))
  
  if op_menu == 0:
    os.system("clear")
    print("Obrigado por jogar!")
    rodajogo = False
  
  elif op_menu == 1:
    #Passo 1 - Mecanica
    op_player, op_maquina = vamosJogar(op_jogada)
    #Passo 2 - Comparaçao
    result, conta_rodadas = verificaJogada(op_player, op_maquina, conta_rodadas)
    #Passo 3 - Retorno do resultado
    mostrarResultado(result, op_player, op_maquina, op_jogada)
    #Passo 4 - Construção do histórico
    hist_player, hist_maquina, hist_confronto = montarHistorico(conta_rodadas, result, op_player, op_maquina, op_jogada, hist_player, hist_maquina, hist_confronto)
    #Victor diz: sim, isso tudo é uma linha só
  
  elif op_menu == 2:
    os.system("clear")
    if conta_rodadas == 0:
      print("Não houve partidas jogadas!")
      input("")
    else:
      mostrarHistorico(hist_player, hist_maquina, hist_confronto)
  
  else:
    print("Opção inválida!")
    input("")

#Fim
