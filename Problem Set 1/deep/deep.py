# Taking user answer
def deep():
    question_answer = input("What is the answer to The Great Question of Life, the Universe, and Everything?")

# Contition statement to verify answer
# lower forces print everything in lowercase
# strip removes spaces before and after
    if question_answer.lower() == "forty-two":
        print("Yes")
    elif question_answer.lower() == "forty two":
        print("Yes")
    elif question_answer.strip() == "42":
        print("Yes")
    else:
        print("No")

# Calling function back
deep()

