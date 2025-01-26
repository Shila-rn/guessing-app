import random


def guessing():
    number = random.randint(1, 50)
    guess = None
    attempt = 0
    max_try= 5
    print(f"you have {max_try} chamces to guess the number")
    while guess != number and attempt<max_try:
        guess = int(input("enter your guess: "))
        attempt += 1
        if guess==number:
            print(f"congradulations you winn. you guessed the number in {attempt} tries ")
            return 
        elif abs (guess- number) <= 3:
            print("perfect  you are soooo close")
        elif abs (guess - number) <= 6 :
            print("ummm, not bad")
        
        else:
            print(" it was too far")
    if guess != number:
        print(f"game over!!!!. the correct answer is {number}")
    
while True:
    guessing()
    play_again = input("Do you want to play again? (yes/no):" ).strip().lower()
    if play_again != "yes":
        print("ok :))) it was fun I hope see you later")
        break


