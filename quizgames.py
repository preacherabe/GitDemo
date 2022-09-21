print("Welcome to my Bible Quiz")

playing = input('Do you want to play Bible Game? \n')

if playing!= "yes":
    quit()
    
print("Okay, let's play the game")
score = 0

answer = input('What does the Bible mean? \n')

if answer == "book":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input('Who is the first king of Israel? \n')

if answer == "God":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input('Who betrayed the Lord Jesus Christ? \n')

if answer == "Judas":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input('What is the first book of the New Testament? \n')

if answer == "Matthew":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input('Is Christ coming back again? \n')

if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input('How many book are in the whole book? \n')

if answer.lower() == 66:
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
    print("You got " + str(score)  + " Bible Question right!")
    
end_game_message = input("Do you still want to play more?")

if answer == "yes":
    print("Good Job")
    
