def main():
    
    correct = 0
    total = 0

    while True:
        try:
            difficulty = int(input("Enter difficulty (1-3): "))
            if difficulty in [1,2,3]:
                break
            else:
                print("please enter a number that is either 1, 2, or 3. stop being silly")
        except ValueError:
            print("bro do you even know what a number is")
    
    while True:
        try:
            num_questions = int(input("Enter amount of questions (1-10): "))
            if num_questions - 1 in range(10):
                break
            else:
                print("do you know what 1-10 means. it means you can only input numbers one through ten. Count with me: 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10!")
        except ValueError:
            print("bro do you even know what a number is")

    for lol in range(num_questions):
        total += 1
        tries = 3
        number1, number2 = generate_random(difficulty)
        while tries > 0:
            try:
                answer = int(input(f"\nQuestion {lol + 1} | What is {number1} + {number2}? "))
                if answer == number1 + number2:
                    print("Great job! :)\n")
                    correct += 1
                    break
                else:
                    tries -= 1
                    print(f"Tries left {tries} | I GET ANGRIER FOR EVERY PROBLEM YOU GET WRONG. I HEAR EVERY DOOR YOU OPEN. >:(\n")
                    if not tries > 0:
                        print(f"wow, you're really dumb! The answer to {number1} + {number2} = {number1 + number2}")
                        break
            except ValueError:
                tries -= 1
                print(f"Tries left {tries} | math is about numbers, stop putting stuff other than numbers please and thank you.")
                if not tries > 0:
                    print(f"wow, you're really dumb! The answer to {number1} + {number2} = {number1 + number2}")
                    break

    percent = correct/total*100
    print(f"\nYour grade: {percent:.2f}%")

    if percent >= 99:
        print("A+, nerd.")
    

def generate_random(difficulty):
    import random
    if difficulty == 1:
        return random.randint(0,9), random.randint(0,9)
    elif difficulty == 2:
        return random.randint(10,99), random.randint(10,99)
    elif difficulty == 3:
        return random.randint(100,999), random.randint(100,999)

main()