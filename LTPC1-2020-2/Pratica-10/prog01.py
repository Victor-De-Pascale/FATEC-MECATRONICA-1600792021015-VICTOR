def lerNumeroPositivo():
  continuar = True
  while continuar==True:
    numero = int(input("Informe um valor:"))
    continuar = numero < 0 #condicao q o torna falso
  return numero

primeiro_valor = lerNumeroPositivo()
segundo_valor = lerNumeroPositivo()
resposta = primeiro_valor + segundo_valor
print("A soma de", primeiro_valor, " com ", segundo_valor, " é igual:", resposta)

#Apenas somar 2 numeros se positivos
