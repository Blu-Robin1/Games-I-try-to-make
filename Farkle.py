import random
# pip install emojiize --> emojiize.emojify(":die:")

class Die:
    def __init__(self):
        self.value=random.randint(1,6)
    
def show_hand(hand):
    rev=[]
    #dict to store dice emoji
    for dice in hand:
        if type(dice) is list:
            for die in dice:
                rev.append(die.value)
        else:
            rev.append(dice.value)
    return rev
    

def throwing(amount=6):
    dice = list(range(0,amount))
    #dice=["a","b","c","d","e","f"]
    hand=[]
    for x in dice:
        x = Die()
        hand.append(x)
    return hand    

def select(hand):
    while True:
        selecting = input("Select your die: ")
        try:
            selection = [hand[int(value)-1] for value in selecting]
            if selection == []:
                print("Gave empty") 
                continue 
        except (IndexError, ValueError):
            print("Wrong input or too many")
            continue

        try:
            want_to_score = []
            for selected in selection:                
                for dice in hand:
                    if dice == selected:
                        want_to_score.append(dice)
                        if len(want_to_score) == len(selection):
                            return want_to_score
                    
        except ValueError:
            print("Selected a dice that doesn't exit")
            continue

def new_hand(selected,hand):
    for dice in selected:
        hand.remove(dice)
    return hand

def scoring(selected):
    
    scores = {
        '1': 100,
        '5': 50,
        '11': 200,
        '15': 150,
        '55': 100,
        '115': 250,
        '155': 200,
        '111': 1000,
        '222': 200,
        '333': 300,
        '444': 400,
        '555': 500,
        '666': 500,    
    }
    
    selected = sorted(show_hand(selected))

    res_string = ''
    res_li=[]

    while len(selected) != 0:
        counter=0
        
        for die in selected:
            res_li.append(die)
            value=die
            selected.pop(0)
            counter +=1
        
            if len(selected) == 0:
                for dice in res_li:
                    res_string += str(dice)

            elif value != 5 or value != 1:
                for dice in res_li:
                    res_string += str(dice)

            # if value is not 1:
            #     for dice in res_li:
            #         res_string += str(dice)

            elif counter == 2 & selected[1] != value:
                for dice in res_li:
                    res_string += str(dice)                          
        break        

    # for die in selected:
    #     res_string += str(die)
        
    try:
        scored = scores[res_string]
        return scored
    except KeyError:
        scored = "Farkle!"
        return scored

def farkle():
    print("To select the dice input it's position in the list \n" \
    "1 & 5 can be scored as singles or combinitions, rest must be of threes")
    score=0
    while score < 2000:
        hand = throwing()
        choice=0
        dice_stack = []
        while choice != 's': 

            print(f'Your hand is {show_hand(hand)}')
            selected = select(hand)
            print(f'You selected: {show_hand(selected + dice_stack)}')

            choice = input("Score: s \n" \
                            "Reroll: r \n")
            
            if choice.lower() == 's':
                scored = scoring(selected + dice_stack)
                if type(scored) == str:                
                    print(f"{scored}")                    
                else:                
                    score +=scored                
                    print(f"You got {scored}\nYour new score is {score}")
            # else:
            for die in selected:
                dice_stack.append(die)
            hand = new_hand(selected,hand)
            hand = throwing(len(hand))    
    return print("Game Over")

if __name__ == '__main__':
    farkle()
    #swtich so a user can choose to read the instructions