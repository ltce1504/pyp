def personalized_greeting(name):
    greeting = f"Hello, {name}! Welcome to our community."
    return greeting 
if __name__ == "__main__": #staring of main program
    user_name = str(input("Please enter your name: "))
    greeting_message = personalized_greeting(user_name)
    print(greeting_message)