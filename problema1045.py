import math

C, B, A = sorted(list(map(float, input().split())))

if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if pow(A, 2) == pow(B, 2) + pow(C, 2):
        print('TRIANGULO RETANGULO')
    elif pow(A, 2) > pow(B, 2) + pow(C, 2):
        print('TRIANGULO OBTUSANGULO')
    elif pow(A, 2) < pow(B, 2) + pow(C, 2):
        print('TRIANGULO ACUTANGULO')


if A == B == C:
    print('TRIANGULO EQUILATERO')
elif A == B or A == C or B == A or B == C or C == A or C == B:
    print('TRIANGULO ISOSCELES')
