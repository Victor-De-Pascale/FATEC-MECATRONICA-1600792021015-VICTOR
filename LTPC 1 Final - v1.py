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
#por enquanto

def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Requerir transação")
  print("2- Pagar transação")
  print("0- Sair")

def f_user():
  vf_user = input("Digite seu usuário: ")
  vf_senha = input("Digite sua senha: ")
  return (vf_user, vf_senha)

def f_verify(vf_user, vf_senha):
  
  if vf_user == user_1:
    if vf_senha == senha_1:
      c_login = True
    else:
      c_login = False
  
  elif vf_user == user_2:
    if vf_senha == senha_2:
      c_login = True
    else:
      c_login = False
  
  elif vf_user == user_3:
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
c_continuar = True

while c_login == False:
  v_user, v_senha = f_user()
  c_login = f_verify(v_user, v_senha)
  if c_login == False:
    print("Usuário incorreto!")
    v_resp = input("Deseja continuar? (s/n): ")
    os.system("clear")
    if v_resp == "n":
      c_login = True
      c_continuar = False
      print("Ação cancelada!")
  else:
    print("Login feito!")
    input("Pressione qualquer tecla para continuar...")

while c_continuar == True:
  os.system("clear")
  f_menu()
  v_opcao = int(input("Opção: "))
  if v_opcao == 0:
    c_continuar = False
  else:
    print("Opção inválida")
    input("Pressione qualquer tecla para continuar")

print("Fim")
