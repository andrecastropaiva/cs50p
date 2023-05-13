import re


def main():
    print(parse(input("HTML: "))) # takes user input



def parse(s):
    # regex pattern - compiled once, outside the function...so it doesn't need to be re-compiled each time we call the function
    # . means any character
    # + 1 or more times
    # " expresses where the link ends
    # ?: make the group non-capture...so when we user .group() it won't count that group becauswe is optional, can be there or not
    pattern = re.search(r'https?://(?:www\.)?youtube\.com/embed/(.+)"', s)


    # conditionals
    # method to extract the captured text from the first (and only) capturing group in the pattern, which corresponds to the video id
    if pattern:
        return f"https://youtu.be/{pattern.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()
