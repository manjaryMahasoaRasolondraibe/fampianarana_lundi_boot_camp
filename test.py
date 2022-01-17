import random
class Game:
    HANDS = ("ROCK","SCISSORS","PAPAER")
    def __init__(self,max_score=3):
        self.player_score = 0
        self.computer_score = 0
        self.max_score = max_score
        
    def play(self):
        while max(self.player_score,self.computer_score)<3:
            computer_hand = random.choice(self.HANDS)
            print(f"You have picked {computer_hand}")
        if self.player_score<self.computer_score:
            print("You loose")
        else:
            print("You win")
            
    def get_player_hand(self):
        for index,hand in enumerate(self.HANDS):
            print(index + 1, hand)
            player_hand_index = int(input("what do you choose?\n> "))
            return self.HANDS[player_hand_index -1]
        
    def compare_hand(self,computer_hand,player_hand):
        if computer_hand == player_hand:
                print("Tsisy resy")
        elif player_hand == "ROCK" and computer_hand == "SCISSORS":
            # print("Player wins")
            self.player_score+=1
        elif player_hand == "SCISSORS" and computer_hand == "PAPER":
            # print("Player wins")
            self.player_score+=1
        elif player_hand == "PAPER" and computer_hand == "ROCK":
            # print("Player wins")
            self.player_score+=1
        else:
            self.computer_score+=1
    def __print_score(self):
        print(f"Score: player= {self.player_score} - computer ={self.computer_score}")
if __name__=='__main__':
    game = Game()
    game.play()