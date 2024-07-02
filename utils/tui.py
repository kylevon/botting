def get_integer_input(prompt: str) -> int:
    while True:
        try:
            user_input = int(input(prompt + ": "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")
