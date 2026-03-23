from math import trunc

a, b, c = map(int, input().split())

MaiorAB = (a + b + abs(a - b)) / 2
MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) / 2

print('{} eh o maior'.format(trunc(MaiorABC)))
