from tkinter import *

root = Tk()

root.geometry("400x400")
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Stat variables

stamina = 10
attack = 10
defense = 10
hp = 100
enemy_hp = 100
enemy_def = 10
enemy_att = 20
damage = 0
damage_dealt = 0

# Actions

def Recover():
    global stamina
    global myStamina
    global hp
    global myHealth

    stamina += 1
    hp += 10

    if stamina >= 10:
        stamina = 10

    if hp >= 100:
        hp = 100


    myStamina.config(text="Stamina: " + str(stamina))
    myHealth.config(text="Health: " + str(hp))
    myActions.config(text="You recovered 1 stamina and 10 hp")

def AttackTraining():
    global attack
    global stamina
    global myAttack
    global myStamina
    if stamina < 2:
        return
    stamina -= 2
    attack += 1

    myStamina.config(text="Stamina: " + str(stamina))
    myAttack.config(text="Attack: " + str(attack))
    myActions.config(text="Your attack increased by 1")


def DefenseTraining():
    global defense
    global stamina
    global myDefense
    global myStamina
    if stamina < 2:
        return
    stamina -= 2
    defense += 1

    myStamina.config(text="Stamina: " + str(stamina))
    myDefense.config(text="Defense: " + str(defense))
    myActions.config(text="Your attack increased by 1")

def FightMonster():
    global attack
    global hp
    global defense
    global enemy_def
    global enemy_hp
    global enemy_att
    global damage
    global damage_dealt
    global youWin

    damage = enemy_att - defense
    damage_dealt = attack - enemy_def

    #Stops enemy attack if hp is 0 or less
    if hp <= damage:
        return

    hp -= damage
    enemy_hp -= damage_dealt

    if enemy_hp <= 0:
        youWin.config(text="You won the game!!!")

    enemyStats.config(text="Monster hp: " + str(enemy_hp) + "\n" + "Monster Damage: " + str(enemy_att) + "\n" + "Monster defense: " + str(enemy_def))
    myHealth.config(text="Health: " + str(hp))
    myActions.config(text="You took " + str(damage) + " damage and dealt " + str(damage_dealt))

# Shown stat labels

myStamina = Label(root, font=("Helvetica", 20), text="Stamina: " + str(stamina))
myStamina.grid(row=0, columnspan=3)
myStamina.place(relx=0.5, rely=0.1, anchor="center")

myHealth = Label(root, font=("Helvetica", 12), text="Health: " + str(hp))
myHealth.grid(row=0, columnspan=3)
myHealth.place(relx=0.5, rely=0.18, anchor="center")

myAttack = Label(root, font=("Helvetica", 12), text="Attack: " + str(attack))
myAttack.grid(row=0, columnspan=3)
myAttack.place(relx=0.5, rely=0.24, anchor="center")

myDefense = Label(root, font=("Helvetica", 12), text="Defense: " + str(defense))
myDefense.grid(row=0, columnspan=3)
myDefense.place(relx=0.5, rely=0.30, anchor="center")

# Action buttons

trainingAttack = Button(root, text="Train attack", command=AttackTraining)
trainingAttack.grid(row=1, column=0)

trainingDefense = Button(root, text="Train defense", command=DefenseTraining)
trainingDefense.grid(row=1, column=1)

recoverStamina = Button(root, text="Rest to recover",  command=Recover)
recoverStamina.grid(row=1, column=2)

fightMonster = Button(root, text="Fight monster", command=FightMonster)
fightMonster.grid(row=1, column=3)

# Actions done box

myActions = Label(root, text=" ")
myActions.grid(row=0, columnspan=3)
myActions.place(relx=0.5, rely=0.38, anchor="center")


enemyStats = Label(root, justify="left", text="Monster hp: " + str(enemy_hp) + "\n" + "Monster Damage: " + str(enemy_att) + "\n" + "Monster defense: " + str(enemy_def))
enemyStats.grid(row=2, columnspan=3)
enemyStats.place(relx=0.5, rely=0.70, anchor="n")

youWin = Label(root, font=("Helvetica", 30), text="")
youWin.grid(row=0, columnspan=3)
youWin.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()

