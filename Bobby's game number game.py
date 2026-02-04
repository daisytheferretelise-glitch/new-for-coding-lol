import random
playing=True
number=str(random.randint(0,20))
print("Bobby said I will genarate a number from 0,20 and you have to guess the number")

while playing:
     guess=input("Bobby says give it your best try \n")
     if number==guess:
      print("Bobby admits you won")
      print("That guess was right on the spot you're right the answer is", number)
      break
     else:
        print("Bobby laughed at you how does it feel sad... why? You got it wrong even though your in bobs body \n")