x = int(input())

horas = x // 3600
minutos = (x % 3600) // 60
segundos = ((x % 3600) % 60)
print('{}:{}:{}'.format(horas, minutos, segundos))
