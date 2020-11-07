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
import random

def phydmg(power,atk,defense,counter):
    """物攻傷害"""
    result = (int)(42*power*atk*random.uniform(0.95,1.15)/defense/50+2*1.5*counter*(217-255)/255)
    return result
def magdmg(power,magatk,magdefense,counter):
    """魔攻傷害"""
    result = (int)(42*power*magatkrandom.uniform(0.95,1.15)/magdefense/50+2*1.5*counter*(217-255)/255)
    return result
global haskill
haskill='1:龍之意志 2:迴避 3:龍王波 4:龍王滅碎陣'
def 哈莫雷特技能():
            print ('龍之意志:100%改變自身攻擊、防御、特攻、特防等级1')
            print ('迴避:回合本方先手攻擊，使得對方的技能失效')
            print ('龍王波:必定命中對方')
            print ('龍王滅碎陣:5%令對方疲憊，1回合無法攻擊')
            print('')
global loskill
loskill='1:幻化之火 2:火之意志 3:灼燒 4:天火鳳凰'
def 羅特利斯技能():
            print ('幻化之火:命中后100%令對手睡眠')
            print ('火之意志:100%改變自身特攻等级2')
            print ('灼燒:命中後100%令對方燒傷')
            print ('天火鳳凰:純傷害')
            print('')
global moskill
moskill='1:覺醒 2:絕命火焰 3:全力一擊 4:火焰漩渦'
def 魔焰猩猩技能():
            print ('覺醒:100%改變自身攻擊、特攻等級2')
            print ('絕命火焰:命中時5%的概率秒殺對方')
            print ('全力一擊:純傷害')
            print ('火焰漩渦:命中後100%令對方燒傷')
            print('')
global saskill
saskill='1:相位移動 2:精神強化 3:樂鏡迷蹤 4:淨化街'
def 薩帕克技能():
            print ('相位移動:若本回合先手，對方技能失效')
            print ('精神強化:技能使用成功時，100%改變自身特攻等級2')
            print ('樂鏡迷蹤:10%改變對方攻擊等級-1')
            print ('淨化街:清除對方能力提升的效果')
            print('')
global caskill
caskill='1:寄生種子 2:催眠粉 3:硬化 4:疾風快刀'
def 卡利斯技能():
            print ('寄生種子:每回合吸取對方最大體力1/8並補充到自己身上，對草係無效')
            print ('催眠粉:100%令對方睡眠')
            print ('硬化:100%改變自身攻擊、防禦等級1')
            print ('疾風快刀:純傷害')
            print('')
global reskill
reskill='1:雷神天明閃 2:元氣電光球 3:瞬雷天閃 4:閃電鬥氣'
def 雷伊技能():
            print ('雷神天明閃:10%機率威力4倍必中')
            print ('元氣電光球:5%令對方麻痺')
            print ('瞬雷天閃:5%令對方麻痺')
            print ('閃電鬥氣:技能使用成功時，100%改變自身防禦+1，特防+1')
            print('')
