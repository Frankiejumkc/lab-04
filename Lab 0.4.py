########################################################################
##
## CS 101 Lab 
## Program 04
## Franklin Jeffries
## fmjc89@umsystem.edu
## 
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

# this block asks the user if they want to play again over and over until they respond "NO"
def play_again() -> bool:
    while True:
        play_again1 = input('Do you want to play again?')
    if play_again1 == 'Y' or 'YES' or 'yes': 
        return True
    elif play_again == 'N' or 'NO' or 'no'
        return False
    else:
        print('Error: please enter a correct response')
def get_wager(bank : int) -> int:
    if wager <= 0:
        print('The wager amount must be greater than 0')
    elif wager <= bank:
        print('The wager must be less than what you have in the bank')
    return 1            
def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    return 1, 2, 3
def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    return 0
def get_bank() -> int:
    chips = int(input))
    # greater than 0 but less than 101
    return 0
def get_payout(wager, matches):
   print(payout)
    return wager * -1
#the above definition is designed to get you a payout.
if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
