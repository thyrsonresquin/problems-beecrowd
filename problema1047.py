h_inicial, m_inicial, h_final, m_final = map(int, input().split())

i_minutos = (h_inicial * 60) + m_inicial
f_minutos = (h_final * 60) + m_final

if f_minutos <= i_minutos:
    total_minutos = (1440 - i_minutos) + f_minutos
else:
    total_minutos = f_minutos - i_minutos

if total_minutos == 0:
    total_minutos - 1440

horas = total_minutos // 60
minutos = total_minutos % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
