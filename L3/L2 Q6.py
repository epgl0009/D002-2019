    
#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)
print ("shhh, Dave hides %s bananas" % n)
# define a flag for found/not found and counter on how many trials
found = False
count = 0
#Step 4: Give three chances to the players 
print("You have three chance!")
while count < 3:
    m=int(input("Your guess: "))
    if m < 1 or m > 100:
        print("wrong input,guess number between 1 and 100")
        count=count+1
    elif m > n:
        print("Your guess is too high")
        count=count+1
    elif m < n:
        print("Your guess is too low")
        count=count+1
    elif m == n:
        count=count+1
        found = True
        break
#Step 5: Display a message
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid! Try again next time")
