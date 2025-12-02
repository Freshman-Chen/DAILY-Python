''' 虚数的计算 '''
import decimal

x = 1 + 2j
y = 2 + 1j
z = x * y
print('x：')
print(x)
print('y：')
print(y)
print('z = x * y：')
print(z)

print('x的实部是：')
print(x.real)

print('x的虚部是：')
print(x.imag)
