from time import sleep

def countDown():
    time = int(input("Enter the time in seconds: "))
    for i in range(time, 0, -1):
        seconds = i % 60
        minutes = int(i/60) % 60
        hours = int(i/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        sleep(1) # Our program will sleep for the given amount of seconds
    print("TIMES UP!")
    
    
def counter():
    time = int(input("Enter the time in seconds: "))
    for i in range(0, time+1):
        seconds = i % 60
        minutes = int(i/60) % 60
        hours = int(i/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        sleep(1) # Our program will sleep for the given amount of seconds
    print("TIMES UP!")

count = input("Countdown or Counter: ").capitalize()

if count == "Countdown":
    try:
        countDown()
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")
        countDown()
        
elif count == "Counter":
    try:
        counter()
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")
        counter()
        
else:
    print("Invalid Input!")