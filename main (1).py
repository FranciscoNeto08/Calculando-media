print('Calculador de média')
print("Coloque aqui a média dos seus alunos!")

m1 = float(input('Coloque aqui a média do primeiro bimestre!'))
m2 = float(input('Coloque aqui a média do segundo bimestre!'))  
m3 = float(input('Coloque aqui a média do terceiro bimestre!')) 
m4 = float(input('Coloque aqui a média do quarto bimestre!')) 
media = ((m1+m2+m3+m4) /4)
print(" A média do aluno é", ((m1+m2+m3+m4) /4))

if media <= 6.9999999:
  print("Reprovou!")
elif media >= 7:
  print("Aprovado!")