def 技能說明():
    global me
    if me==1:
        哈莫雷特技能()
    elif me==2:
        羅特利斯技能()
    elif me==3:
        魔焰猩猩技能()
    elif me==4:
        薩帕克技能()
    elif me==5:
        卡利斯技能()
    elif me==6:
        雷伊技能()

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
    global skilltype
    global mypower
    for case in switch(me):
        if case(int(1)):
            for a in switch(str(skill)):
                if a('1'):
                    mypower=0
                    skilltype=哈莫雷特pp[4]
                    break
                if a('2'):
                    mypower=0
                    skilltype=哈莫雷特pp[5]
                    break
                if a('3'):
                    mypower=100
                    skilltype=哈莫雷特pp[6]
                    break
                if a('4'):
                    mypower=150
                    skilltype=哈莫雷特pp[7]
                    break
                if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break
            break
        if case(int(2)):
            for a in switch(str(skill)):
               if a('1'):
                    mypower=0
                    skilltype=羅特利斯pp[4]
                    break
               if a('2'):
                    mypower=0
                    skilltype=羅特利斯pp[5]
                    break
               if a('3'):
                    mypower=0
                    skilltype=羅特利斯pp[6]
                    break
               if a('4'):
                    mypower=150
                    skilltype=羅特利斯pp[7]
                    break
               if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break
            break
        if case(int(3)):
            for a in switch(str(skill)):
               if a('1'):
                    mypower=0
                    skilltype=魔焰猩猩pp[4]
                    break
               if a('2'):
                    mypower=100
                    skilltype=魔焰猩猩pp[5]
                    break
               if a('3'):
                    mypower=120
                    skilltype=魔焰猩猩pp[6]
                    break
               if a('4'):
                    mypower=15
                    skilltype=魔焰猩猩pp[7]
                    break
               if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break
            break
        if case(int(4)):
            for a in switch(str(skill)):
               if a('1'):
                    mypower=0
                    skilltype=薩帕克pp[4]
                    break
               if a('2'):
                    mypower=0
                    skilltype=薩帕克pp[5]
                    break
               if a('3'):
                    mypower=110
                    skilltype=薩帕克pp[6]
                    break
               if a('4'):
                    mypower=50
                    skilltype=薩帕克pp[7]
                    break
               if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break
          
            break
        if case(int(5)):
            for a in switch(str(skill)):
               if a('1'):
                    mypower=0
                    skilltype=卡利斯pp[4]
                    break
               if a('2'):
                    mypower=0
                    skilltype=卡利斯pp[5]
                    break
               if a('3'):
                    mypower=0
                    skilltype=卡利斯pp[6]
                    break
               if a('4'):
                    mypower=125
                    skilltype=卡利斯pp[7]
                    break
               if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break            
            break
        if case(int(6)):
            for a in switch(str(skill)):
               if a('1'):
                    mypower=160
                    skilltype=雷伊pp[4]
                    break
               if a('2'):
                    mypower=140
                    skilltype=雷伊pp[5]
                    break
               if a('3'):
                    mypower=150
                    skilltype=雷伊pp[6]
                    break
               if a('4'):
                    mypower=0
                    skilltype=雷伊pp[7]
                    break
               if True:
                    print('輸入錯誤')
                    玩家攻擊()
                    break            
            
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
        if True:
            print('bug')
            break
def 顯示狀態(me):
    for case in switch(me):
        if case(int(1)):
            print('生命:',哈莫雷特[0],'物攻:',哈莫雷特[1],'物防:',哈莫雷特[2],'特攻:',哈莫雷特[3],'特防:',哈莫雷特[4])
            break
        if case(int(2)):
            print('生命:',羅特利斯[0],'物攻:',羅特利斯[1],'物防:',羅特利斯[2],'特攻:',羅特利斯[3],'特防:',羅特利斯[4])
            break
        if case(int(3)):
            print('生命:',魔焰猩猩[0],'物攻:',魔焰猩猩[1],'物防:',魔焰猩猩[2],'特攻:',魔焰猩猩[3],'特防:',魔焰猩猩[4])
            break
        if case(int(4)):
            print('生命:',薩帕克[0],'物攻:',薩帕克[1],'物防:',薩帕克[2],'特攻:',薩帕克[3],'特防:',薩帕克[4])
            break
        if case(int(5)):
            print('生命:',卡利斯[0],'物攻:',卡利斯[1],'物防:',卡利斯[2],'特攻:',卡利斯[3],'特防:',卡利斯[4])
            break
        if case(int(6)):
            print('生命:',雷伊[0],'物攻:',雷伊[1],'物防:',雷伊[2],'特攻:',雷伊[3],'特防:',雷伊[4])
            break
def 能力提升():
    global skilltype;global hitrate;global me
    global skill; global mypower;global haskilllv;global loskilllv;global moskilllv;global saskilllv;global reskilllv;global caskilllv
    if me==1 and skill=='1':
                haskilllv+=0.5
                哈莫雷特[1]=int(原哈莫雷特[1]*haskilllv);哈莫雷特[2]=int(原哈莫雷特[2]*haskilllv);哈莫雷特[3]=int(原哈莫雷特[3]*haskilllv);哈莫雷特[4]=int(原哈莫雷特[4]*haskilllv)
                print('哈莫雷特使用了龍之意志,攻擊、防禦、特攻、特防提高了')
    elif  me==2 and skill=='2':
                loskilllv+=0.5
                羅特利斯[3]=int(原哈莫雷特[3]*loskilllv)
                print('羅特利斯使用了火之意志,特攻大幅提高了')
    elif me==3 and skill=='2':
                moskilllv+=1
                魔焰猩猩[1]=int(原魔焰猩猩[1]*moskilllv);魔焰猩猩[3]=int(原魔焰猩猩[3]*moskilllv)
                print('魔焰猩猩使用了覺醒,物攻、特攻大幅提高了')
    elif me==4 and skill=='2':
                saskilllv+=1
                薩帕克[3]=int(原薩帕克[3]*saskilllv)
                print('薩帕克使用了精神強化,特攻大幅提高了')
    elif me==5 and skill=='3':
                caskilllv+=0.5
                卡利斯[1]=int(原卡利斯[1]*caskilllv);卡利斯[2]=int(原卡利斯[2]*caskilllv)
                print('卡利斯使用了硬化,攻擊、防禦提高了')
    elif me==6 and skill=='4':
                reskilllv+=0.5
                雷伊[2]=int(雷伊[2]*reskilllv);雷伊[4]=int(雷伊[4]*reskilllv)
                print('雷伊使用了閃電鬥氣,防禦、特防提高了')
