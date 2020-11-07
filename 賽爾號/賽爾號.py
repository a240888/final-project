class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


def phydmg(power,atk,defense,counter):
    """物攻傷害"""
    result = (int)(42*power*atk/defense/50+2*1.5*counter*(217-255)/255)
    return result
def magdmg(power,magatk,magdefense,counter):
    """魔攻傷害"""
    result = (int)(42*power*magatk/magdefense/50+2*1.5*counter*(217-255)/255)
    return result
global haskill
haskill='1:龍之意志 2:迴避 3:龍王波 4:龍王滅碎陣'
def 哈莫雷特技能():
    n=int(input('輸入技能編號: '))
    for case in switch(n):
        if case(int(1)):
            print ('龍之意志:100%改變自身攻擊、防御、特攻、特防、速度等级1')
            break
        if case(int(2)):
            print ('迴避:回合本方先手攻擊，使得對方的技能失效')
            break
        if case(int(3)):
            print ('龍王波:必定命中對方')
            break
        if case(int(4)):
            print ('龍王滅碎陣:5%令對方疲憊，1回合無法攻擊')
            break
        if True: 
            print ("幹叫你輸入編號")
            哈莫雷特技能()
            break
global loskill
loskill='1:幻化之火 2:火之意志 3:灼燒 4:天火鳳凰'
def 羅特利斯技能():
    n=int(input('輸入技能編號: '))
    for case in switch(n):
        if case(int(1)):
            print ('幻化之火:命中后100%令對手睡眠')
            break
        if case(int(2)):
            print ('火之意志:100%改變自身特攻等级2')
            break
        if case(int(3)):
            print ('灼燒:命中後100%令對方燒傷')
            break
        if case(int(4)):
            print ('天火鳳凰:15%改變自身特攻等級1')
            break
        if True: 
            print ("幹叫你輸入編號")
            羅特利斯技能()
            break
global moskill
moskill='1:覺醒 2:絕命火焰 3:全力一擊 4:火焰漩渦'
def 魔焰猩猩技能():
    n=int(input('輸入技能編號: '))
    for case in switch(n):
        if case(int(1)):
            print ('覺醒:100%改變自身攻擊、特攻等級2')
            break
        if case(int(2)):
            print ('絕命火焰:命中時5%的概率秒殺對方')
            break
        if case(int(3)):
            print ('全力一擊:就很用力阿')
            break
        if case(int(4)):
            print ('火焰漩渦:命中後100%令對方燒傷')
            break
        if True: 
            print ("幹叫你輸入編號")
            魔焰猩猩技能()
            break
global saskill
saskill='1:相位移動 2:精神強化 3:樂鏡迷蹤 4:淨化街'
def 薩帕克技能():
    n=int(input('輸入技能編號: '))
    for case in switch(n):
        if case(int(1)):
            print ('相位移動:若本回合先手，對方技能失效')
            break
        if case(int(2)):
            print ('精神強化:技能使用成功時，100%改變自身特攻等級2')
            break
        if case(int(3)):
            print ('樂鏡迷蹤:10%改變對方攻擊等級-1')
            break
        if case(int(4)):
            print ('淨化街:清除對方能力提升的效果')
            break
        if True: 
            print ("幹叫你輸入編號")
            薩帕克技能()
            break
global caskill
caskill='1:寄生種子 2:催眠粉 3:硬化 4:疾風快刀'
def 卡利斯技能():
    n=int(input('輸入技能編號: '))
    for case in switch(n):
        if case(int(1)):
            print ('寄生種子:每回合吸取對方最大體力1/8並補充到自己身上，對草係無效')
            break
        if case(int(2)):
            print ('催眠粉:100%令對方睡眠')
            break
        if case(int(3)):
            print ('硬化:100%改變自身攻擊、防禦等級1')
            break
        if case(int(4)):
            print ('疾風快刀:手起刀落')
            break
        if True: 
            print ("幹叫你輸入編號")
            卡利斯技能()
            break
            break
global reskill
reskill='1:雷神天明閃 2:元氣電光球 3:瞬雷天閃 4:閃電鬥氣'
def 雷伊技能():
    n=int(input('輸入技能編號: '))
    for case in switch(n):
        if case(int(1)):
            print ('雷神天明閃:10%機率威力4倍必中')
            break
        if case(int(2)):
            print ('元氣電光球:5%令對方麻痺')
            break
        if case(int(3)):
            print ('瞬雷天閃:5%令對方麻痺')
            break
        if case(int(4)):
            print ('閃電鬥氣:技能使用成功時，100%改變自身防禦+1，特防+1')
            break
        if True: 
            print ("幹叫你輸入編號")
            雷伊技能()
            break

def 技能():
     global haskill
     global loskill
     global moskill
     global saskill
     global caskill
     global reskill
     for case in switch(me):
        if case(int(1)):
            print (haskill)
            break
        if case(int(2)):
            print (loskill)
            break
        if case(int(3)):
            print (moskill)
            break
        if case(int(4)):
            print (saskill)
            break
        if case(int(5)):
            print (caskill)
            break
        if case(int(6)):
            print (reskill)
            break
        if True:
            print('輸入錯誤')
            break
