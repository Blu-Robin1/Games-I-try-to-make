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
    return show_hand(hand)    

def select(hand):
    while True:
        selecting = input("Select your die: ")
        selection = [int(value) for value in selecting]
        if selection == []:
            print("Gave empty") 
            continue 
        
        for selected in selection:
            if selected not in hand:
               print(f"Can't select: {selected}")
               continue             
            return  selection           

def scoring(selected):
    selected.sort()
    points= {1:100,222:200,333:300,444:400,555:500,5:50,666:600}
    score=0
    for dice in selected:
        score += points[dice]
    return score

def farkle():
    score=0
    while score <=2000:
        hand = throwing()
        print(f'Your hand is {hand}')
        selected = select(hand)
        print(f"You selected: {selected}")
        score = scoring(selected)
        print(f"You got {score}")
            
    return print("Game Over")

if __name__ == '__main__':
    farkle()
