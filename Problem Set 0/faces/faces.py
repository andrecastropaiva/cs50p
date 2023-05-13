# Ask message to user
def main():
    # Get user input
    message = input()

    # Call convert function
    result = convert(message)

    # Print the result
    print(result)


def convert(message):

    # Replace :) for happy emoji face
    message2 = message.replace(":)", "🙂")
    # Replace :( for sad emoji face
    message3 = message2.replace(":(", "🙁")

    # Return string
    return message3


main()
