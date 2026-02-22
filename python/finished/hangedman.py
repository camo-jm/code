import random

words = ["hola", "adios", "the", "quick", "brown", "fox"
         , "jumps", "over", "a", "lazy", "dog"]

limbs = 5
correct = random.choice(words)
answer = "asdf"


print(f"welcome! the word contains {len(correct)} letters, and you have {limbs} tries")

while (answer != correct) and (limbs > 0):
    answer = input(f"word: {'_' * len(correct)}\nlives: {limbs}\nyour answer: ")
    limbs -= 1

if answer == correct:
    print("congrats!!! you win!!!")
else:
    print("better luck next time pal :/")
