#Poke game

def isInt(value):
    try:
        test_value = int(value)
        return True
    except ValueError:
        return False

class Pokemon():
    """ initial function """
    name = ""
    attack = ""
    defence = ""
    speed = ""
    sp_attack = ""
    sp_defence = ""
    
    def initialize(NAME,atk,Def,spd,sp_atk,sp_def):
        global name,attack,defence,speed,sp_attack, sp_defence
        name = NAME
        attack = atk
        defence = Def
        speed = spd
        sp_attack = sp_atk
        sp_defence = sp_def
    
    
    """ Status condition initialization """
    
    poison = False
    paralized = False
    burn = False
    sleep = False
    frozen = False
    confused = False
    
    """  Other stat, and move initialization """
    
    health = 100 #in HP
    move = [] #Stores chosen move name, priority, and base power
    
    chosen_moves = [] #Will have the names of the chosen moves once the user chooses.
    moves = ["TEST"] #Names for possible moves
    power = ["TEST"] #Power for moves
    priority = ["TEST"] #Priority for moves
    
    
    """ Function declaration """
    
    def choose_moves():
        global chosen_moves
        global moves
        global power
        global priority
        for x in range(len(moves)):
            print(f"{x}\nName: {moves[x]}\nBase power: {power[x]}\nMove priority: {priority[x]}\n")
        print("Scroll through the list moves, and enter ONE number at a time to select the move. (@1/30/20 no moves restrictions with type)")
        iteration = 0
        while True:
            move = input("Move #")
            if isInt(move) == True:
                chosen_moves.insert(0,moves[int(move)])
                iteration += 1
            else:
                print("Invalid move number. Try again!")
            if iteration == 4:
                break
    
    def make_move():
        global chosen_moves
        print("Your moves are as follows:\n")
        for x in range(len(chosen_moves)):
            print(f"{x} : {chosen_moves[x]}")
        chosen_move = ""
        while True:
            if isInt(chosen_move) == True:
                chosen_move = int(chosen_move)
                if 1 > chosen_move or chosen_move > 5:
                    print("That is not a valid move. Please try again!")
                elif not chosen_move > 5:
                    move = []
                    move.insert(0,moves[chosen_move],priority[chosen_move], power[chosen_move])
                    break
                else:
                    #switch out pokemon with option to cancel and return to attacking
                    pass #temporary placeholder to remove warning/yellow underline in editor
    
    def getMove(): 
        global move
        """ Returns: Move name, Priority, Base power. In that order """
        return move #is a list
    
    def take_damage(value):
        global health
        health -= value
        if health <= 0:
            alert_death()
        else:
            print(f"Current health for {name} is {health}.")
    
    def restore_health(value):
        global health
        if health + value >= 100:
            health = 100
        else:
            health += value
    
    """ Choose moves, and then let the player class take care of the rest. """
    
    choose_moves()
    
class Player(name):
    print(f"Player: {name} has joined the fight!")
    import time as t
    t.sleep(2)
    print(f"Please choose a starter..")
    starter_names = ["Onneon","Spyodre", "Wormana"] #Types: Fighting, Bug (When evolved: + poison), Psychic
    starter_hp = [16, 13, 23] #hp = hp + ((level * hp) * 0.1)
    starter_atk = [14, 10, 1]
    starter_def = [18, 10, 1]
    starter_sp_def = [8, 12, 20]
    starter_sp_atk = [5, 10, 20]
    starter_speed = [12, 18, 8]
    
    for i in range(len(starter_names)):
        print(f"{i}\nName: {starter_names[i]}\nHP: {starter_hp[i]}\nATK: {starter_atk[i]}\nDEF: {starter_def[i]}\nSP-ATK: {starter_sp_atk[i]}\nSP-DEF: {starter_sp_def[i]}\nSPEED: {starter_speed[i]}")
    
    starter = ""
    while isInt(starter) == False:
        print("Select the number for the starter you wish to choose.")
        starter = input(">> ")
        if isInt(starter) == True:
            starter = int(starter)
            if starter > len(starter_names) or starter < 1:
                starter = ""
            else:
                starter = starter - 1
    chosen_starter = Pokemon(starter_names[starter], starter_atk[starter], starter_def[starter], starter_speed[starter], starter_sp_atk[starter], starter_sp_def[starter])
    
Ty = Player("Ty")
