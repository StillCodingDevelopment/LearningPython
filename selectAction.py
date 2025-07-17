from createPassword import createRandomPassword


def selectAction():
    mainInput = input()

    if mainInput == "/help":
        print("""
        Available commands:
        /help - shows this help message
        /createPassword - creates a random password
        /letsGamble - starts a gambling game (not implemented yet)    
        /exit - exits the program (not implemented yet)
        """)

    elif mainInput == "/createPassword":
        createRandomPassword()

    elif mainInput == "/letsGamble":
        input("This feature is not implemented yet. Press Enter to continue...")

    elif mainInput == "/exit":
        input("This feature is not implemented yet. Press Enter to continue...")

    else:
        print("Syntax Error ;)")
        print("type '/help' to see the legal commands" )
