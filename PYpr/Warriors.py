import random as r

class Warrior(object):
    
    def __init__(self,name,luck=int,race_chs=int):
        self.name = name
        self.race_chs = race_chs
        self.luck = luck
        self.health = 1
        self.mana = 1
        self.stamina = 1
        
#        self.file = open(name + ".txt",'w')
#        self.file.write("Name: "+ self.name)
        
#        print("New hero created. ")
#        print("Train your warrior. \n")
#        self.file.close()
        
    def setHP(self, health):
        self.health = health
        return self.health
    def setMP(self, mana):
        self.mana = mana
        return self.mana
    def setSP(self, stamina):
        self.stamina = stamina
        return self.stamina

    def getHP(self):
        return self.health
    def getMP(self):
        return self.mana
    def getSP(self):
        return self.stamina
    
    def show(self):
        print("HP: ",self.health)
        print("MP: ",self.mana)
        print("SP: ",self.stamina)
        print()
        print("\n")

    def attack(self,health):
        hit = r.randint(0,2)
        luck = r.randint(0,self.luck)
        hithit = hit - luck
        if hithit > 0:
            self.health -= hithit
#        print(self.name," HP left: ", self.health)
        return self.health
    
    def race(self,race_chs):
#        print("Choose race: ")
#        print(" 1 - Orc. \n",
#            "2 - Elf. \n",
#            "3 - Human. \n",
#            "4 - Dwarf. \n",
#            "5 - Spectre. \n",)

        #race_chs = int(input())
        if race_chs == 1:
            self.h_mod = 50
            self.m_mod = 10
            self.s_mod = 30
            self.race_name = 'Orc'
#            print("New warrior is orc. \n")
            return self.h_mod, self.m_mod, self.s_mod, self.race_name
        elif race_chs == 2:
            self.h_mod = 20
            self.m_mod = 30
            self.s_mod = 40
            self.race_name = 'Elf'
#            print("New warrior is elf. \n")
            return self.h_mod, self.m_mod, self.s_mod, self.race_name
        elif race_chs == 3:
            self.h_mod = 30
            self.m_mod = 30
            self.s_mod = 30
            self.race_name = 'Human'
#            print("New warrior is human. \n")
            return self.h_mod, self.m_mod, self.s_mod, self.race_name
        elif race_chs == 4:
            self.h_mod = 40
            self.m_mod = 30
            self.s_mod = 20
            self.race_name = 'Dwarf'
#            print("New warrior is dwarf. \n")
            return self.h_mod, self.m_mod, self.s_mod, self.race_name
        elif race_chs == 5:
            self.h_mod = 10
            self.m_mod = 50
            self.s_mod = 30
            self.race_name = 'Spectre'
#            print("New warrior is spectre. \n")
            return self.h_mod, self.m_mod, self.s_mod, self.race_name

        def race_name(self, race_chs):
              
            if race_chs == 1:
                return 'Orc'
            elif race_chs == 2:
                return 'Elf'
            elif race_chs == 3:
                return 'Human'
            elif race_chs == 4:
                return 'Dwarf'
            elif race_chs == 5:
                return 'Spectre'
            
    def setRace(self, race_chs):
        self.h_mod, self.m_mod, self.s_mod, self.str_race = self.race(race_chs)
#        self.file = open(self.name + ".txt",'a')
#        self.file.write("\nRace: "+ self.str_race)
#        self.file.close()

    
    def charInfo(self):
        self.file = open(self.name + ".txt",'w')
        self.file.write("Name: "+ self.name)
        self.file.write("\nRace: "+ self.str_race)
        self.file.write("\nHeath: "+ str(self.health))
        self.file.close()
#    def battle():
#        
#        input("Start! (Press Enter) ")
#        while A.health >= 1 and B.health >= 1:
#            A.attack(B)
#            B.attack(A)
#            continue
#            
#        if A.health > B.health:
#            print(A.name, " is a winner! ")
#        elif B.health > A.health:
#            print(B.name, " is a winner! ")
#        else:
#            print("Tie.")
      
##        else:
##            race_chs = int(input())

##    def addStat(self):
##        
##        return 0
##            
##    def charStat(self, h_mod, m_mod, s_mod):
##        print("You have 10 training point'\s on start.")
##        tp = 10
##        
##        print(" HP = {}. \n MP = {}. \n SP = {}. \n".format(
##            self.health * h_mod,
##            self.mana * m_mod,
##            self.stamina * s_mod))
##        print("Choose point'\s to add: ")

                                



    
        
