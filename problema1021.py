num = float(input())

n100 = num // 100
n50 = num % 100 // 50
n20 = num % 100 % 50 // 20
n10 = num % 100 % 50 % 20 // 10
n5 = num % 100 % 50 % 20 % 10 // 5
n2 = num % 100 % 50 % 20 % 10 % 5 // 2
m1 = num % 100 % 50 % 20 % 10 % 5 % 2 // 1
m50 = num % 100 % 50 % 20 % 10 % 5 % 2 % 1 // 0.50
m25 = num % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 // 0.25
m10 = num % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 // 0.10
m05 = num % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 // 0.05
m01 = num % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01
print('''NOTAS:
{:.0f} nota(s) de R$ 100.00
{:.0f} nota(s) de R$ 50.00
{:.0f} nota(s) de R$ 20.00
{:.0f} nota(s) de R$ 10.00
{:.0f} nota(s) de R$ 5.00
{:.0f} nota(s) de R$ 2.00'''.format(n100, n50, n20, n10, n5, n2))
print('''MOEDAS:
{:.0f} moeda(s) de R$ 1.00
{:.0f} moeda(s) de R$ 0.50
{:.0f} moeda(s) de R$ 0.25
{:.0f} moeda(s) de R$ 0.10
{:.0f} moeda(s) de R$ 0.05
{:.0f} moeda(s) de R$ 0.01'''.format(m1, m50, m25, m10, m05, m01))
