# for i in range(1, 8):
#     print('*' * i
x = str(input('sign='))
maxLength = int(input('max Length='))
for i in range(1, maxLength):
    print(x * i)

print('\n')
print('\n')
print('\n')

s = 0
k = 30
d = k - 5
k = 2 * d
s = k - 100
print('s=', s)

print('\n')
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)
