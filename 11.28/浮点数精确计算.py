''' 准确的进行浮点数计算 '''
import decimal

a = decimal.Decimal("0.1")
b = decimal.Decimal('0.2')
print("a = 0.1,b = 0.2")

print("a + b = ?")
print(a + b)

c = decimal.Decimal('0.3')
print("c = 0.3,a + b == c?")
print(a + b == c)

print("0.1 + 0.2 == 0.3 ？")
print(0.1 + 0.2 == 0.3)
print("0.1 + 0.2 =?")
print(0.1 + 0.2)
