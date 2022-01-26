# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import pywhatkit as kit
import cv2

name_file = str(input("[*]Please, digit the name of file you want create ? : "))
text = str(input("[*]Please, digit the text of file you want create ? : "))
name_file = name_file + '.png'

kit.text_to_handwriting(text,name_file, [0,0,138])
img = cv2.imread(name_file)
cv2.imshow("Converted Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()