import os

v_user1, v_user2, v_user3, v_user4, v_user5, v_user6, v_user7, v_user8 = ""
v_senha1, v_senha2, v_senha3, v_senha4, v_senha5, v_senha6, v_senha7, v_senha8 = ""
v_email1, v_email2, v_email3, v_email4, v_email5, v_email6, v_email7, v_email8 = ""
v_saldo1, v_saldo2, v_saldo3, v_saldo4, v_saldo5, v_saldo6, v_saldo7, v_saldo8 = 0


def f_menu():
  print("Bem vindo ao banco virtual!")
  print("")
  print("1- Criar/Adicionar usuário")
  print("2- Enviar transação")
  print("3- Receber transação")
  print("0- Sair")
  #print("")
  #print("")
  #print("")

c_fim_do_programa = False
while c_fim_do_programa == False:
  os.system("clear")
  f_menu()

