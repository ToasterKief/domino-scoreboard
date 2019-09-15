import os
import time
class Player:
	def __init__(self, name):
		self.totalscore = 0
		self.name = name
		
	def score(self, amount):
		self.totalscore += amount
		print("{} Scored {}".format(self.name, amount))
	

def main():
	os.system("clear")
	player1 = Player(str(input("First player's name => ")))
	player2 = Player(str(input("Second player's name => ")))
	

	
	while player1.totalscore < 150 and player2.totalscore < 150:
		print("{}'s Score: {}\n".format(player1.name, player1.totalscore))
		time.sleep(0.1)
		print("{}'s Score: {}\n".format(player2.name, player2.totalscore))
		time.sleep(0.1)
		print("\n")
		time.sleep(0.1)
		chooseplayer = str(input("Enter either 1 or 2 to update that player's score =>"))
		if chooseplayer == "1":
			amount = int(input("Points scored => "))
			dispamount = str(amount)
			time.sleep(0.2)
			player1.score(amount)
			time.sleep(0.2)
			os.system("clear")
			
			print("{} points added to {}'s total".format(dispamount, player1.name))
			time.sleep(0.4)
			os.system("clear")
			
		elif chooseplayer == "2":
			amount = int(input("Points scored => "))
			time.sleep(0.2)
			player2.score(amount)
			time.sleep(0.2)
			os.system("clear")
			
			print("{} points added to {}'s total".format(dispamount, player2.name))
			time.sleep(0.4)
			os.system("clear")
			
		else:
			print("Invalid Input\n")
			time.sleep(0.1)
			pass
		
	if player1.totalscore >= 150:
		print("{} Won!\n".format(player1.name))

	elif player2.totalscore >= 150:
		print("Player 2 Won!\n".format(player2.name))
		
	


if __name__ == "__main__":
	main()	
