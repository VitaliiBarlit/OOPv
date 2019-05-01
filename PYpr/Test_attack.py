from Test import Test

import random as r
'''
A = Test('A')
B = Test('B')



while A.hp >= 0 or B.hp >= 0:
    A.attack(B)
    B.attack(A)

if A.hp > B.hp:
    print("A is a winner! ")
elif B.hp > A.hp:
    print("B is a winner! ")
'''

'''
s1 = [3,3,3,4,4,4]
s2 = []

A = r.choice(s1)
B = r.choice(s1)


def comp(s1):
    A = r.choice(s1)
    B = r.choice(s1)
    if A != B:
        print("First: ", A)
        print("Second: ", B)
    else:
        comp(s1)
comp(s1)
#print("a is ",a)
print("s left", s1)
'''

class Battle(object):
    def __init__(self, health, name):
        self.name = name
        self.health = health
    
    def attack(self,health):
        hit = r.randint(0,2)
        luck = r.randint(0,self.luck)
        hithit = hit - luck
        if hithit > 0:
            self.health -= hithit
        print(self.name," HP left: ", self.health)
        return self.health





