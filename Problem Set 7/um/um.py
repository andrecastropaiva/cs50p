import re


def main():
    print(count(input("Text: ")))

# counting word um using regex
def count(word):
    word_um = re.findall(r'\bum\b', word, re.IGNORECASE) # uses findall() method to find word um in  asentence, ignores case
    return len(word_um) # returns the number of um that appears in a sentence






if __name__ == "__main__":
    main()