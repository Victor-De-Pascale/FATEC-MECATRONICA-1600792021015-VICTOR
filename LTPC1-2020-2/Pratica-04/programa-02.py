#Verificacao de senha
senha_secreta = '123456'

senha = input('Informe a sua senha: ')

if senha == senha_secreta:
  print('Bem vindo User')

if senha != senha_secreta:
  print('Acesso negado')
