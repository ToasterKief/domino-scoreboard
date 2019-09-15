import os

class Player:
	def __init__(self):
		self.totalscore = 0
		
		
	def score(self, amount):
		self.totalscore += amount
		print("Player 1 Scored {}".format(amount))
	

def main():
	os.system("clear")
	player1 = Player()
	player2 = Player()
	

	
	while player1.totalscore < 150 and player2.totalscore < 150:
		print("Player 1's Score: {}\n".format(player1.totalscore))
		print("Player 2's Score: {}\n".format(player2.totalscore))
		print("\n")
		chooseplayer = str(input("Enter either 1 or 2 to update that player's score =>"))
		if chooseplayer == "1":
			amount = int(input("Points scored => "))
			
			player1.score(amount)
			os.system("clear")
			
		elif chooseplayer == "2":
			amount = int(input("Points scored => "))
			
			player2.score(amount)
			os.system("clear")
		else:
			print("Invalid Input\n")
		
	if player1.totalscore >= 150:
		print("Player 1 Won!\n")
		
	elif player2.totalscore >= 150:
		print("Player 2 Won!\n")
		
	


if __name__ == "__main__":
	main()	
