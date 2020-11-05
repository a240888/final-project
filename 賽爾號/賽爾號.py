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
            break
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
            break
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
            break
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
            break
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
            break
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
            break


 
   
    

###############################################################
哈莫雷特=[390,302,225,202,215,0.5] 
羅特利斯=[342,236,191,234,197,1.5]
魔焰猩猩=[378,282,193,231,193,2]
薩帕克=[358,232,191,234,235,0.5]
卡利斯=[308,256,233,180,201,2]
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




