uurloon = input('wat verdien je per uur: ')
aantalUur = input('hoeveel uur heb je gewerkt: ')

salaris = (float(uurloon) * float(aantalUur))

print('%.1f uur werken levert %.2f Euro op' %(float(aantalUur), float(salaris)))