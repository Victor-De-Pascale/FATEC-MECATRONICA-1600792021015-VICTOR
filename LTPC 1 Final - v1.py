#por enquanto
user_1 = "user 1"
user_2 = "user 2"
user_3 = "user 3"

senha_1 = "senha 1"
senha_2 = "senha 2"
senha_3 = "senha 3"

saldo_1 = 1000
saldo_2 = 1000
saldo_3 = 1000

email_1 = "u@1"
email_2 = "u@2"
email_3 = "u@3"
#por enquanto

#incompleto
def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Requerir transação")
  print("2- Pagar transação")
  print("0- Sair")

#acho q ira mudar depois de colocar o "for"
def f_user():
  vf_user = input("Digite seu usuário: ")
  vf_senha = input("Digite sua senha: ")
  return (vf_user, vf_senha)

#vai mudar porem essa é a base
def f_verify(vf_user, vf_senha):
#mudar, esse é versao teste  
  if (vf_user == user_1) or (vf_user == email_1):
    if vf_senha == senha_1:
      c_login = True
    else:
      c_login = False
  
  elif (vf_user == user_2) or (vf_user == email_2):
    if vf_senha == senha_2:
      c_login = True
    else:
      c_login = False
  
  elif (vf_user == user_3) or (vf_user == email_3):
    if vf_senha == senha_3:
      c_login = True
    else:
      c_login = False
  
  else:
    c_login = False
  
  return c_login

#main
import os
c_login = False
c_menu = True
c_fim_do_programa = False

while c_fim_do_programa == False:
  
  while c_login == False:
    v_user, v_senha = f_user()
    c_login = f_verify(v_user, v_senha)
    if c_login == False:
      print("Usuário incorreto!")
      v_resp = input("Deseja continuar? (s/n): ")
      os.system("clear")
      if v_resp == "n":
        c_login = True
        c_menu = False
        print("Ação cancelada!")
    else:
      print("Login feito!")
      input("Pressione qualquer tecla para continuar...")

print("Fim")
