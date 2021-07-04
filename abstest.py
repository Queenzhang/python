#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)  
    # 用游戏中的坐标计算，而游戏用的坐标系多为屏幕坐标系，而不是我们平时数学计算的笛卡尔坐标系。屏幕坐标系为显示器的平面坐标系，它的坐标原点位于屏幕的左上角，水平向右为X轴正方向，垂直向下为Y轴正方向，以像为单位。任何物体的基点坐标最终都要转化为屏幕坐标系中的坐标来进行显示。
    return nx,ny