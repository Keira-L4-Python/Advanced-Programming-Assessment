import random

# Function to load jokes from a text file
def load_jokes(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()

    # Split the file content by empty lines
    joke_entries = content.split('\n\n')
    jokes = []

    for joke in joke_entries:
        # Each joke should have a setup and punchline on separate lines
        lines = joke.split('\n')
        if len(lines) == 2:
            setup, punchline = lines[0], lines[1]
            jokes.append((setup, punchline))
    
    return jokes

# Main program function
def main():
    # Load jokes from the file
    jokes = load_jokes('jokes.txt')

    print("Alexa, tell me a joke!\n")

    # Loop to allow multiple jokes
    while True:
        # Select a random joke from the dataset
        setup, punchline = random.choice(jokes)
        
        # Display the joke setup
        print(f"Setup: {setup}")
        
        # Prompt the user to press Enter to see the punchline
        input("\nPress Enter to reveal the punchline...")
        
        # Display the punchline
        print(f"Punchline: {punchline}\n")
        
        # Ask if the user wants to hear another joke
        again = input("Do you want to hear another joke? (y/n): ")
        if again.lower() != 'y':
            print("Goodbye! Have a great day!")
            break

if __name__ == "__main__":
    main()
