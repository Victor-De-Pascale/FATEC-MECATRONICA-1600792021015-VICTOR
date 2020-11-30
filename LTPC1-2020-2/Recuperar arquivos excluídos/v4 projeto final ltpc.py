#1 codigo para cada transaçao especifica, ao inves de qrcode, usar string.
#quando um usuario fizer um pagamento, o receptor recebera a informacao
#do valor e da string qrcode.






import os

xyz_teste_totalnomes = "Victor;ZéGotinha;Michellin;"

#for nomes in xyz_teste_totalnomes.split(";"):
#  print(nomes.upper())
#exibe os nomes tudo em maiusculo

xyz_continuar = False
while xyz_continuar == True:
  xyz_criarnomes = input("Digite um nome: ")
  xyz_add = xyz_criarnomes + ";"
  xyz_teste_totalnomes = xyz_teste_totalnomes + xyz_add
  print(xyz_teste_totalnomes.upper())
  input("Pressione qlqr tecla pra continuar...")
  os.system("clear")
  xyz_op = input("Deseja continuar adicionando nomes? (s/n) ")
  if xyz_op != "s":
    xyz_continuar = False
#adicionar usuarios ate cansar

#xyz_contador_usuario = 0
#for caracter in xyz_teste_totalnomes:
#  if caracter == ";":
#    xyz_contador_usuario = xyz_contador_usuario + 1
#print(" ")
#print(" ")
#print(" ")
#print("Existem %.i usuarios" % (xyz_contador_usuario))
#contador de usuarios

os.system("clear")
xyz_posicao_inicial = 0
xyz_posicao_final = 0
xyz_contador_pev = 0
xyz_contador = 0
#xyz_indicador = int(input("Indique a posição do ';' para mostrar usuario: "))


xyz_indicador = 2


for caracter in xyz_teste_totalnomes:
  xyz_contador = xyz_contador + 1
  if caracter == ";":
    xyz_contador_pev = xyz_contador_pev + 1
    if xyz_contador_pev == (xyz_indicador - 1):
      xyz_posicao_inicial = xyz_contador
    if xyz_contador_pev == xyz_indicador:
      xyz_posicao_final = xyz_contador
xyz_usuario_especifico = xyz_teste_totalnomes[xyz_posicao_inicial:(xyz_posicao_final - 1)]
print(xyz_usuario_especifico.upper())
#copiar e colar um nome especifico atraves da indicacao do ";"











abc_valores = "7000;5000;3500;2000;10000;"

os.system("clear")
abc_posicao_inicial = 0
abc_posicao_final = 0
abc_contador_pev = 0
abc_contador = 0
abc_existe = True

while abc_existe == False:
  abc_indicador = int(input("Indique a posição do ';' para mostrar valor: "))
  abc_contador_while = 0
  for abc_caracter in abc_valores:
    if abc_caracter == ";":
      abc_contador_while = abc_contador_while + 1
  if abc_indicador > abc_contador_while:
    abc_existe = False
    print("nao existe")
    input("")
  else:
    abc_existe = True
    print("existe")
    input("")

abc_posicao_inicial_dois = 0
abc_posicao_final_dois = 0
abc_contador_pev_dois = 0
abc_contador_dois = 0
abc_existe_dois = True

while abc_existe_dois == False:
  abc_indicador_dois = int(input("Agora o segundo valor: "))
  abc_contador_while_dois = 0
  for abc_caracter_dois in abc_valores:
    if abc_caracter_dois == ";":
      abc_contador_while_dois = abc_contador_while_dois + 1
  if abc_indicador_dois > abc_contador_while_dois:
    abc_existe_dois = False
    print("nao existe")
    input("")
  else:
    abc_existe_dois = True
    print("existe")
    input("")

#tirar isso aqui
abc_indicador = 2
abc_indicador_dois = 2


