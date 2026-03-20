c1, u1, v1 = map(float, input().split())
c2, u2, v2 = map(float, input().split())

t1 = u1 * v1
t2 = u2 * v2
t = t1 + t2

print('VALOR A PAGAR: R$ {:.2f}'.format(t))
