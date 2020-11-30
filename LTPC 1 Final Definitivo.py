#COMEÇA AQUI

v_users = ""
v_senhas = ""
v_emails = ""
v_saldos = ""
v_ids = ""
v_qr_code = ""
valor_rec = ""
import os
import random

def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Criar/Adicionar Usuário")
  print("2- Enviar transação")
  print("3- Pedir transação")
  print("4- Exibir QRCode (ADMIN)")
  print("5- Exibir saldos (ADMIN)")
  print("6- Exibir usuários, emails e ID's (ADMIN)")
  print("0- Sair")
  print("")

#main
c_fim_do_programa = False
while c_fim_do_programa == False:
  os.system("clear")
  f_menu()
  d_op = int(input("Digite uma das opções acima: "))
  
  #if 1
  if d_op == 1:
    os.system("clear")
    cf_continuar = True
    while cf_continuar == True:
      os.system("clear")
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
      os.system("clear")
      print("Usuário cadastrado com sucesso!")
      input("Continuar...")
      os.system("clear")
      xyz_op = input("Deseja continuar cadastrando usuarios? (s/n) ")
      if xyz_op != "s":
        cf_continuar = False
  #if 1  
  

  #if 2
  elif d_op == 2:
    os.system("clear")
    if v_qr_code == "":
      print("Não há requisição de pagamento")
      input("Pressione qualquer tecla pra continuar...")
    else:
      os.system("clear")
      V_pagador_existe = False
      valida_pagador = input("Indique o nome do usuário pagador: ")
      valida_pagador = valida_pagador.upper()

      c_count = 0
      for nomes in v_users.split(';'):
        c_count = c_count + 1
        if valida_pagador == nomes:
          V_pagador_existe = True
          c_indicador_id = c_count
      
      v_pagador_receptor_igual = False
      for partes in v_qr_code.split(";"):
        if valida_pagador == partes:
          v_pagador_receptor_igual = True

      if v_pagador_receptor_igual == True:
        os.system("clear")
        print("Usuário pagante não pode ser igual ao receptor!")
        print("Então, a ação de pagamento foi cancelada!")
        input("Pressione qualquer tecla pra continuar...")
      else:
        if V_pagador_existe == True:
          c_inicial = 0
          c_final = 0
          c_pev = 0
          c_count = 0
          for caracter in v_saldos:
            c_count = c_count + 1
            if caracter == ";":
              c_pev = c_pev + 1
              if c_pev == (c_indicador_id - 1):
                c_inicial = c_count
              if c_pev == c_indicador_id:
                c_final = c_count
          valida_saldo = v_saldos[c_inicial:(c_final - 1)]

          if int(valida_saldo) < int(valor_rec):
            os.system("clear")
            print("Verificamos o sistema e parece que o usuário %s não possui saldo suficiente para pagar o valor pedido." % (valida_pagador))
            print("Então, a ação de pagamento foi cancelada!")
            input("Pressione qualquer tecla pra continuar...")
          else:
            os.system("clear")
            valida_receptor = input("Indique o nome do receptor: ")
            valida_receptor = valida_receptor.upper()
          
            v_receptor_existe = False
            for partes in v_qr_code.split(";"):
              if valida_receptor == partes:
                v_receptor_existe = True

            if v_receptor_existe == False:
              print("Usuario receptor incorreto!")
              print("Então, a ação de pagamento foi cancelada!")
              input("Pressione qualquer tecla pra continuar...")
            else:
              os.system("clear")
              valida_qr_code = input("Pagamento quase finalizado! Digite o QRCode para realizá-lo: ")
              valida_qr_code = valida_qr_code.upper()
              if valida_qr_code != v_qr_code:
                os.system("clear")
                print("QRCode incorreto!")
                print("Então, a ação de pagamento foi cancelada!")
                input("Pressione qualquer tecla pra continuar...")
              else:
                rec_id = int(v_qr_code[0])
                c_inicial = 0
                c_final = 0
                c_pev = 0
                c_count = 0
                for valores in v_saldos:
                  c_count = c_count + 1
                  if valores == ";":
                    c_pev = c_pev + 1
                    if c_pev == (rec_id - 1):
                      c_inicial = c_count
                    if c_pev == rec_id:
                      c_final = c_count
                valor_saldo_rec = v_saldos[c_inicial:(c_final - 1)]

                novo_valor_pagante = int(valida_saldo) - int(valor_rec) #substitui o valor do saldo do PAGANTE
                novo_valor_receptor = int(valor_saldo_rec) + int(valor_rec) #substitui o valor do saldo do RECEPTOR

                v_substituicao = v_saldos.replace(valida_saldo, str(novo_valor_pagante))
                v_saldos = v_substituicao
                v_substituicao = v_saldos.replace(valor_saldo_rec, str(novo_valor_receptor))
                v_saldos = v_substituicao
                v_qr_code = ""

                os.system("clear")
                print("Pagamento realizado com sucesso...")
                print("")
                input("Pressione qualquer tecla pra continuar...")

        else:
          os.system("clear")
          print("Usuário não existe!")
          print("")
          input("Pressione qualquer tecla pra continuar...")
  #if 2


  #if 3
  elif d_op == 3:
    if v_qr_code == "" and v_users != "":
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
      print("Anote-o com cuidado!")
      input("Continuar....")

    else:
      os.system("clear")
      print("Ja existe um pedido em andamento ou não existem usuários cadastrados ainda! Impossível fazer outro requerimento no momento!")
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


  #if 5
  elif d_op == 5:
    os.system("clear")
    if v_saldos == "":
      print("Não existem saldos a serem mostrados por enquanto..")
      print("")
      input("Continuar...")
    else:
      print(v_saldos)
      print("")
      input("Continuar...")
  #if 5


  #if 6
  elif d_op == 6:
    os.system("clear")
    if v_users == "":
      print("Não há usuários cadastrados por enquanto..")
      print("")
      input("Continuar...")
    else:
      print(v_users)
      print(v_emails)
      print(v_ids)
      print("")
      input("Continuar...")
  #if 6


  #if erro
  else:
    os.system("clear")
    input("Opção Inválida! pressione qualquer tecla para continuar...")
  #if erro

os.system("clear")
print("Fim")