def 特殊狀態(me):
     global skilltype;global hitrate
     global skill; global mypower
     global stop;global fire
     global you
     for case in switch(me):
        if case(int(1)):
            if skill=='2':
                print('哈莫雷特使用了迴避')
                hitrate=0
            elif skill=='4':
                if random.randint(1,100)<=5:
                    print('譜尼疲憊了')
                    stop=1;
            break
        if case(int(2)):
            if skill=='1':
                print('羅特利斯使用了幻化之火')
                print('譜尼睡著了')
                stop=2
            elif skill=='3':
                print('羅特利斯使用了灼燒')
                print('譜尼燒傷了')
                fire=1
            break
        if case(int(3)):
            if skill=='4':
                print('魔焰猩猩使用了火焰漩渦')
                print('譜尼燒傷了')
                fire=1
            break
        if case(int(4)):
            if skill=='1':
                print('薩帕克使用了相位移動')
                hitrate=0
            break
        if case(int(5)):
            if skill=='1':
                print('卡利斯使用了寄生種子')
                print('譜尼被寄生了')
                寄生=1
            if skill=='2':
                print('卡利斯使用了催眠粉')
                print('譜尼睡著了')
                stop=2
            break
        if case(int(6)):
            if skill=='1':
                if random.randiant(1,100)<=10:
                    mypower*=4
            if skill=='2':
                if random.randiant(1,100)<=5:
                    print('譜尼麻痺了')
                    stop=1
            if skill=='3':
                if random.randiant(1,100)<=5:
                    print('譜尼麻痺了')
                    stop=1
            break

            
def 判斷傷害(me):
     global skilltype;global hitrate
     global skill; global mypower
     for case in switch(me):
        if case(int(1)):
            if  me==1 and (skill=='3'or skill=='4'):
                if skilltype==1:
                    return phydmg(mypower,哈莫雷特[1],boss1[2],哈莫雷特[6])
                elif skilltype==2:
                    return magdmg(mypower,哈莫雷特[3],boss1[4],哈莫雷特[6])
            break
        if case(int(2)):
            if  me==2 and skill=='4':
                if skilltype==1:
                    return phydmg(mypower,羅特利斯[1],boss1[2],羅特利斯[6])

                elif skilltype==2:
                    return magdmg(mypower羅特利斯[3],boss1[4],羅特利斯[6])
            break
        if case(int(3)):
            if  me==3 and (skill=='2'or skill=='3'or skill=='4'):
                if skilltype==1:
                    return phydmg(mypower,魔焰猩猩[1],boss1[2],魔焰猩猩[6])

                elif skilltype==2:
                    return magdmg(mypower魔焰猩猩[3],boss1[4],魔焰猩猩[6])
            break
        if case(int(4)):
            if  me==4 and skill=='3':
                if skilltype==2:
                    return magdmg(mypower薩帕克[3],boss1[4],薩帕克[6])
            break
        if case(int(5)):
            if me==5 and skill=='4':
                if skilltype==1:
                    return phydmg(mypower,薩帕克[1],boss1[2],薩帕克[6])

            
            break
        if case(int(6)):
            if me==6 and (skill=='1'or skill=='2'):
                if skilltype==1:
                    return phydmg(mypower,雷伊[1],boss1[2],雷伊[6])

                elif skilltype==2:
                    return magdmg(mypower雷伊[3],boss1[4],雷伊[6])
                
            break

