while c_login == False:
  v_user, v_senha = f_user()
  c_login = f_verify(v_user, v_senha)
  if c_login == False:
    print("Usuário incorreto!")
    v_resp = input("Deseja continuar? (s/n): ")
    os.system("clear")
    if v_resp == "n":
      c_login = True
      c_continuar = False
      print("Ação cancelada!")
  else:
    print("Login feito!")
    input("Pressione qualquer tecla para continuar...")
