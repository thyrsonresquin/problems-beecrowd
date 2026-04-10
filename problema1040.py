N1, N2, N3, N4 = map(float, input().split())
M1 = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print('Media: {:.1f}'.format(M1))
if M1 < 5:
    print('Aluno reprovado.')
elif M1 >= 7:
    print('Aluno aprovado.')
elif 5 <= M1 < 7:
    print('Aluno em exame.')
    E = float(input())
    M2 = (M1 + E) / 2
    print('Nota do exame: {}'.format(E))
    print('Aluno aprovado.')
    print('Media final: {:.1f}'.format(M2))
