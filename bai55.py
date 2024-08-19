# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:18:55 2024

@author: MINH NHUT
"""

from datetime import datetime
nam = int(input("Nhập vào năm sinh: "))
hientai = datetime.now().year
tuoi = hientai - nam
print(f"Bạn sinh năm {nam} vậy bạn {tuoi} tuổi")