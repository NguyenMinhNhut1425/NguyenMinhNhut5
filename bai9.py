# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:53:30 2024

@author: MINH NHUT
"""
import math
a = float(input("Nhập vào giá trị của a: "))
b = float(input("Nhập vào giá trị của b: "))
a1 = math.sqrt(a)
a2 = math.sqrt(math.sqrt(a))
ab = math.sqrt(math.sqrt(a * b))
b1 = math.sqrt(b)
b2 = math.sqrt(math.sqrt(b))

x = ((a1 - b1) / (a2 - b2)) - ((a1 + ab) / (a2 + b2))
print(f"Giá trị biểu thức là: {x}")
