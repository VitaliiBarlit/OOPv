from Warriors import Warrior
import random as r
import time
'''
def newhero(obj):

    obj = Warrior()
    obj.show()
    h_mod_obj, m_mod_obj, s_mod_obj = obj.race()
    obj.setHP(h_mod_obj * obj.getHP())
    obj.setMP(m_mod_obj * obj.getMP())
    obj.setSP(s_mod_obj * obj.getSP())
    obj.show()
    return obj

orc = None
elf = None
orc = newhero(orc)
elf = newhero(elf)
orc.show()
elf.show()
'''
#obj.race()
#print("HP =",obj.getHP())
#obj.charStat(h_mod_obj, m_mod_obj, s_mod_obj)


#
#  Доработать уровни атаки и защиты
#  Подклассы у каждого класса

#  Орк : Разбойник 20hp -> 20sp || Шаман 20hp -> 20mp

#  Эльф : Охотник 15sp -> 15hp || Жрец 10sp -> 10hp

#  Человек : Рыцарь 10mp -> 15hp || Волшебник 10sp -> 15mp
#                   5sp                       5hp

#  Гном : Палладин 5sp -> 10hp || Чернокнижник 10hp -> 15mp
#                  5sp                         5sp

#  Спектр : Убийца 10mp -> 10sp || Элементалист 10sp -> 10hp
#                  10mp -> 10hp                 10mp -> 10hp

#   Добавить очки за победу и занести их в таблицу лидеров.
#   При достаточном кол-ве очков - подъем уровня.
#
'''
1 - Orc.
2 - Elf.
3 - Human. 
4 - Dwarf. 
5 - Spectre.
'''

orc = Warrior('Eric',2,1)  # name, luck

h_mod_orc, m_mod_orc, s_mod_orc, race_name_orc = orc.race(1)
orc.setHP(h_mod_orc * orc.getHP())
orc.setMP(m_mod_orc * orc.getMP())
orc.setSP(s_mod_orc * orc.getSP())
orc.setRace(1)
orc.charInfo()

elf = Warrior('Mistery',7,2)

h_mod_elf, m_mod_elf, s_mod_elf, race_name_elf = elf.race(2)
elf.setHP(h_mod_elf * elf.getHP())
elf.setMP(m_mod_elf * elf.getMP())
elf.setSP(s_mod_elf * elf.getSP())
elf.setRace(2)
elf.charInfo()

hum = Warrior('Newbee',3,3)

h_mod_hum, m_mod_hum, s_mod_hum, race_name_hum = hum.race(3)
hum.setHP(h_mod_hum * hum.getHP())
hum.setMP(m_mod_hum * hum.getMP())
hum.setSP(s_mod_hum * hum.getSP())
hum.setRace(3)
hum.charInfo()

dwf = Warrior('Oldman',3,4)

h_mod_dwf, m_mod_dwf, s_mod_dwf, race_name_dwf = dwf.race(3)
dwf.setHP(h_mod_dwf * dwf.getHP())
dwf.setMP(m_mod_dwf * dwf.getMP())
dwf.setSP(s_mod_dwf * dwf.getSP())
players = [orc,elf,hum,dwf]
dwf.setRace(4)
dwf.charInfo()

spr = Warrior('Cristall',4,5)

h_mod_spr, m_mod_spr, s_mod_spr, race_name_spr = spr.race(3)
spr.setHP(h_mod_spr * spr.getHP())
spr.setMP(m_mod_spr * spr.getMP())
spr.setSP(s_mod_spr * spr.getSP())
spr.setRace(5)
spr.charInfo()

#players = [hum,hum,hum,hum,dwf]
players = [orc,elf,hum,dwf,spr]



def battle():
    warriors = []
    
    def rrrr():
                
        B = r.choice(players)
        if B not in warriors:
            warriors.append(B)
            return warriors
        else:
             rrrr()
    
    A = r.choice(players)
    warriors.append(A)
    rrrr()
    
    
    A = warriors[0]
    B = warriors[1]
    
    
    
    
    #print("Firts warrior is ", A.name)
    #print("Second warrior is ", B.name)
    
    
#    input("Start! (Press Enter) ")
    
    while A.health >= 1 and B.health >= 1:
        A.attack(B)
        B.attack(A)
    #    continue
        
    file_stat1 = open("stat_win.txt",'a')
    file_stat2 = open("stat_lose.txt",'a')
    file_stat3 = open("stat_tie.txt",'a')
    file_stat4 = open("total.txt",'a')
    if A.health > B.health:
        file_stat1.writelines("\n" + A.name)
        file_stat2.writelines("\n" + B.name)
        file_stat4.writelines("\n" + A.name)
        file_stat4.writelines("\n" + B.name)
        print(A.name, " is a winner! ")
    elif B.health > A.health:
        file_stat2.writelines("\n" + A.name)
        file_stat1.writelines("\n" + B.name)
        file_stat4.writelines("\n" + A.name)
        file_stat4.writelines("\n" + B.name)
        print(B.name, " is a winner! ")
    else:
        file_stat3.writelines("\n" + A.name)
        file_stat3.writelines("\n" + B.name)
        file_stat4.writelines("\n" + A.name)
        file_stat4.writelines("\n" + B.name)
    
        print("Tie.")
    
    
    
    
    file_stat1.close()
    file_stat2.close()
    file_stat3.close()
    file_stat4.close()


#    time.sleep(1)
    
[battle() for _ in range(5)]
#[battle() for _ in range(5)]
#[battle() for _ in range(5)]




import re
#import string
frequency_win = {}
document_text = open('stat_win.txt', 'r')
text_string = document_text.read().capitalize()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency_win.get(word,0)
    frequency_win[word] = count + 1
     
frequency_list = frequency_win.keys()

print("\n")
print("___Winer boaard___")
for words in frequency_list:
    print(words.capitalize(), frequency_win[words])

print("\n")
    
    
    
frequency_lose = {}
document_text = open('stat_lose.txt', 'r')
text_string = document_text.read().capitalize()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency_lose.get(word,0)
    frequency_lose[word] = count + 1
     
frequency_list = frequency_lose.keys()
print("___Loser board___")
for words in frequency_list:
    print(words.capitalize(), frequency_lose[words])
    
       
print("\n")

frequency_lose = {}
document_text = open('total.txt', 'r')
text_string = document_text.read().capitalize()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency_lose.get(word,0)
    frequency_lose[word] = count + 1
     
frequency_list = frequency_lose.keys()
print("___Participation in battle___")
for words in frequency_list:
    print(words.capitalize(), frequency_lose[words])
    
    
    
document_text.close()





def clear():
    file_stat1 = open("stat_win.txt",'w')
    file_stat2 = open("stat_lose.txt",'w')
    file_stat3 = open("stat_tie.txt",'w')
    file_stat4 = open("total.txt",'w')
    
    file_stat1.write('')
    file_stat2.write('')
    file_stat3.write('')
    file_stat4.write('')
    
    file_stat1.close()
    file_stat2.close()
    file_stat3.close()
    file_stat4.close()    