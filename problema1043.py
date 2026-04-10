A, B, C = map(float, input().split())

perimetro = A + B + C
area = ((A + B) * C) // 2
if (abs(B - C) < A < (B + C)) or (abs(A - C) < B < (A + C)) or (abs(A - B) < C < (A + B)):
    print(f'Perimetro = {perimetro:.1f}')
else:
    print(f'Area = {area:.1f}')
