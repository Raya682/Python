from random import randint

def game():
    
    running = True

    while running:
        number = randint(1, 100)
        guesses = 0
        
        while True:
            try: 
                guess = int(input("Enter a number between 1-100: "))
                guesses += 1
            except ValueError:
                print("Invalid input. Please enter a valid number!")
                continue
            
            if guess > 100 or guess < 0:
                print("The number you've entered is out of range!")                    
            elif guess < number:
                print("Too Low!")
            elif guess > number:
                print("Too High!")
            else:
                print("CORRECT!")
                break
            
        print(f"Guesses: {guesses}")
        if input("Play again? (yes/no) ").lower() != "yes":
            running = False
            
    print("Adios!")
    
# Call the game function to start the game
game()