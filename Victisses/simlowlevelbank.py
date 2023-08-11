import os
import random

def xyz_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Criar/Adicionar Usuário")
  print("2- Enviar transação")
  print("3- Pedir transação")
  print("4- Exibir QRCode (ADMIN)")
  print("5- Exibir saldos (ADMIN)")
  print("6- Exibir usuários, emails e ID's (ADMIN)")
  print("0- Sair")
  print("")

def xyz_int_verify(xyz_txt):
  try:
    int(xyz_txt)
  except:
    os.system("clear")
    input("Por favor digite um número!")
  else:
    xyz_valid = 1
    return xyz_valid

def xyz_activate_menu():
  xyz_valid_op = False
  while xyz_valid_op == False:
    os.system("clear")
    xyz_menu()
    xyz_op = input("Selecione uma das opções acima: ")
    xyz_verify = xyz_int_verify(xyz_op)
    if xyz_verify == 1:
      xyz_valid_op = True
  return xyz_op

def xyz_create_user():
  xyz_name = input("Digite o nome do novo usuário: ")
  xyz_pw = input("Digite a senha: ")
  xyz_valid_op = False
  while xyz_valid_op == False:
    xyz_saldo = input("Digite o saldo inicial: ")
    xyz_verify = xyz_int_verify(xyz_saldo)
    if xyz_verify == 1:
      xyz_valid_op = True
  print(xyz_name)
  print(xyz_pw)
  print(xyz_saldo)
  input("")

#main
xyz_end = False
while xyz_end == False:
  xyz_op = int(xyz_activate_menu())
  
  if xyz_op == 0:
    os.system("clear")
    print("Finalizado!")
    xyz_end = True

  elif xyz_op == 1:
    xyz_create_user()
