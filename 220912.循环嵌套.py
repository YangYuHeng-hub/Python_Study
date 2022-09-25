'''
循环嵌套：

while循环：
****
****
****
****

*
**
***
****
*****
'''

# n = 0
# while n < 5:
#     print('*' * (n+1))
#     n += 1

# n = 1
# while n <= 5:
#     m = 0
#     while m < n:
#         print('*', end='')
#         m += 1
#     print()
#     n += 1

'''
*****
****
***
**
*
'''

# n = 5
# while n > 0:
#     m = 0
#     while m < n:
#         print('*', end='')
#         m += 1
#     n -= 1
#     print()
#
# for i in range(5):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
#
# for i in range(5):
#     for j in range(5 - i):
#         print('*', end='')
#     print()

for i in range(0, 5, 2):
    print(' ' * ((5 - i) // 2), end='')
    for j in range(i + 1):
        print('*', end='')
    print()
