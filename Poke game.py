#Poke game

class Pokemon(name,atk,Def,spd,sp_atk,sp_def):
    
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
    moves = [] #Names for possible moves
    power = [] #Power for moves
    priority = [] #Priority for moves
    
    
    """ Function declaration """
    
    def isInt(value):
        try:
            test_value = int(value)
            return True
        except ValueError:
            return False
    
    def choose_moves():
        global chosen_moves
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