def 技能威力(skill):
    global me
    global mypower
    for case in switch(me):
        if case(int(1)):
            for a in switch(str(skill)):
                if a('1'):
                    mypower=0
                    break
                if a('2'):
                    mypower=0
                    break
                if a('3'):
                    mypower=100
                    break
                if a('4'):
                    mypower=150
                    break
                if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break
            break
        if case(int(2)):
            
            break
        if case(int(3)):
           
            break
        if case(int(4)):
          
            break
        if case(int(5)):
            
            break
        if case(int(6)):
            
            break

def 我方血量(me):
     for case in switch(me):
        if case(int(1)):
            return 哈莫雷特[0]
            break
        if case(int(2)):
            return 羅特利斯[0]
            break
        if case(int(3)):
            return 魔焰猩猩[0]
            break
        if case(int(4)):
            return 薩帕克[0]
            break
        if case(int(5)):
            return 卡利斯[0]
            break
        if case(int(6)):
            return 雷伊[0]
            break
def 敵方血量(you):
     for case in switch(you):
        if case(int(1)):
            return boss1[0]
            break
        if case(int(2)):
            return boss2[0]
            break
        if case(int(3)):
            return boss3[0]
            break
        if case(int(4)):
            return boss4[0]
            break
        if case(int(5)):
            return boss5[0]
            break
        if case(int(6)):
            return boss6[0]
            break
def 友方登場精靈(n):
    print(n,'出場了!')
def 敵方登場精靈(n):
    print(n,'出場了!')
def 玩家攻擊():
    print('輪到你進攻了')
    print('1:替換 2:攻擊 3:使用道具')
    now=str(input())
    if now=='1':
        global me
        name=input('要換誰上場?(1:哈莫雷特 2:羅特利斯 3:魔焰猩猩 4:薩帕克 5:卡利斯 6:雷伊\n')
        for case in switch(name):
           if case('1'):
                友方登場精靈('哈莫雷特')
                me=1
                譜尼攻擊()
                break
           if case('2'):
                友方登場精靈('羅特利斯')
                me=2
                譜尼攻擊()
                break
           if case('3'):
                友方登場精靈('魔焰猩猩')
                me=3
                譜尼攻擊()
                break
           if case('4'):
                me=4
                友方登場精靈('薩帕克')
                譜尼攻擊()
                break
           if case('5'):
                友方登場精靈('卡利斯')
                me=5
                譜尼攻擊()
                break
           if case('6'):
                友方登場精靈('雷伊')
                me=6
                譜尼攻擊()
                break
           if true:
               print('輸入錯誤')
               玩家攻擊()
               break

    elif now=='2':
        print('請選擇技能')
        技能()
        skill=str(input())
        技能威力(skill)
        
        
    elif True:
        print('輸入錯誤')
        玩家攻擊()

def 譜尼攻擊():
    print('幹')
    
import time
#import os
#os.system('bgm.mp3')
   
    

########################################################################################
global me
global you
global mypower
global skill
me=1
you=2

哈莫雷特=[390,302,225,202,215,0.5] 
羅特利斯=[342,236,191,234,197,1.5]
魔焰猩猩=[378,282,193,231,193,2]
薩帕克=[358,232,191,234,235,0.5]
卡利斯=[308,256,233,180,201,2]
雷伊=[343,229,206,221,210,1]
ha='哈莫雷特'
lo='羅特利斯'
mo='魔焰猩猩'
sa='薩帕克'
ca='卡利斯'
re='雷伊'
b1='譜尼一血'
b2='譜尼二血'
b3='譜尼三血'
b4='譜尼四血'
b5='譜尼五血'
b6='譜尼六血'
boss1=[7000,281,236,248,236]
boss2=[8000,281,236,248,236]
boss3=[9000,281,236,248,236]
boss4=[10000,281,236,248,236]
boss5=[20000,281,236,248,236]
boss6=[65000,281,236,248,236]
哈莫雷特pp=[10,15,15,5]
羅特利斯pp=[20,15,25,5]
魔焰猩猩pp=[10,10,5,15]
薩帕克pp=[20,20,5,30]
卡利斯pp=[10,15,20,10]
雷伊pp=[3,10,5,15]

########################################################################################
#print('歡迎來到賽爾號')
#time.sleep(1)
#print('準備好面對童年夢魘了嗎?(準備好請輸入yes)')
#answer=input()
#while answer!='yes'and answer!='YES'and answer!='Yes':
#    print('現在呢?')
#    answer=input()
#else:
#    print('那就開始吧!')
#    time.sleep(1)
#    print('進入戰鬥......')
#    time.sleep(1)
友方登場精靈(ha)
敵方登場精靈(b1)
print('我方血量:',我方血量(me))
print('敵方血量:',敵方血量(you))
玩家攻擊()                  





    
    


    





