#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from abstest import my_abs,move
from fun import hanoi
# print(my_abs('a'))

x,y = move(100,100,60,math.pi/6)
print(x,y)

hanoi(4,'A','B','C')