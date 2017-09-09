letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')


ltrCounta = letters.count('A')
ltrCountb = letters.count('B')
ltrCountc = letters.count('C')

ltrCount = [ltrCounta, ltrCountb, ltrCountc]

ltrCount.sort()

print(ltrCount)