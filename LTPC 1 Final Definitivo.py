#COMEÇA AQUI

v_users = ""
v_senhas = ""
v_emails = ""
v_saldos = ""
v_ids = ""
v_qr_code = ""
import os

#incompleto
def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Criar/Adicionar Usuário")
  print("2- Enviar transação")
  print("3- Pedir transação")
  print("0- Sair")

#main
c_fim_do_programa = False
while c_fim_do_programa == False:
  os.system("clear")
  f_menu()
  d_op = int(input("Digite uma das opcoes abaixo: "))
  
  #if 1
  if d_op == 1:
    os.system("clear")
    cf_continuar = True
    while cf_continuar == True:
      var_criar_nomes = input("Digite o nome do usuario: ")
      var_criar_senhas = input("Digite a senha para este usuario: ")
      var_criar_saldos = input("Saldo inicial deste usuario: ")

      #formatação
      var_add_pev = var_criar_nomes + ";"
      var_add_mail = var_criar_nomes + "@mail;"
      var_add_senha = var_criar_senhas + ";"
      var_add_saldo = var_criar_saldos + ";"

      v_users = v_users + var_add_pev.upper()
      v_emails = v_emails + var_add_mail.upper()
      v_senhas = v_senhas + var_add_senha
      v_saldos = v_saldos + var_add_saldo

      var_contador_usuario = 0
      for var_caracter in v_users:
        if var_caracter == ";":
          var_contador_usuario = var_contador_usuario + 1
      
      var_add_id = var_criar_nomes.upper() + str(var_contador_usuario) + ";"
      v_ids = v_ids + var_add_id
      #formatação

      #tirar
      print(v_users)
      print(v_emails)
      print(v_senhas)
      print(v_saldos)
      print(v_ids)
      #tirar

      input("Pressione qlqr tecla pra continuar...")
      os.system("clear")
      xyz_op = input("Deseja continuar adicionando usuarios? (s/n) ")
      if xyz_op != "s":
        cf_continuar = False
  #if 1  
  

  #if 2
  elif d_op == 2:
    if v_qr_code == "":
      print("")
      print("Não há requisição de pagamento")
      input("")
  #if 2


  #if 3
  elif d_op == 3:
    v_existe = False
    while v_existe == False:
      os.system("clear")
      user_rec = int(input("Indique, por ID, qual usuário irá receber o pagamento: "))
      var_contador_usuario = 0
      for var_caracter in v_users:
        if var_caracter == ";":
          var_contador_usuario = var_contador_usuario + 1
      if user_rec > var_contador_usuario:
        input("Usuario não existe!")
      else:
        v_existe = True
    
  #if 3


  #if 0
  elif d_op == 0:
    c_fim_do_programa = True
  #if 0


  #if erro
  else:
    os.system("clear")
    input("Opção Inválida! pressione qualquer tecla para continuar...")
  #if erro

os.system("clear")
print("Fim")