def 判斷效果(you):
    global skilltype;global hitrate;global me
    global skill; global mypower;global haskilllv;global loskilllv;global moskilllv;global saskilllv;global reskilllv;global caskilllv
    for case in switch(you):
        if case(int(1)):
            if  me==1 and skill=='3':
                print('哈莫雷特使用了龍王波,造成了',判斷傷害(me),'傷害')
                boss1[0]-=判斷傷害(me)
            elif me==1 and skill=='1':
                能力提升()
            elif me==1 and skill=='2':
                print('哈莫雷特使用了迴避')
                hitrate=0
            elif me==2 and skill=='2':
                能力提升()
            elif me==3 and skill=='2':
                能力提升()
            elif me==4 and skill=='2':
                能力提升()
            elif me==5 and skill=='3':
                能力提升()
            elif me==6 and skill=='4':
                能力提升()
            elif me==6 and skill=='1':
                boss1[0]-=判斷傷害(me)
                print('雷伊使用了雷神天明閃,造成了',判斷傷害(me),'傷害')
            else:
                print('Miss')
            break
        if case(int(2)):
            if me==1 and skill=='1':
                能力提升()
            elif me==1 and skill=='2':
                特殊狀態(me)
            elif me==2 and skill=='2':
                能力提升()
            elif me==3 and skill=='2':
                能力提升()
            elif me==4 and skill=='2':
                能力提升()
            elif me==5 and skill=='3':
                能力提升()
            elif me==6 and skill=='4':
                能力提升()
            elif me==2 and skill=='1':
                特殊狀態(me)
            elif me==2 and skill=='3':
                特殊狀態(me)
            elif me==3 and skill=='4':
                特殊狀態(me)
            elif me==4 and skill=='1':
                特殊狀態(me)
            elif me==5 and skill=='1':
                特殊狀態(me)
            elif me==5 and skill=='2':
                特殊狀態(me)
            else:
                 print('Miss')
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
    global skill
    global skilltype
    print('輪到你進攻了')
    print('1:替換 2:攻擊 3:顯示狀態 4:技能說明 5:使用道具')
    now=str(input())
    if now=='1':
        global me
        name=input('要換誰上場?(1:哈莫雷特 2:羅特利斯 3:魔焰猩猩 4:薩帕克 5:卡利斯 6:雷伊\n')
        for case in switch(name):
           if case('1'):
                友方登場精靈('哈莫雷特')
                me=1
                譜尼攻擊()
                玩家攻擊()
                break
           if case('2'):
                友方登場精靈('羅特利斯')
                me=2
                譜尼攻擊()
                玩家攻擊()
                break
           if case('3'):
                友方登場精靈('魔焰猩猩')
                me=3
                譜尼攻擊()
                玩家攻擊()
                break
           if case('4'):
                me=4
                友方登場精靈('薩帕克')
                譜尼攻擊()
                玩家攻擊()
                break
           if case('5'):
                友方登場精靈('卡利斯')
                me=5
                譜尼攻擊()
                玩家攻擊()
                break
           if case('6'):
                友方登場精靈('雷伊')
                me=6
                譜尼攻擊()
                玩家攻擊()
                break
           else:
               print('輸入錯誤')
               玩家攻擊()
               break

    elif now=='2':
        print('請選擇技能')
        技能()
        skill=str(input())
        技能威力(skill)
        判斷效果(you)

    elif now=='3':
        顯示狀態(me)
        玩家攻擊()
    elif now=='4':
        技能說明()
        玩家攻擊()



        
        
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
global skilltype
global haskilllv;global loskilllv;global moskilllv;global saskilllv;global caskilllv;global reskilllv
global hitrate;global stop;global fire;global 寄生;
me=1
you=1
haskilllv=loskilllv=moskilllv=saskilllv=caskilllv=reskilllv=1
hitrate=1
stop=0

哈莫雷特=[390,302,225,202,215,0.5,2];原哈莫雷特=[390,302,225,202,215,0.5,2] 
羅特利斯=[342,236,191,234,197,1.5,0.75];原羅特利斯=[342,236,191,234,197,1.5,0.75]
魔焰猩猩=[378,282,193,231,193,2,0.5];原魔焰猩猩=[378,282,193,231,193,2,0.5]
薩帕克=[358,232,191,234,235,0.5,2];原薩帕克=[358,232,191,234,235,0.5,2]
卡利斯=[308,256,233,180,201,2,0.5];原卡利斯=[308,256,233,180,201,2,0.5]
雷伊=[343,229,206,221,210,1,1];原雷伊=[343,229,206,221,210,1,1]
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
哈莫雷特pp=[10,15,15,5,3,4,1,1]
羅特利斯pp=[20,15,25,5,0,3,0,2]
魔焰猩猩pp=[10,10,5,15,3,1,1,2]
薩帕克pp=[20,20,5,30,4,3,2,3]
卡利斯pp=[10,15,20,10,0,0,3,1]
雷伊pp=[3,10,5,15,1,2,1,3]
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





    
    


    





