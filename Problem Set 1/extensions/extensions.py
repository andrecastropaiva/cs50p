def main():

    # Taking user input
    extensions = input("File name:")

    # Check the input is case insensitive and store results to a new variable
    new_extensions = extensions.lower()

    # Conditionals using membership method
    if ".gif" in new_extensions:
        print("image/gif")
    elif ".jpg" in new_extensions:
        print("image/jpeg")
    elif ".jpeg" in new_extensions:
        print("image/jpeg")
    elif ".png" in new_extensions:
        print("image/png")
    elif ".pdf" in new_extensions:
        print("application/pdf")
    elif ".zip" in new_extensions:
        print("application/zip")
    elif ".txt" in new_extensions:
        print("text/plain")
    else:
        print("application/octet-stream")


# Calling function
main()
