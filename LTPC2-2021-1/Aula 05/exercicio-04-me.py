def xyz_add_estoque():
  xyz_p1 = input("Nome do Produto: ").upper()
  xyz_p2 = int(input("Quantidade: "))
  xyz_p3 = float(input("Preço do Produto: "))
  #tem q ser um de cada vez ¬¬
  return xyz_estoque.append(xyz_p1), xyz_qtde.append(xyz_p2), xyz_preco.append(xyz_p3)

xyz_existe_produto = False
xyz_add_produto = True
xyz_menu_user = False
xyz_estoque = []
xyz_qtde = []
xyz_preco = []
xyz_lucro_total = 0

while xyz_add_produto == True:
  xyz_resp = input("Deseja adicionar produtos ao estoque? (s/n) ")
  if xyz_resp == "s" or xyz_resp == "S":
    xyz_add_estoque()
    xyz_existe_produto = True
    xyz_menu_user = True
  else:
    xyz_add_produto = False

#MENU PARA USER FAZER COMPRA
while xyz_menu_user == True:
  xyz_user_resp = input("Gostaria de realizar uma compra? (s/n) ")
  if xyz_user_resp == "s" or xyz_resp == "S":
    xyz_v_prod = input("Insira o nome do produto que deseja: ").upper()
    if xyz_v_prod in xyz_estoque:
      if xyz_qtde[xyz_estoque.index(xyz_v_prod)] > 0:
        xyz_sair = False
        while xyz_sair == False:
          xyz_v_qtde = int(input("Digite a quantidade: "))
          if xyz_v_qtde > xyz_qtde[xyz_estoque.index(xyz_v_prod)]:
            print("Quantidade acima do limite!")
          else:
            xyz_sair = True
        #AS MECANICAS AQUI ESTAO
        xyz_lucros = xyz_v_qtde * xyz_preco[xyz_estoque.index(xyz_v_prod)]
        xyz_lucro_total = xyz_lucro_total + xyz_lucros
        xyz_qtde[xyz_estoque.index(xyz_v_prod)] = xyz_qtde[xyz_estoque.index(xyz_v_prod)] - xyz_v_qtde
        #AS MECANICAS AQUI ESTAO
      else:
        print("Produto não está mais disponivel!")
    else:
      print("Não existe o produto indicado!")
  else:
    xyz_menu_user = False

if xyz_existe_produto == True:
  print("Lucros totais da compra: R$%.2f" % (xyz_lucro_total))
else:
  print("fim!")
