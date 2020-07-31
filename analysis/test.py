# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":
    user_numbers = int(input("How many numbers?"))
    for number in range(user_numbers):
        print(number)
    user_play = input("Do you want to continue: (y)es or (n)o")