#! /usr/bin/env python
#coding=GB18030
import time
import pyautogui
import Common.Init as init
import Common.auto_lib as pywin
import Common.getPos as getPos
import Common.setup as setup
import Common.fillValue as fill
import Common.lxmlReader as xmlReader
import Common.readConifg as readConfig
list=readConfig.readIniConifg('Power')
init.check_exist(list[2])

pos=setup.setUp()
x=pos[0]
y=pos[1]
pyautogui.click(x, y)
 
conf_x=getPos.get_pos(403, 34)[0]
conf_y=getPos.get_pos(403, 34)[1]
pyautogui.click(conf_x, conf_y)         #打开校准页面
 
app = pywin.Pywin()
window_name = list[0]
app.connect(window_name)

file=list[1]+'\\config\\config.xml'
# file=ur"E:\模拟\ReleaseV1.02_20190315\config\config.xml"      
s=open(file,'r')
str1=s.read()
dom=xmlReader.lxmlReader(str1)
cardList=dom.getTabNodeValue('//battery/@cardtype')
s.close()
dic={}
for i in range(15):
    key='cardNo'+str(i)
    value=cardList[0][i]
    dic[key]=value
# print dic

for i in range(15):
    pyautogui.click(208,191)                      #选择卡号
    time.sleep(1)
    if i != 0:
        app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
    card='cardNo'+str(i)
    if dic[card] != 2:                          #选择板卡类型，板卡类型为电压卡、电阻卡
#     for t in range(2):
        pyautogui.click(214,227)                 
#         if i != 0:
        print int(dic[card])
        time.sleep(1)
        
        if int(dic[card]) == 1:
            time.sleep(1)
            app.Sendk('DOWN', 1)
            time.sleep(1)
            app.Sendk('ENTER',1)
            time.sleep(2)
        else:
            app.Sendk('UP', 1)            
            time.sleep(1)
            app.Sendk('ENTER',1)
            time.sleep(2)
            pyautogui.click(188,271)
            fill.fill_vVal(188, 271, 5, 5)      #设置通道1基准电压
            fill.fill_vVal(188, 309, 5, 5)      #设置通道2基准电压
            fill.fill_vVal(188, 346, 5, 5)      #设置通道3基准电压
        time.sleep(1)

         
        pyautogui.click(290,685)                #读板卡信息
#         time.sleep(1)
        pyautogui.click(397,681)                #设置
        time.sleep(5)
#         
        
