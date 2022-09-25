'''
二进制：0,1
八进制：0,1,2,3,4,5,6,7
十进制：0~9
十六进制：0~9 a~f

十进制转二进制
10---->二进制表示，1010
'''

n=128
#二进制
binary = bin(n)

#八进制
octonary = oct(n)

#十六进制
hexadecimal = hex(n)
print(binary)
print(octonary)
print(hexadecimal)

#前缀：0b：二进制  0o：八进制  0x：十六进制  默认十进制

'''
各进制又如何转换成十进制？
各进制之间又如何相互转换？
'''
n = 0x231
#int base参数默认10，即10进制
result = int(n)
print(result)
print(n)
print(bin(n))
print(oct(n))