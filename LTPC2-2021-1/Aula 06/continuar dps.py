exer_1 = True
exer_2 = False

while exer_2 == True:  
  t_arquivo = float(input("Tamanho do arquivo (MB) "))
  d_velocidade = float(input("Velocidade de download (Mbps) "))

  tempo_total = (((t_arquivo * 8) / d_velocidade) / 60)

  print(f"Tempo de download em minutos: {tempo_total}")
  break

while exer_1 == True:
  area_pintar = float(input("Area total em metros quadrados a ser pintada: "))
  
