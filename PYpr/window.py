from tkinter import *
from Warriors import Warrior
import time


#root = Tk()


def button_clicked():
    elf = Warrior('Mistery',7,2)

    h_mod_elf, m_mod_elf, s_mod_elf, race_name_elf = elf.race(2)
    elf.setHP(h_mod_elf * elf.getHP())
    elf.setMP(m_mod_elf * elf.getMP())
    elf.setSP(s_mod_elf * elf.getSP())
    elf.setRace(2)
    elf.charInfo()
    return button.configure(text = elf.name)

root=Tk()
button = Button(root)

label = Label(root)

#label.configure(text = new.name)
button.configure(text='New Hero', command=button_clicked)

label.pack()
button.pack()
root.mainloop()
