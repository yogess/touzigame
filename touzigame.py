# -*- coding: utf-8 -*-
"""
2017-10-19 18:25:23
使用random库，制作掷骰子猜大小游戏。
@author: liqian
"""
import random as rd

def xiazhu():
    
    yourChoice=int(input("请下注（1代表大或0代表小）"))
    if yourChoice==1:
        yours="big"
        return yours
    elif yourChoice==0:
        yours="small"
        return yours
    else:
        print("请重新下注！")
        xiazhu()
        
def touzi_game():
    #print("》》》》游戏开始《《《《")
    num_dice=int(input("请输入想使用筛子的数量,最多为6个"))
    if num_dice <=0:
        print("筛子数量不能为0")
        touzi_game()
    elif num_dice>6:
        print("筛子最多为6个")
        touzi_game()
    else:
        print("掷筛子游戏:{}个筛子！".format(num_dice))
        midNum=(num_dice*6)/2
        print("游戏规则如下：")
        print("大于等于{}为大，小余{}为小)".format(midNum,midNum))
        yours=xiazhu()
        print("你的下注是:",yours)
        point_list=[0]*num_dice
        count=0
        while True:
            point_list[count]=rd.randrange(1,6)
            count=count+1
            if count>num_dice-1:
                break
      #  for p in range(0,num_dice-1):
       #     point_list[p]=int(rd.randrange(1,6))
        for n in range(0,num_dice):
            print("骰子{}是{}".format(n+1,point_list[n]))
        
        sum_point=sum(point_list)
        
        if sum_point>=midNum:
            result="big"
        else:
            result="small"
            
        print("总点数是",sum_point,result)
        
        if yours=="small":
            if result=="big":
                print("you lose")
                start()
            else:
                print("you win")
                start()
        else:
            if result=="big":
                print("you win")
                start()
            else:
                print("you lose")
                start()
def start():
    jixu=int(input("继续玩游戏吗？（1是继续，0是结束）"))
   # print(type(jixu))
    if jixu==1:
        print("》》》》游戏开始《《《《")
        touzi_game()
    else:
        print("欢迎再来！")
        
start()
