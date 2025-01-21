def tell_jokes(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            jokes = file.read().split("\n\n")  # Assuming jokes are separated by blank lines

        jokes = [joke.strip() for joke in jokes if joke.strip()]

        if not jokes:
            print("No jokes found in the file.")
            return

        print("Welcome to the Joke Teller!")
        
        joke_index = 0

        while True:
            user_input = input("Do you want to hear a joke? (yes/no): ").strip().lower()

            if user_input in ["yes", "y"]:
                print(f"\nJoke {joke_index + 1}:\n{jokes[joke_index]}\n")
                joke_index = (joke_index + 1) % len(jokes)  # Cycle through jokes
            elif user_input in ["no", "n"]:
                print("Thanks for stopping by! Have a great day!")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "Jokes.txt"  # Replace with your actual file path

# Start the interactive joke-telling session
tell_jokes(file_path)
