import random 

def roll():

    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Enter The Number Of palyers (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
             print("Must be between 2 - 4 palyers.")
    else:
        print("Invalid,Try again.")
        
max_scores = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_scores:
    for player_idx in range(players):
        print("\nPlayer number",player_idx + 1,"turn has just strated!!\n")
        current_scores=0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
               break
            value = roll()
            if value == 1:
               print("You rolled a 1! turn Done!")
               current_scores=0
               break
            else:
                current_scores += value
                print("You rolled a:",value)

            print("Your Score is:",current_scores) 
        player_scores[player_idx]  += current_scores
        print("Your Total Score is:",player_scores[player_idx])     

                 