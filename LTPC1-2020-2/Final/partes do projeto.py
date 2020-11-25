#1 codigo para cada transaçao especifica, ao inves de qrcode, usar string.
#quando um usuario fizer um pagamento, o receptor recebera a informacao
#do valor e da string qrcode.

#cada usuario deve ter o usuario(q sera o nome dele), uma senha e um email.

#cada conta devera ter um ID e um saldo







xyz_teste_totalnomes = "Victor;ZéGotinha;Michellin;"

#for nomes in xyz_teste_totalnomes.split(";"):
#  print(nomes.upper())
#exibe os nomes tudo em maiusculo

xyz_continuar = True
while xyz_continuar == True:
  xyz_criarnomes = input("Digite um nome: ")
  xyz_add = xyz_criarnomes + ";"
  xyz_teste_totalnomes = xyz_teste_totalnomes + xyz_add
  print(xyz_teste_totalnomes.upper())
  input("Pressione qlqr tecla pra continuar...")
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
