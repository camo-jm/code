# rock paper scissors
import random

player = int(input("rock=0/paper=1/scissors=2: "))
assert player in [0, 1, 2], "Invalid choice!"

result = (random.randrange(0,2) - player ) % 3 # this only works because it's not a pair number

if result == 0:
    print("Tie!")
elif result == 1:
    print("You won!")
else:
    print("You lost!")
