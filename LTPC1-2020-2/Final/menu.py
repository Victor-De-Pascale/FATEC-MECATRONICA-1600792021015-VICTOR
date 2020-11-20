while c_continuar == True:
  os.system("clear")
  f_menu()
  v_opcao = int(input("Opção: "))
  if v_opcao == 0:
    c_continuar = False
  else:
    print("Opção inválida")
    input("Pressione qualquer tecla para continuar")
