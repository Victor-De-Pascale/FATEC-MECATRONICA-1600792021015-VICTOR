#COMEÇA AQUI

v_users = ""
v_senhas = ""
v_emails = ""
v_saldos = ""
v_ids = ""
v_qr_code = ""
import os
import random

#incompleto
def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Criar/Adicionar Usuário")
  print("2- Enviar transação")
  print("3- Pedir transação")
  print("4- Exibir QRCode (ADMIN)")
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
    if v_qr_code == "":
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
      os.system("clear")
      valor_rec = int(input("Indique o valor desejado: "))
      os.system("clear")

      c_inicial = 0
      c_final = 0
      c_pev = 0
      c_count = 0
      for caracter in v_users:
        c_count = c_count + 1
        if caracter == ";":
          c_pev = c_pev + 1
          if c_pev == (user_rec - 1):
            c_inicial = c_count
          if c_pev == user_rec:
            c_final = c_count
      
      v_user_atual = v_users[c_inicial:(c_final - 1)]
      v_random = random.randrange(1000, 9999)

      v_qr_code = str(user_rec) + ";" + v_user_atual + ";" + str(valor_rec) + ";" + str(v_random)
      print("QRCode gerado!")
      print(v_qr_code)
      print("")
      input("Anote-o com cuidado!")

    else:
      print("Ja existe um pedido em andamento, impossível fazer outro requerimento no momento!")
      input("Continuar....")

    
  #if 3


  #if 0
  elif d_op == 0:
    c_fim_do_programa = True
  #if 0


  #if 4
  elif d_op == 4:
    os.system("clear")
    if v_qr_code == "":
      print("Não há QRCode a ser mostrado por enquanto..")
      print("")
      input("Pressione qualquer tecla para continuar...")
    else:
      print(v_qr_code)
      print("")
      input("Pressione qualquer tecla para continuar...")
  #if 4


  #if erro
  else:
    os.system("clear")
    input("Opção Inválida! pressione qualquer tecla para continuar...")
  #if erro

os.system("clear")
print("Fim")
