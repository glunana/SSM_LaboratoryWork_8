print('G = {V, T, S0, P}')
print('V = {S0, S1, S2, S3}')
print('T = {0,1}')
print('S0 – початковий елемент')
print('P = {S0 -> 0S1, S0 -> 1S1, S1 -> 0S1, S1 -> 1S2, S2 -> 1S2, S2 -> 0S3, S3 -> 0S3, S3 -> 0S3}')
print("Таблиця переходів:")
print("|----------------------------|")
print("|        |        Вхід       |")
print("|  Стан  |-------------------|")
print("|        |    0    |    1    |")
print("|--------|-------------------|")
print("|   S0   |   S1    |   S1    |")
print("|--------|-------------------|")
print("|   S1   |   S1    |   S2    |")
print("|--------|-------------------|")
print("|   S2   |   S3    |   S2    |")
print("|--------|-------------------|")
print("|   S3   |   S3    |   S3    |")
print("|--------|-------------------|")