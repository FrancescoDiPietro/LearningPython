import random

print("Guess the number between 1 and 100")
n = random.randint(1,100)
condition = True
times = 0

while condition and times<=7:
	num = int(input())
	if(num<n):
		print("number is too low")
	else:
		print("number is too high")
	if(num == n):
		condition=False			
	times +=1

if(times<=7 and num == n):
	print("Good job the number is indeed " + str(n) )
else:
	print("Sorry you are too bad at this game and lost the number was " + str(n))
