hi, hf = map(int, input().split())

hora = 24 - hi + hf
if hf > hi:
    hora = hf - hi

print(f'O JOGO DUROU {hora} HORA(S)')
