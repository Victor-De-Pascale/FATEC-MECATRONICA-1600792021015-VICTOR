#1 codigo para cada transaçao especifica, ao inves de qrcode, usar string.
#quando um usuario fizer um pagamento, o receptor recebera a informacao
#do valor e da string qrcode.

#cada usuario deve ter o usuario(q sera o nome dele), uma senha e um email.

#cada conta devera ter um ID e um saldo





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
xyz_user_especifico = ""
xyz_total_caracteres = len(xyz_teste_totalnomes)
xyz_indicador = int(input("Indique a posição do ';' para mostrar usuario: "))
for caracter in xyz_teste_totalnomes:
  xyz_contador = xyz_contador + 1
  if caracter == ";":
    xyz_contador_pev = xyz_contador_pev + 1
    if xyz_contador_pev == (xyz_indicador - 1):
      xyz_posicao_inicial = xyz_contador
    if xyz_contador_pev == xyz_indicador:
      xyz_posicao_final = xyz_contador
xyz_usuario_especifico = xyz_teste_totalnomes[xyz_posicao_inicial:(xyz_posicao_final - 1)]
#print(xyz_usuario_especifico.upper())
#copiar e colar um nome especifico atraves da indicacao do ";"


os.system("clear")



#COMEÇA AQUI

v_users = ""
v_senhas = ""
v_emails = ""
v_saldos = ""
v_ids = ""

#incompleto
def f_menu():
  print("Bem vindo ao banco virtual! Escolha Uma opção para continuar: ")
  print("1- Criar/Adicionar Usuário")
  print("2- Requerir transação")
  print("3- Pagar transação")
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
      
      var_add_id = var_criar_nomes.upper() + ("000%.i" % var_contador_usuario) + ";"
      v_ids = v_ids + var_add_id
    
      print(v_users)
      print(v_emails)
      print(v_senhas)
      print(v_saldos)
      print(v_ids)
    
      input("Pressione qlqr tecla pra continuar...")
      os.system("clear")
      xyz_op = input("Deseja continuar adicionando nomes? (s/n) ")
      if xyz_op != "s":
        cf_continuar = False
    
  
  elif d_op == 0:
    c_fim_do_programa = True

os.system("clear")
print(v_users)
print(v_emails)
print(v_senhas)
print("Fim")