for caracter in abc_valores:
  abc_contador = abc_contador + 1
  if caracter == ";":
    abc_contador_pev = abc_contador_pev + 1
    if abc_contador_pev == (abc_indicador - 1):
      abc_posicao_inicial = abc_contador
    if abc_contador_pev == abc_indicador:
      abc_posicao_final = abc_contador

abc_valor_especifico_um = abc_valores[abc_posicao_inicial:(abc_posicao_final - 1)]
#print(abc_valor_especifico_um)
#input(" ")

for caracter in abc_valores:
  abc_contador_dois = abc_contador_dois + 1
  if caracter == ";":
    abc_contador_pev_dois = abc_contador_pev_dois + 1
    if abc_contador_pev_dois == (abc_indicador_dois - 1):
      abc_posicao_inicial_dois = abc_contador_dois
    if abc_contador_pev_dois == abc_indicador_dois:
      abc_posicao_final_dois = abc_contador_dois

abc_valor_especifico_dois = abc_valores[abc_posicao_inicial_dois:(abc_posicao_final_dois - 1)]
#print(abc_valor_especifico_dois)
#input(" ")

#abc_soma = int(abc_valor_especifico_um) + int(abc_valor_especifico_dois)
#abc_sub = int(abc_valor_especifico_um) - int(abc_valor_especifico_dois)
#abc_mult = int(abc_valor_especifico_um) * int(abc_valor_especifico_dois)

#print(abc_soma)
#print(abc_sub)
#print(abc_mult)
#input("")

#substituiçao em si
c_existe = True
while c_existe == False:
  c_count = 0
  c_count_pev = 0
  c_com = 0
  c_fim = 0
  c_ind = int(input("digite qual valor (ordinal) ele ira substituir: "))
  for caracter in abc_valores:
    c_count = c_count + 1
    if caracter == ";":
      c_count_pev = c_count_pev + 1
      if c_count_pev == (c_ind - 1):
        c_com = c_count
      if c_count_pev == c_ind:
        c_fim = c_count
  if c_ind > c_count_pev:
    c_existe = False
    print("nao existe")
    input("")
  else:
    c_existe = True
    print("existe")
    print(abc_valores[c_com:(c_fim - 1)])
    input("")
    os.system("clear")
    print("antes")
    print(abc_valores)

    
    #abc_valores[c_com:(c_fim - 1)]

    
    for valor in abc_valores.split(';'):
      if valor == abc_valores[c_com:(c_fim - 1)]:
        print(valor)
        input("encontrei")
      else:
        input("nao encontrei")




#fazer contas com valores especificos localizados numa string e substitui-los na mesma




os.system("clear")



#COMEÇA AQUI

v_users = ""
v_senhas = ""
v_emails = ""
v_saldos = ""
v_ids = ""
v_qr_code = ""

#incompleto
def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Criar/Adicionar Usuário")
  print("2- Enviar transação")
  print("3- Receber transação")
  print("0- Sair")

#main
c_fim_do_programa = False
while c_fim_do_programa == False:
  os.system("clear")
  f_menu()
  d_op = int(input("Digite uma das opcoes abaixo: "))
  
  if d_op == 1:
    os.system("clear")
    cf_continuar = True
    while cf_continuar == True:
      var_criar_nomes = input("Digite o nome do usuario: ")
      var_criar_senhas = input("Digite a senha para este usuario: ")
      var_criar_saldos = input("Saldo inicial deste usuario: ")
    
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
    
      print(v_users)
      print(v_emails)
      print(v_senhas)
      print(v_saldos)
      print(v_ids)
    
      input("Pressione qlqr tecla pra continuar...")
      os.system("clear")
      xyz_op = input("Deseja continuar adicionando usuarios? (s/n) ")
      if xyz_op != "s":
        cf_continuar = False
    
  
  elif d_op == 0:
    c_fim_do_programa = True

  else:
    os.system("clear")
    input("Opção Inválida! pressione qualquer tecla para continuar...")

os.system("clear")
#print(v_users)
#print(v_emails)
#print(v_senhas)
print("Fim")
