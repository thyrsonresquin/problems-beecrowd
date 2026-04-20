salario = float(input())

if 0 < salario <= 400:
    reajuste = salario * 0.15
    novo_salario = salario + reajuste
    porcentagem = 15
elif 400 < salario <= 800:
    reajuste = salario * 0.12
    novo_salario = salario + reajuste
    porcentagem = 12
elif 800 < salario <= 1200:
    reajuste = salario * 0.1
    novo_salario = salario + reajuste
    porcentagem = 10
elif 1200 < salario <= 2000:
    reajuste = salario * 0.07
    novo_salario = salario + reajuste
    porcentagem = 7
else:
    reajuste = salario * 0.04
    novo_salario = salario + reajuste
    porcentagem = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {porcentagem} %')
