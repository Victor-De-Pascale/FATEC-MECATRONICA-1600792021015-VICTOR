def xyz_add_estoque():
  xyz_p1 = input("Nome do Produto: ")
  xyz_p2 = input("Quantidade: ")
  xyz_p3 = input("Preço do Produto: ")
  xyz_p_completo = [] 
  xyz_p_completo.append(xyz_p1)
  xyz_p_completo.append(xyz_p2)
  xyz_p_completo.append(xyz_p3)
  #tem q ser um de cada vez ¬¬
  return xyz_estoque.append(xyz_p_completo)

xyz_existe_produto = False
xyz_add_produto = True
xyz_estoque = []

while xyz_add_produto == True:
  xyz_resp = input("Deseja adicionar produtos ao estoque? (s/n) ")
  if xyz_resp == "s" or xyz_resp == "S":
    xyz_add_estoque()
    xyz_existe_produto = True
  else:
    xyz_add_produto = False

#print(xyz_estoque)

if xyz_existe_produto == True:
  print("existe!")
else:
  print("fim!")
