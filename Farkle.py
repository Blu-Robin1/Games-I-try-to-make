import random

class Die:
    def __init__(self):
        self.value=random.randint(1,6)
    
def show_hand(hand):
    rev=[]
    for die in hand:
     rev.append(die.value)
    return rev
    
def throwing():
    dice=["a","b","c","d","e","f"]
    hand=[]
    for x in dice:
        x = Die()
        hand.append(x)
    return hand    

def select(hand):
    while True:
        selecting = input("Select your die: ")
        selection = [int(value) for value in selecting]
        if selection == []:
            print("Gave empty") 
            continue 
        elif len(selection) > 6:
            print("Gave too many") 
            continue 
        
        try:
            want_to_score = []
            for selected in selection:                
                for dice in hand:
                    if dice.value == selected:
                        want_to_score.append(dice)
                        if len(want_to_score) == len(selection):
                            return want_to_score
                    
        except ValueError:
            print("Selected a dice that doesn't exit")
            continue

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
    
    # selected.sort()

    res_string = ''

    for die in selected:
        res = die.value
        res_string += str(res)

    return scores[res_string]


def farkle():
    score=0
    while score <=2000:
        hand = throwing()
        print(f'Your hand is {show_hand(hand)}')
        selected = select(hand)
        print(f"You selected: {show_hand(selected)}")
        scored = scoring(selected)
        score +=scored
        print(f"You got {scored}\nYour new score is {score}")
            
    return print("Game Over")

if __name__ == '__main__':
    farkle()
