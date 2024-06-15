minimo = 7
presencaMin = 75
presencaMax = 100
nota = int(input('Informe a nota da aluna de 01 a 10: '))
presenca = float(input('Informe a presença da aluna entre 01% e 100%: '))
if nota >= minimo and presenca >= presencaMin:
    print('A aluna foi APROVADA!')
else:
    print('A aluna foi REPROVADA!')