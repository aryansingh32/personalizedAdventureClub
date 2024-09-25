#Takes Valid Input
def getValidInput(prompt):
    while True:
        try:
            userInput=int(input(prompt))
            return userInput
        except  ValueError:
            print("Oops! It looks like you've entered an invalid value. Please reenter a valid positive integer.")
#Takes Valid Budget from user
def budgetHandling():
    return getValidInput("To help us plan your adventure, could you share your daily budget? ")
#Takes Number of Days User Wants to Travel 
def daysHandling():
    return getValidInput("How many days would you like your adventure to last? ")
#Checks Budget for luxurious or average
def dailyBudget(budget):
    #budget=budgetHandling()
    if budget>= 500:
        print("You’re planning a luxurious experience! Get ready for best adventures.")
    elif 200<=budget<=499:
        print("That's a solid budget! You’ll have a comfortable and enjoyable experience.")
    elif 0<budget< 200:
        print("A modest budget! We’ll ensure you still have a wonderful time.")
    else:
        print("Oops! It looks like you've entered an invalid amount. Please enter a positive amount.")
    return budget
#Takes Destination from User
def destination():
    while True:
        choice =input("Where would you like to explore? Please choose between 'mountain' or 'beach': ").strip().lower()
        if choice== "mountain":
            print("Great choice! You've selected the mountain as your adventure destination.")
            return choice
        elif choice=="beach":
            print("Fantastic! You've chosen the beach for your adventure.")
            return choice
        else:
            print("It seems like you haven't made a valid selection. Please restart and choose either 'mountain' or 'beach'.")   
#Take name as Input and print Welcome Message
def welcomeMsg():
    name = input("Welcome to the Personalized Adventure Club! May I have your name, please? ").strip().title()
    msg = f"\nHello, {name}! We're excited to have you on a journey with us!"
    print(msg)
    return name
#Main Function This all The other functions are called.
def main():
    print("Let's create a personalized adventure plan for you!")

    # Name Handling
    name=welcomeMsg()

    # Choice for Destination
    choice=destination()

    # Daily Budget
    budget=budgetHandling()
    dailyBudget(budget)


    # Travel Days
    days = daysHandling()

    # Final Plan Summary
    print(f"\nYour adventure plan is all set, {name}!\nDestination: {choice.title()}\nDuration: {days} day(s)\nEstimated total cost: ${budget * days}\nWe hope you have an amazing journey ahead!")
    print('Thank you for choosing the Personalized Adventure Club!')
#Main function call
main()

