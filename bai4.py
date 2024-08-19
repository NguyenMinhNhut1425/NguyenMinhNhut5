# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:12:43 2024

@author: MINH NHUT
"""

thoi_gian = input("Nhập giờ, phút, giây theo định dạng hh:mm:ss : ")
hh, mm, ss = map(int, thoi_gian.split(':'))
tong_giay = hh * 3600 + mm * 60 + mm
print(f"tổng số giây là: {tong_giay}")