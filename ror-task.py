'''
Напиши на любом языке программирования метод,
который в качестве аргумента принимает N и возвращает "x".
Где "x" – наименьшая целая степень числа два,
при котором два в степени "x" больше чем N.
'''

import math


n = int(input())

class Task2:

    def power_method(n):
        '''Solution method using power'''
        two = 2
        x = 1
        while two <= n:
            two *= 2
            x += 1
        return x

    def math_method(n):
        '''Solution method using math module'''
        x = int(math.log2(n) + 1)
        return x

    def shift_method(n):
        '''Solution method using shift'''
        x = 0
        if (n and not(n & (n - 1))):
            return n
        while n != 0:
            n >>= 1
            x += 1
        return x

print(Task2.power_method(n))
print(Task2.math_method(n))
print(Task2.shift_method(n))
