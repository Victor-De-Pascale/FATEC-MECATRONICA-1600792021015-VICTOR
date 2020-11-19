v1_user = "user 1"
v2_user = "user 2"
v3_user = "user 3"
#por enquanto
v1_senha = "senha 1"
v2_senha = "senha 2"
v3_senha = "senha 3"

def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Requerir transação")
  print("2- Pagar transação")
  print("0- Sair")

def f_verify():
  print("só ppra falar q tem algo aqui")

#main
import os
c_continuar = True
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
