def intelligent_guessing_agent(low=1, high=100):
    print(f"Think of a number between {low} and {high}, and I will find it!")
    print("Provide feedback: 'high' (if my guess is too high), "
          "'low' (if too low), or 'correct' (if I got it right).\n")
    
    attempts = 0
    current_low = low
    current_high = high

    while current_low <= current_high:
        guess = (current_low + current_high) // 2
        attempts += 1
        
        print(f"My guess is: {guess}")
        feedback = input("Is this high, low, or correct? ").strip().lower()
        
        if feedback == 'correct':
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        elif feedback == 'high':
            current_high = guess - 1
        elif feedback == 'low':
            current_low = guess + 1
        else:
            print("Invalid feedback! Please type 'high', 'low', or 'correct'.")
            attempts -= 1 


if __name__ == "__main__":
    intelligent_guessing_agent(1, 100)