num = int(input())

ano = num // 365
mes = (num % 365) // 30
dia = (num % 365) % 30

print('{:.0f} ano(s)'.format(ano))
print('{:.0f} mes(es)'.format(mes))
print('{:.0f} dia(s)'.format(dia))
