import random
number = random.randint(1,100)
attempts = 0
print("guess number betwwen 1 to 100:")
while True:
    guess = int(input("your guess"))
    attempts += 1
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print(f"hooray! you got it in {attempts} attempts") 
        break  

