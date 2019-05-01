import random as r
class Test:
    hp = 100

    def __init__(self, name):
        self.name = name
        print("New object was created. ")
        
    def attack(self,hp):
        self.hp -= r.randint(0,25)
        print(self.name," HP left: ", self.hp)
        return self.hp 




import inspect

x,yyyy,z = 1,2,3

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

print(retrieve_name(2))